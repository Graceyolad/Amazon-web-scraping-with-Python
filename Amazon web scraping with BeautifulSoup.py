#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd
import smtplib


# In[2]:


#connecting to website to get needed data

URL = 'https://www.amazon.de/Apple-iPhone-14-Pro-256/dp/B0BDJCM1SG/ref=sr_1_2_sspa?crid=2VBVM8UZB511B&keywords=iphone%2B14&qid=1664872886&qu=eyJxc2MiOiI0LjI5IiwicXNhIjoiNC4yMyIsInFzcCI6IjMuMzIifQ&sprefix=iph%2Caps%2C805&sr=8-2-spons&language=en_GB&currency=EUR&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

product = soup2.find(id='productTitle').get_text()

ratings = soup2.find(id = 'acrCustomerReviewText').get_text()

rating_star = soup2.find(id = 'acrPopover').get_text()

price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()


print(product)
print(price)
print(ratings)
print(rating_star)


# In[3]:


#indexing out the values needed
price = price[price.index('€'):(price.index('€')) + 6]
price = price.strip()[1:]
product = product[product.index('A'):(product.index('('))]
product = product.strip()
ratings =ratings.strip()[:2]
rating_star = rating_star.strip()[:4]


print(product)
print(price)
print(ratings)
print(rating_star)


# In[4]:


#checking out today's date
today = datetime.date.today()
print(today)


# In[5]:


#creating an excel file to house the data 
header = ['Product', 'Price', 'Date', 'Ratings', 'Rating_star']
data = [product, price,today, ratings, rating_star]

with open('amazoniphone14dataset.csv', 'w', newline = '', encoding = 'UTF8') as f:
    writer =  csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[6]:


#importing and viewing the data as a dataframe
df = pd.read_csv(r'C:\Users\Grace\amazonphone14dataset.csv')
df


# In[ ]:


#appending data to the csv and automating the process
def check_price():
    
    URL = 'https://www.amazon.de/Apple-iPhone-14-Pro-256/dp/B0BDJCM1SG/ref=sr_1_2_sspa?crid=2VBVM8UZB511B&keywords=iphone%2B14&qid=1664872886&qu=eyJxc2MiOiI0LjI5IiwicXNhIjoiNC4yMyIsInFzcCI6IjMuMzIifQ&sprefix=iph%2Caps%2C805&sr=8-2-spons&language=en_GB&currency=EUR&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    product = soup2.find(id='productTitle').get_text()

    ratings = soup2.find(id = 'acrCustomerReviewText').get_text()

    rating_star = soup2.find(id = 'acrPopover').get_text()

    price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()
    
    price = price[price.index('€'):(price.index('€')) + 6]
    price = price.strip()[1:]
    product = product[product.index('A'):(product.index('('))]
    product = product.strip()
    ratings =ratings.strip()[:2]
    rating_star = rating_star.strip()[:4]
    
   
    import datetime
    today = datetime.date.today()
    
    import csv
    
    header = ['Product', 'Price', 'Date', 'Ratings', 'Rating_star']
    data = [product, price,today, ratings, rating_star]
    
    with open('amazoniphone14dataset.csv', 'a+', newline = '', encoding = 'UTF8') as f:
        writer =  csv.writer(f)
        writer.writerow(data)
    
    


# In[ ]:


#updating my data daily
while (True):
    check_price()
    time.sleep(86400)


# In[ ]:


df = pd.read_csv(r'C:\Users\Grace\amazonphone14dataset.csv')
df


# In[ ]:




