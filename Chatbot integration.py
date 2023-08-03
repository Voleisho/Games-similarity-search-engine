tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")


df = pd.read_csv('data.csv')
descriptions = df['Description'].tolist()
categories = df['Genre'].tolist()
names = df['title'].tolist()

#istrinam nan reiksmes,del visa ko
df2=df.dropna().reset_index(drop=True)


def games_recommender(titlee):
    with open('Vectors_names.pkl', 'rb') as f:
     probs = pickle.load(f)



    vector_of_name = model(**tokenizer(titlee, return_tensors='pt', truncation=True, padding = True))[0].detach().squeeze()

    similarity = cosine_similarity(vector_of_name, probs)

    games = []
    for arr in similarity:
      for i, each_val in enumerate(arr):
         games.append([names[i],each_val])

    final_games = sorted(games, key=lambda x: x[1], reverse=True)

    for arr in final_games[0:1]:
    # print(f'\nScore : \n\n  {arr[1]}')
      print(f'\nGame : \n\n {arr[0]}')

    arr = np.delete(arr,-1)

    arr = ''.join(arr)

    with open('Vectors_names.pkl', 'rb') as f:
     probs1 = pickle.load(f)


    similarity2 = cosine_similarity(probs1)

    indexes = pd.Series(df2['title'])

    similar_games = []
    idx = indexes[indexes == arr].index[0]  
    similarities = pd.Series(similarity2[idx]).sort_values(ascending = False) 
    indexes_count = list(similarities.iloc[1:6].index)

    for i in indexes_count:  
        similar_games.append(list(df2['title'])[i])

   

    return similar_games


def get_games_by_category(name):
    with open('Vectors_category.pkl', 'rb') as f:
     probs = pickle.load(f)

    vector_of_category = model(**tokenizer(name, return_tensors='pt', truncation=True, padding = True))[0].detach().squeeze()

    similarity_of_category = cosine_similarity(vector_of_category, probs)

    categor = []
    for arr_of_category in similarity_of_category:
      for i, each_val in enumerate(arr_of_category):
          categor.append([categories[i],each_val])

    final_categor = sorted(categor, key=lambda x: x[1], reverse=True)

    for arr_of_category in final_categor[0:1]:
      print(f'\ncategory : \n\n {arr_of_category[0]}')

    arr_of_category = np.delete(arr_of_category,-1)

    arr_of_category = ''.join(arr_of_category)

    similarity_of_category2 = cosine_similarity(probs)

    indexes = pd.Series(df2['Genre'])

    similar_games = []
    Prices = []
    idx = indexes[indexes == arr_of_category].index[0]  
    similarities = pd.Series(similarity_of_category2[idx]).sort_values(ascending = False) 
    indexes_count = list(similarities.iloc[1:6].index)  

    for i in indexes_count:  
        similar_games.append(list(df2['title'])[i])
        #similar_games.append(list(df2['Genre'])[i])
        Prices.append(list(df2['Price'])[i])

    Price = list(map(lambda x: x.strip('€'), Prices))

    pricess = [float(i) for i in Price]

   
    technologies= {
    'names':similar_games,
    'prices' :pricess
    }

    df_games = pd.DataFrame(technologies)
    #Price = filter(None, Price)

    df_games = df_games.sort_values(by=['prices'])

    first_value = list(df_games.iloc[-1])


    first_value = str(first_value)

    #foo = [float(i) for i in Price]


    similar_games = str(similar_games)

    

    #print('average price of games in this category is:\n' + avg + "€")

    #print('games in this category\n'+ name + '\nare these:\n')


    return first_value


   
  


app = flask.Flask(__name__)



def handle_webhook(request):

  game_name = request['queryResult']['parameters']['Name']


  similar_games = games_recommender(game_name)


  if similar_games:
   
    response_text = 'Here are some similar games for {}: {}'.format(game_name, ',\n'.join(similar_games))
   
  else:

    response_text = 'Sorry, we could not find any similar games for {}'.format(game_name)
  res = {'fulfillmentText': response_text}
  return res


def handle_webhook1(request):

  category = request['queryResult']['parameters']['Games-category']


  games_in_category = get_games_by_category(category)


  if games_in_category:
    response_text = 'Here is the cheapest game in the category of {}: {}'.format(category,''.join(games_in_category))
  else:
    response_text = 'Sorry, we could not find any in this category {}'.format(category)
  res = {'fulfillmentText': response_text}
  return res

@app.route('/webhook', methods=['POST'])
def webhook():

  req = request.get_json(silent=True, force=True)

  intent = req['queryResult']['intent']['displayName']


  if intent == 'Game-Names':

    res = handle_webhook(req)

  elif intent == 'Get-games-by-category':
    res = handle_webhook1(req)

  else:
    res = {'fulfillmentText': 'kazkas neveikia :('}


  res = jsonify(res)
  res.headers['Content-Type'] = 'application/json'
  return make_response(res)

if __name__ == '__main__':
  app.run()