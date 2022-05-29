from py2neo import Graph
import json
import numpy as np
import tweepy           # To consume Twitter's API
import pandas as pd
import shutil
import os



json_data=open('/Users/junha_lee/documents/junha/study/projects/predictcyberattacks/crawling/follow/1000/Relationship_100.json').read()

data = json.loads(json_data)


#between_name = []
#close_name = []
#rf_name = []
#
#all_name =[]

name_score = []

for i in range(0, len(all_name)):
    score = 0
    try :
        bs = 100-between_name.index(all_name[i])
    except:
        bs = 0
    try :
        cs = 100-close_name.index(all_name[i])
    except:
        cs = 0
    try :
        rs = 100-rf_name.index(all_name[i])
    except:
        rs = 0        

    score = bs + cs + rs
    name_score.append(score)
    
    all_name[name_score.index(max(name_score))]
    name_score.remove(max(name_score))
    
    
    
    
sorting_all_name = []

for i in range(0,len(all_name)):
    sorting_all_name.append(all_name[name_score.index(max(name_score))])
    name_score.remove(max(name_score))
        
        
for i in range(0, 10):
    print(sorting_all_name[i])
        


temp = []

for i in range(0, len(userid)):
    for j in range(0, len(data)):
        if str(userid[i]) == str(data[j]["username"]):
            temp.append(data[j])
    

for i in range(0, len(temp)-1):
    if temp[i]["username"] == temp[i+1]["username"]:
        print(i)


#accountlist = pd.read_excel('../list/test.xlsx')
data = pd.read_excel('/Users/junha_lee/Desktop/Betweenness_score.xls')

nodeid = data['nodeId'].values


def setting():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "1"
    
    graph = Graph(uri=uri, user=user, password=password)
    graph.run("CREATE CONSTRAINT ON (n:Hackers) ASSERT n.username IS UNIQUE")
    graph.run("CREATE CONSTRAINT ON (n:NotHackers) ASSERT n.username IS UNIQUE")
    

def nodeid_to_userid():
    
    userid = []
    
    for i in range(0,100):
        userid.append(graph.run("MATCH (s) WHERE ID(s) = "+str(nodeid[i])+" RETURN s.username").data()[0]['s.username'])
        
    return userid
        
def userid_to_screenname(userid):
    
#    CONSUMER_KEY = "LMb6DIm8jWSPZh3QZfjUqeXZE" 
#    CONSUMER_SECRET = "nIGcBLqqC5vMspxbJbiyvWYMY6Nu6ItY2tDvrp5jyoRzHg4J6P" 
#    ACCESS_TOKEN = "1098046038554767360-M0IL17I6bb1Hzho3gvMRKegOAFEY62" 
#    ACCESS_TOKEN_SECRET = "fkIjWg8VcMLaKo2O6wvA6BkK7f3scGy9mXPZlFabbtEjV" 
    
    CONSUMER_KEY = "4oqZjge7qM0n3WNftJiKHFtOF" #API key
    CONSUMER_SECRET = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP" 
    ACCESS_TOKEN = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT" 
    ACCESS_TOKEN_SECRET = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL" 
    
    
    # Authentication and access using keys:
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)
    
    username = []
    
    for i in range(0,len(userid)):
        try:
            username.append(api.get_user(userid[i]).screen_name)
        except:
            print(i)
    
    return username



def find_tweets():
   
    username = screenname
    
    for names in username:
        try:
            shutil.copy('/Users/junha_lee/Desktop/tweets/user/'+names+'.json','/Users/junha_lee/Desktop/tweets/between_100')
        except:
            print(names)
    


if __name__ == '__main__':
    setting()
    userid_to_screenname(nodeid_to_userid())
    

