import json 
import datetime as datetime
import tweepy           # To consume Twitter's API
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

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
     

    
    
def weighted_draw_y(n):

    userids = []
    score = []
    
#    score_data = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/recordedfuture_score.xls')
#    score_data = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/betweenness_score.xls')
    score_data = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/closeness_score.xls')


    for i in range(0, len(score_data)):
        userids.append(str(score_data['userid'][i]))
        score.append(int(score_data['score'][i]))


#    with open('/Users/junha_lee/Desktop/Scrapyresult/1000/'+n+'.json') as json_file: 
#    with open('/Users/junha_lee/Desktop/Scrapyresult/X_100/'+n+'.json') as json_file: 
#    with open('/Users/junha_lee/Desktop/Scrapyresult/Betweenness_100/'+str(n)+'.json') as json_file: 
    with open('/Users/junha_lee/Desktop/Scrapyresult/Closeness_100/'+str(n)+'.json') as json_file: 
        
        data = json.load(json_file) 

    username = []
    
    for i in range(0, len(data)):
        username.append(str(data[i]['usernameTweet']))
    
    usernames = list(set(username))
    

    
    usernames_score = []
    
    for i in range(0, len(usernames)):
        try:
            usernames_score.append(score[userids.index(str(api.get_user(usernames[i]).id))])
        except:
            usernames_score.append(1)
            
    
    date = []
    frequency = []
                
    for i in range(0,len(data)):
        
        date.append(data[i]['datetime'][0:10])
        
        user = str(data[i]['usernameTweet'])
        user_score = usernames_score[usernames.index(user)]
        

        if i==0 or date[i] != date[i-1]:
            frequency.append(user_score)
        elif date[i] == date[i-1]:
            frequency.append(frequency[i-1]+user_score)
    
    g_date = []
    g_freq = []
    g_avg = []
            
    for i in range(0,len(date)):
        if i==0 :  
            g_freq.append(frequency[0])
            g_date.append(date[0][5:10])
        else:
            if (i == (len(date)-1)):
                g_freq.append(frequency[i])
                g_date.append(date[i][5:10])
            else:            
                if(date[i] != date[i+1]):
                    g_freq.append(frequency[i])
                    g_date.append(date[i][5:10])            

    avg = float(sum(g_freq))/float(len(g_freq))
    

    
    for i in range(0, len(g_date)):
        g_avg.append(avg)


    fig = plt.figure()
    fig.set_size_inches(200.5, 10.5)
    plt.plot(g_date,g_freq,color='black',marker='o',linestyle='solid')
    plt.plot(g_date,g_avg,color='red',marker='o',linestyle='solid')
    
    
    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/weighted_1000/weighted_"+n+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/weighted_100/weighted_"+n+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/weighted_b_100/weighted_"+n+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/weighted_c_100/weighted_"+n+".pdf")
    
  
    
    
def draw_y(n):
    
    n = str(2017)
        
#    with open('/Users/junha_lee/Desktop/Scrapyresult/1000/'+n+'.json') as json_file: 
    with open('/Users/junha_lee/Desktop/tweets/random/year/'+n+'.json') as json_file: 
        data = json.load(json_file) 

    date = []
    frequency = []
                
    for i in range(0,len(data)):
        date.append(data[i]['datetime'][0:10])

        if i==0 or date[i] != date[i-1]:
            frequency.append(1)
        elif date[i] == date[i-1]:
            frequency.append(frequency[i-1]+1)
            
    
    g_date = []
    g_freq = []
    g_avg = []
            
    for i in range(1,len(date)):
        if(frequency[i] == 1) : 
            g_freq.append(frequency[i-1])
            g_date.append(date[i-1][5:10])
            
    avg = float(sum(g_freq))/float(len(g_freq))
    
    
   
    for i in range(0, len(g_date)):
        g_avg.append(avg)

    fig = plt.figure()
    fig.set_size_inches(200.5, 10.5)
    plt.plot(g_date,g_freq,color='black',marker='o',linestyle='solid')
    plt.plot(g_date,g_avg,color='red',linestyle='solid')
    
    
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/1000/"+n+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/X_100/"+n+".pdf")
    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/Betweenness_100/"+n+".pdf")
