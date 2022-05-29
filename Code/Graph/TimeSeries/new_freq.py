import json 
import datetime as datetime
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

import tweepy           # To consume Twitter's API


# Twitter App access keys for @user
CONSUMER_KEY = "LMb6DIm8jWSPZh3QZfjUqeXZE" 
CONSUMER_SECRET = "nIGcBLqqC5vMspxbJbiyvWYMY6Nu6ItY2tDvrp5jyoRzHg4J6P" 
ACCESS_TOKEN = "1098046038554767360-M0IL17I6bb1Hzho3gvMRKegOAFEY62" 
ACCESS_TOKEN_SECRET = "fkIjWg8VcMLaKo2O6wvA6BkK7f3scGy9mXPZlFabbtEjV" 

# Consumer API keys:
#CONSUMER_KEY = "4oqZjge7qM0n3WNftJiKHFtOF" #API key
#CONSUMER_SECRET = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP" 
#ACCESS_TOKEN = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT" 
#ACCESS_TOKEN_SECRET = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL" 


# Authentication and access using keys:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)



def set_attack_date():
    
    startdate = datetime.date(2012,3,1)
    enddate = datetime.date(2019,4,3)
        
    date_list = []    
    while startdate<=enddate:
        date_list.append(str(startdate))
        startdate = startdate + datetime.timedelta(days=1)
    
    selected_date = [[]]
    with open('/Users/junha_lee/desktop/attack_date.json','r') as atkfile:
        attack_date = json.load(atkfile)
    
    attack_date =  {"Attack": "2013-01-02"},{"Attack": "2013-02-01"},{"Attack": "2013-03-20"},{"Attack": "2013-03-21"},{"Attack": "2013-03-26"},{"Attack": "2013-04-05"},{"Attack": "2013-04-26"},{"Attack": "2013-05-15"},{"Attack": "2013-05-16"},{"Attack": "2013-07-19"},{"Attack": "2013-08-27"},{"Attack": "2013-12-05"},{"Attack": "2014-03-14"},{"Attack": "2014-07-11"},{"Attack": "2014-07-17"},{"Attack": "2014-07-29"},{"Attack": "2014-08-24"},{"Attack": "2014-08-27"},{"Attack": "2014-09-30"},{"Attack": "2014-10-20"},{"Attack": "2014-11-10"},{"Attack": "2014-11-17"},{"Attack": "2015-01-06"},{"Attack": "2015-01-07"},{"Attack": "2015-01-25"},{"Attack": "2015-04-09"},{"Attack": "2015-06-17"},{"Attack": "2015-08-07"},{"Attack": "2015-10-21"},{"Attack": "2015-11-25"},{"Attack": "2015-12-31"},{"Attack": "2016-01-19"},{"Attack": "2016-01-20"},{"Attack": "2016-01-25"},{"Attack": "2016-01-29"},{"Attack": "2016-06-20"},{"Attack": "2016-11-08"},{"Attack": "2016-11-27"},{"Attack": "2016-11-28"},{"Attack": "2017-02-27"},{"Attack": "2017-03-10"},{"Attack": "2017-03-11"},{"Attack": "2017-03-13"},{"Attack": "2017-06-23"},{"Attack": "2017-06-27"},{"Attack": "2017-08-07"},{"Attack": "2017-11-17"},{"Attack": "2018-01-27"},{"Attack": "2018-03-19"},{"Attack": "2018-03-22"},{"Attack": "2018-03-24"},{"Attack": "2018-06-14"},{"Attack": "2018-07-14"},{"Attack": "2018-08-26"},{"Attack": "2018-10-11"},{"Attack": "2018-11-01"},{"Attack": "2018-12-10"},{"Attack": "2018-12-29"} 
    
   
    for j in range(0,len(attack_date)):
        for i in range(0,len(date_list)):
            if(attack_date[j]['Attack']==date_list[i]):
                selected_date.append(date_list[i-3:i+4])
                
    attack_date = []
    
    for i in range(1, len(selected_date)):
        attack_date.append(selected_date[i])
    
    
    return attack_date



for i in range(0, 10):
    draw_y(attack_date[i])
for i in range(10, 20):
    draw_y(attack_date[i])
for i in range(20, 30):
    draw_y(attack_date[i])
for i in range(30, 40):
    draw_y(attack_date[i])
for i in range(40, 50):
    draw_y(attack_date[i])
for i in range(50, len(attack_date)):
    draw_y(attack_date[i])



def draw_y(day):
    
    n = int(day[0].split('-')[0])
    
    if day[0].split('-')[0] != day[-1].split('-')[0]:
    
        with open('/Users/junha_lee/Desktop/ScrapyResult/Filtered_B_100/'+str(n)+'.json') as json_file: data1 = json.load(json_file)     
        with open('/Users/junha_lee/Desktop/ScrapyResult/Filtered_B_100/'+str(n+1)+'.json') as json_file: data2 = json.load(json_file)   
        
       
        date=[]
        
        for i in range(0, len(data1)):
            date.append(data1[i]['datetime'][0:10])
        for i in range(0,len(data2)):
            date.append(data2[i]['datetime'][0:10]) 
    else:
        
        with open('/Users/junha_lee/Desktop/ScrapyResult/Filtered_B_100/'+str(n)+'.json') as json_file: data1 = json.load(json_file)     
        date=[]
        
        for i in range(0, len(data1)):
            date.append(data1[i]['datetime'][0:10])
            
    
    date_count = {}
    
    for d in date:
        if d in date_count.keys():
            date_count[d] += 1
        else:
            date_count[d] = 1
        
    g_date = date_count.keys()    
    g_freq = date_count.values()
    g_avg = []

    
    max_freq = max(g_freq)
    min_freq = min(g_freq)
    
            
    n_freq = []        
            
    for i in range(0, len(g_freq)):
        n_freq.append(float(g_freq[i]-min_freq)/float(max_freq-min_freq))
        
            
    year_average = float(sum(n_freq))/float(len(n_freq))
    
    
    
    a_date = []
    a_freq=[]
    a_avg = []
    
    
    for i in range(0, len(day)):
        if day[i] in g_date:
            for j in range(0, len(g_date)):
                if day[i] == g_date[j]:
                    a_date.append(g_date[j])
                    a_freq.append(n_freq[j])
        else:
            a_date.append(day[i])
            a_freq.append(0)
    
    attack_average = float(sum(a_freq))/float(len(a_freq))
    
    ba_avg = []
    
    avg = 0
    for i in range(0, 3):
        avg += a_freq[i]
    
    for i in range(0, 3):
        ba_avg.append(avg/3)
    
    ba_avg.append(a_freq[3])
    
    avg = 0
    for i in range(4,7):
        avg += a_freq[i]
    for i in range(4,7):
        ba_avg.append(avg/3)
        
    
   
    for i in range(0, len(a_date)):
        g_avg.append(year_average)
        a_avg.append(attack_average)


    fig = plt.figure()
    fig.set_size_inches(20.5, 5.5)
    plt.plot(a_date,a_freq,color='black',marker='o',linestyle='solid')
    plt.plot(a_date,a_avg,color='red',marker='o',linestyle='solid')
    plt.plot(a_date,g_avg,color='green',marker='o',linestyle='solid')
#    plt.plot(a_date,ba_avg,color='blue',marker='o',linestyle='solid')

    
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/1000/"+n+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/X_100/"+n+".pdf")
    fig.savefig("/Users/junha_lee/Desktop/Graph/Betweenness/filter/313/"+str(day[3])+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/Closeness_100/"+n+".pdf")
    