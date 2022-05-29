import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing
import json
import time


# Twitter App access keys for @user
#CONSUMER_KEY = "LMb6DIm8jWSPZh3QZfjUqeXZE" 
#CONSUMER_SECRET = "nIGcBLqqC5vMspxbJbiyvWYMY6Nu6ItY2tDvrp5jyoRzHg4J6P" 
#ACCESS_TOKEN = "1098046038554767360-M0IL17I6bb1Hzho3gvMRKegOAFEY62" 
#ACCESS_TOKEN_SECRET = "fkIjWg8VcMLaKo2O6wvA6BkK7f3scGy9mXPZlFabbtEjV" 

# Consumer API keys:
CONSUMER_KEY = "4oqZjge7qM0n3WNftJiKHFtOF" #API key
CONSUMER_SECRET = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP" 
ACCESS_TOKEN = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT" 
ACCESS_TOKEN_SECRET = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL" 


# Authentication and access using keys:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)


def test():
    accountlist = pd.read_excel('test.xlsx')
    
    values = accountlist['Twitter accounts'].values
    column = ['Twitter accounts']
    df_selection = accountlist[column]
    usernames=values
    temp = []
    
    
    usernames = userid
    
    temp=[]
    
    for username in usernames:
        data = {
                "username" : username,
                "following" : [],
                "follower" : []}
        
        try :
            data["follower"] = api.followers_ids(user_id = username)
            data["following"] = api.friends_ids(user_id = username)
            
        except :
            data["follower"] = []
            data["following"] = []
            
        temp.append(data)
        print(username)
        
        
    #    with open('hacker/'+username+'.json','w') as towrite:
    with open('/Users/junha_lee/Desktop/sample_followingfollower.json','w') as towrite:
        json.dump(temp,towrite,ensure_ascii=False)
    
        temp=[]
        print(username)
        
        avg = sum(score)/len(score)


def main():
        
    json_data=open('/Users/junha_lee/Desktop/c.json').read()
    
    data = json.loads(json_data)
    
    
    
    
    general_user = []
    
    for i in range(0, len(data)):
        if len(data[i]['user_mentions']) != 0:
            general_user.append(data[i]['user_mentions'][0]['id'])
    
    filter_general = []
    
    for i in range(0,100):
        filter_general.append(general_user[i])
        
    temp=[]
    
    for i in range(0,len(filter_general)):
        data = {
                "username" : filter_general[i],
                "following" : [],
                "follower" : []}
        
        try :
            data["follower"] = api.followers_ids(user_id = filter_general[i])
            data["following"] = api.friends_ids(user_id = filter_general[i])
            
        except :
            data["follower"] = []
            data["following"] = []
            
        temp.append(data)
        print(i)
    
    
    #    with open('hacker/'+username+'.json','w') as towrite:
    with open('/Users/junha_lee/Desktop/sample_followingfollower.json','w') as towrite:
        json.dump(temp,towrite,ensure_ascii=False)
    
            




if __name__ == '__main__':
    main()
    