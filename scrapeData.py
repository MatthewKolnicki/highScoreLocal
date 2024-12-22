# webscrape basketball-reference.com box scores for all games

import requests

url = "https://www.basketball-reference.com/players/a/abdulka01.html"

response = requests.get(url)

print(response.json())