from fileinput import close

import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://www.cyberforum.ru/python-beginners/" #первоначальная страница

with open("темы питона 2.csv", "w", encoding= "UTF-8-sig", newline= "" ) as f:
    write = csv.writer(f, delimiter=";")
    write.writerow(["Заголовок", "Ссылка"])

#счетчик страниц
    page = 1
#цикл перебора страниц
    while url:
        print(f"Парсим страницу №{page}")
        response = requests.get(url,
        headers = {"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        heading = soup.find_all("a", id=lambda x: x and x.startswith("thread_title_"))

        time.sleep(1)

        for h in heading:
            title = h.text.strip()
            link = h["href"]
            if not link.startswith("https"):
               link = "https://www.cyberforum.ru/" + link
            write.writerow([title, link])



        next_page = soup.find("a", rel = "next")

        if next_page:
            url = next_page['href']



        else:
            url = None

        page += 1

close()