#    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/Closeness_100/"+n+".pdf")
    
    
    
    
    
    
    
    
    
def weighted_draw_y_all(n):

    userids_x = []
    score_x = []
    userids_b = []
    score_b = []
    userids_c = []
    score_c = []
    
    score_data_x = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/recordedfuture_score.xls')
    score_data_b = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/betweenness_score.xls')
    score_data_c = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/closeness_score.xls')


    for i in range(0, len(score_data_x)):
        userids_x.append(str(score_data_x['userid'][i]))
        score_x.append(int(score_data_x['score'][i]))
        
    for i in range(0, len(score_data_b)):
        userids_b.append(str(score_data_b['userid'][i]))
        score_b.append(int(score_data_b['score'][i]))
        
    for i in range(0, len(score_data_c)):
        userids_c.append(str(score_data_c['userid'][i]))
        score_c.append(int(score_data_c['score'][i]))

    with open('/Users/junha_lee/Desktop/Scrapyresult/X_100/'+n+'.json') as json_file: 
        data_x = json.load(json_file) 
    with open('/Users/junha_lee/Desktop/Scrapyresult/Betweenness_100/'+str(n)+'.json') as json_file: 
        data_b = json.load(json_file) 
    with open('/Users/junha_lee/Desktop/Scrapyresult/Closeness_100/'+str(n)+'.json') as json_file: 
        data_c = json.load(json_file) 

    username_x = []
    username_b = []
    username_c = []
    
    for i in range(0, len(data_x)):
        username_x.append(str(data_x[i]['usernameTweet']))
    for i in range(0, len(data_b)):
        username_b.append(str(data_b[i]['usernameTweet']))    
    for i in range(0, len(data_c)):
        username_c.append(str(data_c[i]['usernameTweet']))    
    
    usernames_x = list(set(username_x))
    usernames_b = list(set(username_b))
    usernames_c = list(set(username_c))
    
    usernames_score_x = []
    usernames_score_b = []
    usernames_score_c = []

    for i in range(0, len(usernames_x)):
        try:
            usernames_score_x.append(score_x[userids_x.index(str(api.get_user(usernames_x[i]).id))])
        except:
            usernames_score_x.append(1)
    for i in range(0, len(usernames_b)):
        try:
            usernames_score_b.append(score_b[userids_b.index(str(api.get_user(usernames_b[i]).id))])
        except:
            usernames_score_b.append(1)    
    for i in range(0, len(usernames_c)):
        try:
            usernames_score_c.append(score_c[userids_c.index(str(api.get_user(usernames_c[i]).id))])
        except:
            usernames_score_c.append(1)    
    

    
    date_x = []
    frequency_x = []
    date_b = []
    frequency_b = []
    date_c = []
    frequency_c = []
    
    # X
    for i in range(0,len(data_x)):
        date_x.append(data_x[i]['datetime'][0:10])
        user = str(data_x[i]['usernameTweet'])
        user_score = usernames_score_x[usernames_x.index(user)]
        if i==0 or date_x[i] != date_x[i-1]:
            frequency_x.append(user_score)
        elif date_x[i] == date_x[i-1]:
            frequency_x.append(frequency_x[i-1]+user_score)
    g_date_x = []
    g_freq_x = []
    g_avg_x = []
    for i in range(0,len(date_x)):
        if i==0 :  
            g_freq_x.append(frequency_x[0])
            g_date_x.append(date_x[0][5:10])
        else:
            if (i == (len(date_x)-1)):
                g_freq_x.append(frequency_x[i])
                g_date_x.append(date_x[i][5:10])
            else:            
                if(date_x[i] != date_x[i+1]):
                    g_freq_x.append(frequency_x[i])
                    g_date_x.append(date_x[i][5:10])            
    avg_x = float(sum(g_freq_x))/float(len(g_freq_x))
    for i in range(0, len(g_date_x)):
        g_avg_x.append(avg_x)



    # B
    for i in range(0,len(data_b)):
        date_b.append(data_b[i]['datetime'][0:10])
        user = str(data_b[i]['usernameTweet'])
        user_score = usernames_score_b[usernames_b.index(user)]
        if i==0 or date_b[i] != date_b[i-1]:
            frequency_b.append(user_score)
        elif date_b[i] == date_b[i-1]:
            frequency_b.append(frequency_b[i-1]+user_score)
    g_date_b = []
    g_freq_b = []
    g_avg_b = []
    for i in range(0,len(date_b)):
        if i==0 :  
            g_freq_b.append(frequency_b[0])
            g_date_b.append(date_b[0][5:10])
        else:
            if (i == (len(date_b)-1)):
                g_freq_b.append(frequency_b[i])
                g_date_b.append(date_b[i][5:10])
            else:            
                if(date_b[i] != date_b[i+1]):
                    g_freq_b.append(frequency_b[i])
                    g_date_b.append(date_b[i][5:10])            
    avg_b = float(sum(g_freq_b))/float(len(g_freq_b))
    for i in range(0, len(g_date_b)):
        g_avg_b.append(avg_b)
        
    # C
    for i in range(0,len(data_c)):
        date_c.append(data_c[i]['datetime'][0:10])
        user = str(data_c[i]['usernameTweet'])
        user_score = usernames_score_c[usernames_c.index(user)]
        if i==0 or date_c[i] != date_c[i-1]:
            frequency_c.append(user_score)
        elif date_c[i] == date_c[i-1]:
            frequency_c.append(frequency_c[i-1]+user_score)
    g_date_c = []
    g_freq_c = []
    g_avg_c = []
    for i in range(0,len(date_c)):
        if i==0 :  
            g_freq_c.append(frequency_c[0])
            g_date_c.append(date_c[0][5:10])
        else:
            if (i == (len(date_c)-1)):
                g_freq_c.append(frequency_c[i])
                g_date_c.append(date_c[i][5:10])
            else:            
                if(date_c[i] != date_c[i+1]):
                    g_freq_c.append(frequency_c[i])
                    g_date_c.append(date_c[i][5:10])            
    avg_c = float(sum(g_freq_c))/float(len(g_freq_c))
    for i in range(0, len(g_date_c)):
        g_avg_c.append(avg_c)




    fig = plt.figure()
    fig.set_size_inches(200.5, 10.5)
    
    plt.plot(g_date_x,g_freq_x,color='black',marker='o',linestyle='solid')
    plt.plot(g_date_x,g_avg_x,color='black',marker='o',linestyle='solid')
    plt.plot(g_date_b,g_freq_b,color='red',marker='o',linestyle='solid')
    plt.plot(g_date_b,g_avg_b,color='red',marker='o',linestyle='solid')
    plt.plot(g_date_c,g_freq_c,color='blue',marker='o',linestyle='solid')
    plt.plot(g_date_c,g_avg_c,color='blue',marker='o',linestyle='solid')

    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/weighted_xbc/weighted_"+n+".pdf")
    






    
