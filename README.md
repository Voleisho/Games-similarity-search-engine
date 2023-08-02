# Games-similarity-search-engine

This repository contains an innovative Games Similarity Search Engine, developed as part of a university project, to help gamers explore related titles from a digital marketplace for gamers. The project encompasses three main components:

## Web Scraping 
Leveraging web scraping techniques, the project gathers essential game information from the digital gaming marketplace. Collected data includes game titles, genres, descriptions, prices, and links.

## Similarity Search Engine
The Search Engine component is a key part of the project responsible for facilitating game recommendations and categorizing games based on user input.

### Functionality
The search engine leverages the power of pre-trained transformer models from the **transformers** library. It processes user input, whether it's a game title for recommendation or a game category for grouping similar games.

#### 1. Game Recommendations:
The search engine utilizes the DistilBERT model from the transformers library to perform similarity analysis between the user-provided game title and the game descriptions available in the dataset. It calculates cosine similarity scores based on the game descriptions and provides a list of game recommendations that are similar to the user's input game title.

#### 2. Game Categorization:
The search engine enables users to input a game category of their interest. It uses the pre-trained DistilBERT model to calculate cosine similarity between the user-provided category and the game categories available in the dataset. The search engine then returns a list of games that belong to the most similar category, along with their prices.

## Dialogflow Integration with Flask
The Dialogflow Integration part focuses on incorporating the search engine functionality into a chatbot powered by Dialogflow. The chatbot will enable users to interact with the game similarity search engine through natural language queries.


