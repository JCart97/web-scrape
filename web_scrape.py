import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/Jack/Documents/GitHub/chromedriver')
driver.get('https://www.gov.uk/')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
driver.quit()

for element in soup.findAll(attrs='homepage-services-and-info__list'):
  data_attribute = element.find('a')
  for data_attribute in element:
    tag = data_attribute.find('data-track-dimension')
  if tag not in results:
    results.append(tag.text)
print(results)
#this is a comment.