def draw_y_all(n):
        
#    with open('/Users/junha_lee/Desktop/Scrapyresult/1000/'+n+'.json') as json_file: 
    with open('/Users/junha_lee/Desktop/Scrapyresult/X_100/'+n+'.json') as json_file: 
        data_x = json.load(json_file) 
    with open('/Users/junha_lee/Desktop/Scrapyresult/Betweenness_100/'+n+'.json') as json_file: 
        data_b = json.load(json_file) 
    with open('/Users/junha_lee/Desktop/Scrapyresult/Closeness_100/'+n+'.json') as json_file: 
        data_c = json.load(json_file) 



    date_x = []
    frequency_x = []
    date_b = []
    frequency_b = []
    date_c = []
    frequency_c = []
    
    # X
    for i in range(0,len(data_x)):
        date_x.append(data_x[i]['datetime'][0:10])
        if i==0 or date_x[i] != date_x[i-1]:
            frequency_x.append(1)
        elif date_x[i] == date_x[i-1]:
            frequency_x.append(frequency_x[i-1]+1)
    g_date_x = []
    g_freq_x = []
    g_avg_x = []
    for i in range(1,len(date_x)):
        if(frequency_x[i] == 1) : 
            g_freq_x.append(frequency_x[i-1])
            g_date_x.append(date_x[i-1][5:10])
    avg_x = float(sum(g_freq_x))/float(len(g_freq_x))
    for i in range(0, len(g_date_x)):
        g_avg_x.append(avg_x)
    
    # B    
    for i in range(0,len(data_b)):
        date_b.append(data_b[i]['datetime'][0:10])
        if i==0 or date_b[i] != date_b[i-1]:
            frequency_b.append(1)
        elif date_b[i] == date_b[i-1]:
            frequency_b.append(frequency_b[i-1]+1)
    g_date_b = []
    g_freq_b = []
    g_avg_b = []
    for i in range(1,len(date_b)):
        if(frequency_b[i] == 1) : 
            g_freq_b.append(frequency_b[i-1])
            g_date_b.append(date_b[i-1][5:10])
    avg_b = float(sum(g_freq_b))/float(len(g_freq_b))
    for i in range(0, len(g_date_b)):
        g_avg_b.append(avg_b) 
        
    # C
    for i in range(0,len(data_c)):
        date_c.append(data_c[i]['datetime'][0:10])
        if i==0 or date_c[i] != date_c[i-1]:
            frequency_c.append(1)
        elif date_c[i] == date_c[i-1]:
            frequency_c.append(frequency_c[i-1]+1)
    g_date_c = []
    g_freq_c = []
    g_avg_c = []
    for i in range(1,len(date_c)):
        if(frequency_c[i] == 1) : 
            g_freq_c.append(frequency_c[i-1])
            g_date_c.append(date_c[i-1][5:10])
    avg_c = float(sum(g_freq_c))/float(len(g_freq_c))
    for i in range(0, len(g_date_c)):
        g_avg_c.append(avg_c)

        
    fig = plt.figure()
    fig.set_size_inches(200.5, 10.5)
    
    
    
    
    plt.plot(g_date_x,g_freq_x,color='black',marker='o',linestyle='solid')
    plt.plot(g_date_x,g_avg_x,color='black',marker='o',linestyle='solid')
    plt.plot(g_date_b,g_freq_b,color='red',marker='o',linestyle='solid')
    plt.plot(g_date_b,g_avg_b,color='red',marker='o',linestyle='solid')
    plt.plot(g_date_c,g_freq_c,color='blue',marker='o',linestyle='solid')
    plt.plot(g_date_c,g_avg_c,color='blue',marker='o',linestyle='solid')
    
    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/xbc/"+n+".pdf")
    
    
    
    
    
    
    
    

    
