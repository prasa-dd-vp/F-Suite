from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
import re
import pyrebase
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyrebase
#res = 0
# Create your views here.

def handShake(request):
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
  print(len(link))
  title = []
  for i in range(6,12):
          title.append(link[i][48:-13])
          news[title[i-6]] = link[i]  
  #print(news)

  # Get the firebase credentials
  config = {
    "apiKey": "AIzaSyA2t_s0Te5StZBe8yYqiOA8Sb478bFn84c",
    "authDomain": "current-trends-farmer.firebaseapp.com",
    "databaseURL": "https://current-trends-farmer.firebaseio.com",
    "projectId": "current-trends-farmer",
    "storageBucket": "current-trends-farmer.appspot.com",
  }

  #print(news)
  # Initialize the configurations
  firebase = pyrebase.initialize_app(config)
  
  db = firebase.database()
  db.child("latest_news").set(news)
  print("success!")
  #print(news)
  return JsonResponse({"Result" : "done"}, status = 201)



def production_prediction(request, area):
  if request.method == "POST":
    area = int(area)
    #print(area)
    dataset = pd.read_csv(r'F:\projects\Smart_Farming\tn_clean.csv')
    temp = pd.get_dummies(dataset['Season'])
    dataset = dataset.drop(['Season'], axis =1)
    dataset = dataset.join(temp)
    X = dataset.iloc[:, [5]].values
    y = dataset.iloc[:, 6].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.26, random_state = 0)

    # Fitting Multiple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)

    #print("The salary for the specified experience will be:%10d" % regressor.predict(np.array([[area]])))
    result = regressor.predict(np.array([[area]]))
    global res
    res = str(int(result[0]/1000))
    #print(int(result[0]))
    return JsonResponse({"Result" : "success!"}, status = 201)

def return_data(request):
  if request.method == "POST":
    print(res)
    return JsonResponse({"Result_data" : res})

def firebase_upload(request):
  if request.method == "POST":
    

    # Get the firebase credentials
    config = {
      "apiKey": "AIzaSyA2t_s0Te5StZBe8yYqiOA8Sb478bFn84c",
      "authDomain": "current-trends-farmer.firebaseapp.com",
      "databaseURL": "https://current-trends-farmer.firebaseio.com",
      "projectId": "current-trends-farmer",
      "storageBucket": "current-trends-farmer.appspot.com",
    }
    # Initialize the configurations
    firebase = pyrebase.initialize_app(config)


    data = {'0': 'மழைக்கான வாய்ப்பு உள்ளது', '1':'சூறாவளி எச்சரிக்கை', '2':'புயலுக்கு வாய்ப்பு உள்ளது', '3':'சில நாட்களுக்கு உலர் வானிலை',
            '4':'மிக அதிக வெப்பத்திற்கான வாய்ப்பு உள்ளது'}
    db = firebase.database()
    db.child("suggestions").set(data)



