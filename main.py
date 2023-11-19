import requests
from bs4  import BeautifulSoup
import lxml


user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
hearders = {"User-agent": user}
session = requests.Session()
for j  in range (1, 7):
    print(f"Page {j}")
    url = f"https://cash-bacer.club/shops?page={j}"
    response = session.get(url, hearders=hearders)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text,)
        soup = BeautifulSoup(response.text,)
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all('div', class_="row col-lg-9 com-md-9 col-12")
        for i  in all_products:
            title = i.find('div', class_="shop-title")
            cashback = i.find("div", class_="shop-rate")
            print(title.text, cashback.text)
