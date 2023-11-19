import openpyxl
import requests
from bs4 import BeautifulSoup
import lxml

url = "https://allo.ua/ua/products/internet-planshety/"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-agent":user}

session = requests.Session()

response = session.get(url, headers=headers)

book = openpyxl.Workbook()
book.save("catalog.xlsx")
sheet = book.active
sheet["A1"] = "Title"
sheet["B1"] = "Review"
sheet["C1"] = "Price"
count = 2


for j in range(1,26):
    print(f'Page {j}')
    with open('catalog.txt', "a", encoding="utf-8") as file:
      url = 'https://allo.ua/ua/products/internet-planshety/p-"[j]/'
      response = session.get(url,headers=headers)

      if response.status_code == 200:
          soup = BeautifulSoup(response.text,"lxml")
          all_products = soup.find_all("div", class_="products-layout__item")
          for i in all_products:
              if i.find('div', class_="product-card__content"):
                  title = i.find('a', class_="product-card__title")
                  print(title.text)
                  try:
                     review = i.find('span', class_="review-button__text review-button__text--count")
                  except NameError:
                       print("нема")
                  print(review.text)
                  price = i.find('div', class_="v-pb__cur")
                  print(price.txt)
              else:
                  print("Error")
                   #file.write(f"{titel.text{}review.text}{price.text} \n")

    for i range(len(all_products)):
        title = all_products[i].find('a', class_="product-card__titel")
        review = all_products[i].find('span', class_="review-button__text review-button__text--count")
        price = all_products[i].find('div', class_="v-pb__cur")
        sheet[f"A{i}"] = title.text
        sheet[f"B{i}"] = review.text
        sheet[f"C{i}"] = price.text
        count =+ 1

book.save('catalog.xlsx')
book.close()




