# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:18:06 2018

@author: prasad
"""

from bs4 import BeautifulSoup
import requests
import re

url= "www.dinamani.com/agriculture/"
r= requests.get("http://"+url)
data = r.text

soup = BeautifulSoup(data, "html.parser")
all_news = soup.find(class_='list-group')
#title = all_news.find_all(text = True)
#print(title)

news = {}
link = []
for i in all_news.find_all('a'):
        link.append(str(i.get('href')))
#print(link)

title = []
for i in range(len(link)):
        title.append(link[i][48:-13])

for i in range(len(link)):
        news[title[i]] = link[i]


print(news)


