import requests
from bs4 import BeautifulSoup

url = "https://www.citilink.ru/catalog/videokarty/?ysclid=mh8fp4ogyk120914662"

response = requests.get(url,
headers = {"User-Agent": "Mozilla/5.0"})

html = response.text

soup = BeautifulSoup(html, "html.parser")

carts = soup.find_all("div", class_="app-catalog-18v0w1v-StyledName e17y4iou0")

for cart in carts:


    m_tg = cart.find("div", class_="app-catalog-18v0w1v-StyledName")
    print(m_tg)
    #pr = cart.find("div", class_= "text").text
#print(carts)