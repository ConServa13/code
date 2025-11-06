import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span",
class_="text").text
    author = quote.find("small",
class_="author")
    print(f"{text} - {author}".encode('utf-8', 'ignore').decode('utf-8')) 