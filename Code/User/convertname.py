import json
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data


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


accountlist = pd.read_excel('2.xlsx')

values = accountlist['Twitter accounts'].values
column = ['Twitter accounts']
df_selection = accountlist[column]
usernames=values
temp = []


for username in usernames:
    
    #with open('hackers/'+username+'.json','r') as toread:
    #with open('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Follow/list/'+username+'.json','r') as json_file:
    with open('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Follow/hacker/'+username+'.json','r') as json_file:

        data=json.load(json_file);
        
    name = {
                "username" : username,
                "following" : [],
                "follower" : []
            }


    for i in range(0, len(data[0]["follower"])):
        try :
            name["follower"].append( api.get_user(data[0]["follower"][i]).screen_name)
        except tweepy.error.TweepError :    
            print(data[0]["follower"][i])
    
    
    for i in range(0, len(data[0]["following"])):
        try :
            name["following"].append(api.get_user(data[0]["following"][i]).screen_name)
        except tweepy.error.TweepError :    
            print(data[0]["following"][i])
    
    temp.append(name)
    print(username)
        
    #with open('list_name/'+username+'.json','w') as towrite:
    with open('hacker_name/'+username+'.json','w') as towrite:
        json.dump(temp,towrite,ensure_ascii=False)
        
    temp =[]