def norm(n):

    userids_x = []
    score_x = []
    userids_b = []
    score_b = []    
    userids_c = []
    score_c = []    
    
    ######### 점수표
    score_data_x = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/recordedfuture_score.xls')
    score_data_b = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/betweenness_score.xls')
    score_data_c = pd.read_excel('/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/closeness_score.xls')

    for i in range(0, len(score_data_x)):
        userids_x.append(str(score_data_x['userid'][i]))
        score_x.append(int(score_data_x['score'][i]))
        
    for i in range(0, len(score_data_b)):
        userids_b.append(str(score_data_b['userid'][i]))
        score_b.append(int(score_data_b['score'][i])) 
        
    for i in range(0, len(score_data_c)):
        userids_c.append(str(score_data_c['userid'][i]))
        score_c.append(int(score_data_c['score'][i]))        

    ######### 트윗 저장 디렉토리
    with open('/Users/junha_lee/Desktop/Scrapyresult/X_100/'+str(n)+'.json') as json_file: 
        data_x = json.load(json_file) 
    with open('/Users/junha_lee/Desktop/Scrapyresult/Betweenness_100/'+str(n)+'.json') as json_file: 
        data_b = json.load(json_file)         
    with open('/Users/junha_lee/Desktop/Scrapyresult/Closeness_100/'+str(n)+'.json') as json_file: 
        data_c = json.load(json_file)         

    username_x = []
    username_b = []
    username_c = []

    for i in range(0, len(data_x)):
        username_x.append(str(data_x[i]['usernameTweet']))
    for i in range(0, len(data_b)):
        username_b.append(str(data_b[i]['usernameTweet']))        
    for i in range(0, len(data_c)):
        username_c.append(str(data_c[i]['usernameTweet']))        
        
    usernames_x = list(set(username_x))
    usernames_b = list(set(username_b))
    usernames_c = list(set(username_c))

    usernames_score_x = []
    usernames_score_b = []
    usernames_score_c = []

    for i in range(0, len(usernames_x)):
        try:
            usernames_score_x.append(score_x[userids_x.index(str(api.get_user(usernames_x[i]).id))])
        except:
            usernames_score_x.append(1)
            
    for i in range(0, len(usernames_b)):
        try:
            usernames_score_b.append(score_b[userids_b.index(str(api.get_user(usernames_b[i]).id))])
        except:
            usernames_score_b.append(1)            
            
    for i in range(0, len(usernames_c)):
        try:
            usernames_score_c.append(score_c[userids_c.index(str(api.get_user(usernames_c[i]).id))])
        except:
            usernames_score_c.append(1)            
            
    date_x = []
    frequency_x = []
    frequency_w_x = []
    date_b = []
    frequency_b = []
    frequency_w_b = []
    date_c = []
    frequency_c = []
    frequency_w_c = []
                
    for i in range(0,len(data_x)):
        
        date_x.append(data_x[i]['datetime'][0:10])
        user = str(data_x[i]['usernameTweet'])
        user_score = usernames_score_x[usernames_x.index(user)]
        
        if i==0 or date_x[i] != date_x[i-1]:
            frequency_x.append(1)
            frequency_w_x.append(user_score)
        elif date_x[i] == date_x[i-1]:
            frequency_x.append(frequency_x[i-1]+1)
            frequency_w_x.append(frequency_w_x[i-1]+user_score)
        
    for i in range(0,len(data_b)):
        
        date_b.append(data_b[i]['datetime'][0:10])
        user = str(data_b[i]['usernameTweet'])
        user_score = usernames_score_b[usernames_b.index(user)]
        
        if i==0 or date_b[i] != date_b[i-1]:
            frequency_b.append(1)
            frequency_w_b.append(user_score)
        elif date_b[i] == date_b[i-1]:
            frequency_b.append(frequency_b[i-1]+1)
            frequency_w_b.append(frequency_w_b[i-1]+user_score)
            
    for i in range(0,len(data_c)):
        
        date_c.append(data_c[i]['datetime'][0:10])
        user = str(data_c[i]['usernameTweet'])
        user_score = usernames_score_c[usernames_c.index(user)]
        
        if i==0 or date_c[i] != date_c[i-1]:
            frequency_c.append(1)
            frequency_w_c.append(user_score)
        elif date_c[i] == date_c[i-1]:
            frequency_c.append(frequency_c[i-1]+1)
            frequency_w_c.append(frequency_w_c[i-1]+user_score)
        
    g_date_x = []
    g_freq_x = []
    g_avg_x = []
    
    g_freq_w_x = []
    g_avg_w_x = []
    
    g_date_b = []
    g_freq_b = []
    g_avg_b = []
    
    g_freq_w_b = []
    g_avg_w_b = []    
    
    g_date_c = []
    g_freq_c = []
    g_avg_c = []
    
    g_freq_w_c = []
    g_avg_w_c = []    
        
    for i in range(0,len(date_x)):

        if (i == (len(date_x)-1)):
            g_freq_x.append(frequency_x[i])
            g_date_x.append(date_x[i][5:10])
            g_freq_w_x.append(frequency_w_x[i])
        else:            
            if(date_x[i] != date_x[i+1]):
                g_freq_x.append(frequency_x[i])
                g_date_x.append(date_x[i][5:10])            
                g_freq_w_x.append(frequency_w_x[i])
                
    for i in range(0,len(date_b)):
   
        if (i == (len(date_b)-1)):
            g_freq_b.append(frequency_b[i])
            g_date_b.append(date_b[i][5:10])
            g_freq_w_b.append(frequency_w_b[i])
        else:            
            if(date_b[i] != date_b[i+1]):
                g_freq_b.append(frequency_b[i])
                g_date_b.append(date_b[i][5:10])            
                g_freq_w_b.append(frequency_w_b[i])                     
                    
    for i in range(0,len(date_c)):
       
        if (i == (len(date_c)-1)):
            g_freq_c.append(frequency_c[i])
            g_date_c.append(date_c[i][5:10])
            g_freq_w_c.append(frequency_w_c[i])
        else:            
            if(date_c[i] != date_c[i+1]):
                g_freq_c.append(frequency_c[i])
                g_date_c.append(date_c[i][5:10])            
                g_freq_w_c.append(frequency_w_c[i])                    
        
    g_freq_n_x = []
    g_freq_w_n_x = []
    g_freq_n_b = []
    g_freq_w_n_b = []
    g_freq_n_c = []
    g_freq_w_n_c = []
    
    for i in range(0, len(g_freq_x)):
        g_freq_n_x.append((float(g_freq_x[i])-float(min(g_freq_x)))/(float(max(g_freq_x))-float(min(g_freq_x))))
        g_freq_w_n_x.append((float(g_freq_w_x[i])-float(min(g_freq_w_x)))/(float(max(g_freq_w_x))-float(min(g_freq_w_x))))   
        
    for i in range(0, len(g_freq_b)):
        g_freq_n_b.append((float(g_freq_b[i])-float(min(g_freq_b)))/(float(max(g_freq_b))-float(min(g_freq_b))))
        g_freq_w_n_b.append((float(g_freq_w_b[i])-float(min(g_freq_w_b)))/(float(max(g_freq_w_b))-float(min(g_freq_w_b))))         
        
    for i in range(0, len(g_freq_c)):
        g_freq_n_c.append((float(g_freq_c[i])-float(min(g_freq_c)))/(float(max(g_freq_c))-float(min(g_freq_c))))
        g_freq_w_n_c.append((float(g_freq_w_c[i])-float(min(g_freq_w_c)))/(float(max(g_freq_w_c))-float(min(g_freq_w_c)))) 

    avg_x = float(sum(g_freq_n_x))/float(len(g_freq_n_x))
    avg_w_x = float(sum(g_freq_w_n_x))/float(len(g_freq_w_n_x))

    for i in range(0, len(g_date_x)):
        g_avg_x.append(avg_x)
        g_avg_w_x.append(avg_w_x)
        
    avg_b = float(sum(g_freq_n_b))/float(len(g_freq_n_b))
    avg_w_b = float(sum(g_freq_w_n_b))/float(len(g_freq_w_n_b))

    for i in range(0, len(g_date_b)):
        g_avg_b.append(avg_b)
        g_avg_w_b.append(avg_w_b)

    avg_c = float(sum(g_freq_n_c))/float(len(g_freq_n_c))
    avg_w_c = float(sum(g_freq_w_n_c))/float(len(g_freq_w_n_c))

    for i in range(0, len(g_date_c)):
        g_avg_c.append(avg_c)
        g_avg_w_c.append(avg_w_c)

        
    fig = plt.figure()
    fig.set_size_inches(200.5, 10.5)
    

    plt.plot(g_date_x,g_freq_n_x,color='black',marker='o',linestyle='solid')
    plt.plot(g_date_x,g_avg_x,color='black',linestyle='solid')        
    plt.plot(g_date_x,g_freq_w_n_x,color='black',marker='o',linestyle=':')
    plt.plot(g_date_x,g_avg_w_x,color='black',linestyle=':')          
          
    plt.plot(g_date_b,g_freq_n_b,color='blue',marker='o',linestyle='solid')
    plt.plot(g_date_b,g_avg_b,color='blue',linestyle='solid')        
    plt.plot(g_date_b,g_freq_w_n_b,color='blue',marker='o',linestyle=':')
    plt.plot(g_date_b,g_avg_w_b,color='blue',linestyle=':')         
        
    plt.plot(g_date_c,g_freq_n_c,color='red',marker='o',linestyle='solid')
    plt.plot(g_date_c,g_avg_c,color='red',linestyle='solid')        
    plt.plot(g_date_c,g_freq_w_n_c,color='red',marker='o',linestyle=':')
    plt.plot(g_date_c,g_avg_w_c,color='red',linestyle=':')     
    
    ######### 그래프 저장 디렉토리
    fig.savefig("/Users/junha_lee/Documents/Junha/Study/Projects/PredictCyberAttacks/Graph/FrequencyGraph/norm/"+n+".pdf")    
    
    
if __name__ == '__main__':
    
    for i in range(2012,2020):
        norm(str(i))
        print str(i)+' is ended'

