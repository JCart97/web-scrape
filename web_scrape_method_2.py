import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import timezone
import datetime
dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)

driver = webdriver.Chrome(executable_path='/Users/Jack/Documents/GitHub/chromedriver')
driver.get('https://www.currys.co.uk/computing/laptops/laptops')
products=[] #List to store name of the product
prices=[] #List to store price of the product
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
driver.quit()

for a in soup.findAll('div', attrs={'class':'row product-grid list-view justify-content-center'}):
  for b in a.findAll('span', attrs={'class':'list-product-tile-name desktop-only'}):
    name = b.find('a',attrs={'class':'link text-truncate pdpLink'})
    if name not in products:
      products.append(name.text.strip())
  for desktops in a.findAll('div',attrs = {'class': 'desktop-only'}):
    for price in desktops.findAll('span', attrs={'class':'sales'}):
      price.find("content")
      prices.append(price.text.strip().replace('£',''))

df = pd.DataFrame({'product_name': products, 'prices': prices, 'currency': 'GBP', 'as_of': utc_time})
df.to_csv('products.csv', index=False, encoding='utf-8')