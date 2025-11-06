import requests
from bs4 import BeautifulSoup

url = "https://yandex.ru/search/?text=время+в+мире&clid=2270455&banerid=6301000000%3ASW-8670539ce8ff&win=677&lr=10716"
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")

time = soup.find_all("main", class_= "main" )

print (time)