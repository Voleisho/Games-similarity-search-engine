import requests 
from bs4 import BeautifulSoup
import csv
from collections.abc import Mapping
import re
from requests import get
import sys
import numpy as np
import time
import random
import pandas as pd


pages = np.arange(1,250,1)

product_links = []

for page in pages:
    #time.sleep(random.randint(5,10))
    headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

    start_url = 'https://www.gamesmarketplace.com/store/games?page=' + str(page) + '.html'

    
    #web_page = requests.get(start_url, headers=headers, timeout=30)
    web_page = None

    while web_page is None:
     try:
      web_page = requests.get(start_url, headers=headers, timeout=30)
     except requests.HTTPError as e:
      print(f"[!] Exception caught: {e}")
      time.sleep(random.randint(5,10))
 
 
     soup = BeautifulSoup(web_page.content, 'html.parser')
    

    for link in soup.find_all('a', class_='oSVLlh'):
       if link['href'] not in product_links:
         product_links.append('https://www.gamesmarketplace.com' + link['href'])
    with open('data.csv', 'w') as csv_file:

         writer = csv.writer(csv_file)
         writer.writerow(['title', 'Price', 'Genre', 'Description', 'Link'])
    
         for product_url in product_links:
           product_page = requests.get(product_url)
           product_soup = BeautifulSoup(product_page.content, 'html.parser')
           
           try:
             product_name = product_soup.find('h1', class_='C68dpx').text.strip()
           except:
             product_name = 'None'
     
           try:
             price = product_soup.find('span', class_='L5ErLT').text
           except:
             price = 'None'

           try:  
             product_genre = product_soup.find('ul', class_='aoHRvN').text.strip()
           except:
             product_genre = 'None'
    
           try:  
             product_description = product_soup.find('div', class_=re.compile("Wz6WhX")).text.strip()
           except:
             product_description = 'None'

           writer.writerow([product_name, price, product_genre, product_description, product_url])


