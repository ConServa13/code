import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("div", class_= "quote")

while url:
    for i in quotes:
        text = i.find("span", class_ = "text").text
        #print(f"{text}")

    next = soup.find_all("li", class_ = "next")
    for n in next:
        ne = n.find("a")
        url = None
print (ne)