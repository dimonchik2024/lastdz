import requests
import lxml
from bs4 import BeautifulSoup

session =requests.Session()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}


for j in range(1, 7):
    url = f"https://cash-backer.club/shops?page={j}"
    print(f"PAGE - {j}")
    response = session.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"lxml")

        allProduct = soup.find("div", class_="row col-lg-9 col-md-9 col-12")
        products = soup.find_all("div", class_="col-lg-2,col-md-3 shop-list-card pseud")

        for elem in products:
            name_company = elem.find("div", class_="shop-rate").text
            products = allProduct.find_all("div", class_="shop-rate").text

            with open("result.txt", "a", encoding="utf-8") as file:
                file.write(f"{name_company} -->> {procent}\n")
