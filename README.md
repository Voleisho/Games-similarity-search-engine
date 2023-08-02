# Games-similarity-search-engine

This repository contains an innovative Games Similarity Search Engine, developed as part of a university project, to help gamers explore related titles from a digital marketplace for gamers. The project encompasses three main components:

## Web Scraping 
The Web Scraping component employs powerful web scraping techniques to collect essential game information from the digital gaming marketplace. The data gathered includes game titles, prices, genres, descriptions, and links.

The provided code demonstrates the process of web scraping from a digital gaming marketplace. By utilizing libraries such as **requests**, **BeautifulSoup**, and **csv**, the code fetches data from multiple pages on the website. It iterates through a range of page numbers and extracts relevant information about games, such as their titles, prices, genres, and descriptions.

The collected data is then saved to a CSV file named `data.csv`, which acts as a structured dataset containing the necessary information about the games available on the platform.

## Similarity Search Engine
The Search Engine component is a key part of the project responsible for facilitating game recommendations and categorizing games based on user input.

### Functionality
The search engine leverages the power of pre-trained transformer models from the **transformers** library. It processes user input, whether it's a game title for recommendation or a game category for grouping similar games.

#### 1. Game Recommendations:
The search engine utilizes the DistilBERT model from the transformers library to perform similarity analysis between the user-provided game title and the game descriptions available in the dataset. It calculates cosine similarity scores based on the game descriptions and provides a list of game recommendations that are similar to the user's input game title.

#### 2. Game Categorization:
The search engine enables users to input a game category of their interest. It uses the pre-trained DistilBERT model to calculate cosine similarity between the user-provided category and the game categories available in the dataset. The search engine then returns a list of games that belong to the most similar category, along with their prices.

## Dialogflow Integration with Flask

The Dialogflow Integration with Flask enables the chatbot to seamlessly incorporate the game similarity search engine. Users interact with the search engine through natural language queries, receiving game recommendations and cheapest games in specific categories.

This integration leverages Flask as a webhook, handling user queries and invoking the search engine functions. The chatbot responds to users based on the results obtained from the search engine.


