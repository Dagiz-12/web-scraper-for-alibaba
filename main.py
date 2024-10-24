from bs4 import BeautifulSoup
import requests


content = requests.get(
    'https://www.alibaba.com/product-detail/Standard-Quality-CeraVes-Moisturizing-Cream-Body_10000012483822.html?spm=a2700.trademark.0.0.5beeHn9jHn9jO6').text

soup = BeautifulSoup(content, 'html.parser')
prices = soup.find_all('div', class_='price-item')
for price in prices:

    pri = price.find('div', class_='price').text
    qun = price.find('div', class_='quality').text
# for price in prices:
# quantity = prices.div.text
# \\   price = cards.a.text \\
    print(f'''prices: {pri}''')
    print(f'''quantity: {qun}''')
#  print(card_name)
