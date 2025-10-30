import requests
from bs4 import BeautifulSoup
import csv

from pyautogui import write

a = "https://www.cyberforum.ru/python-beginners"

url = a

response = requests.get(url,
headers = {"User-Agent": "Mozilla/5.0"})

html = response.text

soup = BeautifulSoup(html, "html.parser")

heading = soup.find_all("a", id=lambda x: x and x.startswith("thread_title_"))

#запись в файл
with open("темы питона.csv", "w", encoding="utf-8-sig", newline = "") as f:
    write = csv.writer(f, delimiter=";")
    write.writerow(["Заголовок", "Ссылка"])

    for a_tag in soup.find_all("a", id=lambda x: x and x.startswith("thread_title_")):
        title = a_tag.text
        link = a_tag["href"]
        write.writerow([title, link])



