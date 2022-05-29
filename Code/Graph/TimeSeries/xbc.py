

import datetime
import json
import tweepy           # To consume Twitter's API
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook


startdate = datetime.date(2012,3,1)
enddate = datetime.date(2019,4,3)
    
date_list = []    
while startdate<=enddate:
    date_list.append(str(startdate))
    startdate = startdate + datetime.timedelta(days=1)

CONSUMER_KEY = "4oqZjge7qM0n3WNftJiKHFtOF" #API key
CONSUMER_SECRET = "CZOzvRcdwFOzPZFoM5igXVGBbOBp7lQWBBtCRe76wuv738equP" 
ACCESS_TOKEN = "1004411169568747520-7NBYDlDKlGXX9q5gjXasgRRo5p3HtT" 
ACCESS_TOKEN_SECRET = "b3BSPhEfHGYCxuIaNPg1CFcJtKkCWnjIZESooDgT99GWL" 
#
#CONSUMER_KEY = "LMb6DIm8jWSPZh3QZfjUqeXZE" 
#CONSUMER_SECRET = "nIGcBLqqC5vMspxbJbiyvWYMY6Nu6ItY2tDvrp5jyoRzHg4J6P" 
#ACCESS_TOKEN = "1098046038554767360-M0IL17I6bb1Hzho3gvMRKegOAFEY62" 
#ACCESS_TOKEN_SECRET = "fkIjWg8VcMLaKo2O6wvA6BkK7f3scGy9mXPZlFabbtEjV" 



# Authentication and access using keys:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=10)

def get_selected_date():

    selected_date = [[]]
    with open('/Users/junha_lee/desktop/normal.json','r') as atkfile:
        attack_date = json.load(atkfile)
        print(attack_date)
    
    for j in range(0,len(attack_date)):
        for i in range(0,len(date_list)):
            if(attack_date[j]['Normal']==date_list[i]):
                selected_date.append(date_list[i-7:i+8])
    
    return selected_date


def get_score():
    
    userids_x = []
    score_x = []
    userids_b = []
    score_b = []    
    userids_c = []
    score_c = []    
    
    score_data_x = pd.read_excel('/Users/boyoung/Documents/PredictCyberAttacks/Graph/FrequencyGraph/code/recordedfuture_score.xls')
    score_data_b = pd.read_excel('/Users/boyoung/Documents/PredictCyberAttacks/Graph/FrequencyGraph/code/betweenness_score.xls')
    score_data_c = pd.read_excel('/Users/boyoung/Documents/PredictCyberAttacks/Graph/FrequencyGraph/code/closeness_score.xls')
    
    
    for i in range(0, len(score_data_x)):
        userids_x.append(str(score_data_x['userid'][i]))
        score_x.append(int(score_data_x['score'][i]))
    
    for i in range(0, len(score_data_b)):
        userids_b.append(str(score_data_b['userid'][i]))
        score_b.append(int(score_data_b['score'][i])) 
    
    for i in range(0, len(score_data_c)):
        userids_c.append(str(score_data_c['userid'][i]))
        score_c.append(int(score_data_c['score'][i])) 
        
    
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






attack_date = []

for i in range(1, len(selected_date)):
    attack_date.append(selected_date[i])


def not_weighted():      
    
    before_count_list = []
    attack_count_list = []
    after_count_list = []

    for i in range(0, len(attack_date)):
        

        year_b = int(attack_date[i][7].split('-')[0])-1
        year = attack_date[i][7].split('-')[0]
        year_a = int(attack_date[i][7].split('-')[0])+1
        
        before = []
        after = []
        attack = []
        
        for j in range(0, len(attack_date[i])):
            if (j<7):
                before.append(attack_date[i][j])
            elif j==7:
                attack.append(attack_date[i][j])
            else:
                after.append(attack_date[i][j])
                
        
        before_count = 0
        after_count = 0
        attack_count = 0
        
        
        with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Filtered_C_100/'+str(year_b)+'.json') as test_file:
            before_json = json.load(test_file)
        with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Filtered_C_100/'+str(year)+'.json') as test_file:
            attack_json = json.load(test_file)            
        with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Filtered_C_100/'+str(year_a)+'.json') as test_file:
            after_json = json.load(test_file)            
         
        for n in range(0, len(before_json)):
            if before_json[n]['datetime'][0:10] in before:
                before_count += 1
                
        for n in range(0, len(after_json)):
            if after_json[n]['datetime'][0:10] in after:
                after_count += 1
        
        for n in range(0, len(attack_json)):
            if attack_json[n]['datetime'][0:10] in before:
                before_count += 1
            elif attack_json[n]['datetime'][0:10] in attack:
                attack_count += 1
            elif attack_json[n]['datetime'][0:10] in after:
                after_count += 1
        
        
        before_count_list.append(before_count)
        attack_count_list.append(attack_count)
        after_count_list.append(after_count)
        
        '''
    for i in range(0, len(attack_date)):
        print((before_count_list[i]-min(before_count_list))/(max(before_count_list)-min(before_count_list)))
            
    for i in range(0, len(attack_date)):
        print((attack_count_list[i]-min(attack_count_list))/(max(attack_count_list)-min(attack_count_list)))
        
    for i in range(0, len(attack_date)):
        print((after_count_list[i]-min(after_count_list))/(max(after_count_list)-min(after_count_list)))        
        '''
        
    for i in range(0, len(attack_date)):
        print(before_count_list[i]/7)
        
    for i in range(0, len(attack_date)):
        print(attack_count_list[i]/1)        
        
    for i in range(0, len(attack_date)):
        print(after_count_list[i]/7)        
        
        

def weighted():      
    
    # score 받아오기
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
    
    
    before_count_list_x = []
    attack_count_list_x = []
    after_count_list_x = []
    
    before_count_list_b = []
    attack_count_list_b = []
    after_count_list_b= []
    
    before_count_list_c = []
    attack_count_list_c = []
    after_count_list_c = []
    
    for i in range(0, len(attack_date)):
        
        print(i)
        
        # 연도
        year_b = int(attack_date[i][7].split('-')[0])-1
        year = attack_date[i][7].split('-')[0]
        year_a = int(attack_date[i][7].split('-')[0])+1
        
        before = []
        after = []
        attack = []
        
        # 날짜 구분하기
        for j in range(0, len(attack_date[i])):
            if (j<7):
                before.append(attack_date[i][j])
            elif j==7:
                attack.append(attack_date[i][j])
            else:
                after.append(attack_date[i][j])
        
        before_count_x = 0
        after_count_x = 0
        attack_count_x = 0
        
        before_count_b = 0
        after_count_b= 0
        attack_count_b = 0
        
        before_count_c = 0
        after_count_c = 0
        attack_count_c = 0
        
        # 트윗 파일 가져오기
        with open('/Users/junha_lee/desktop/scrapyresult/X_100/'+str(year_b)+'.json') as test_file:
            before_json_x = json.load(test_file)
        with open('/Users/junha_lee/desktop/scrapyresult/X_100/'+str(year)+'.json') as test_file:
            attack_json_x = json.load(test_file)            
        with open('/Users/junha_lee/desktop/scrapyresult/X_100/'+str(year_a)+'.json') as test_file:
            after_json_x = json.load(test_file)    

        with open('/Users/junha_lee/desktop/scrapyresult/Betweenness_100/'+str(year_b)+'.json') as test_file:
            before_json_b = json.load(test_file)
        with open('/Users/junha_lee/desktop/scrapyresult/Betweenness_100/'+str(year)+'.json') as test_file:
            attack_json_b = json.load(test_file)            
        with open('/Users/junha_lee/desktop/scrapyresult/Betweenness_100/'+str(year_a)+'.json') as test_file:
            after_json_b = json.load(test_file)    

        with open('/Users/junha_lee/desktop/scrapyresult/Closeness_100/'+str(year_b)+'.json') as test_file:
            before_json_c = json.load(test_file)
        with open('/Users/junha_lee/desktop/scrapyresult/Closeness_100/'+str(year)+'.json') as test_file:
            attack_json_c = json.load(test_file)            
        with open('/Users/junha_lee/desktop/scrapyresult/Closeness_100/'+str(year_a)+'.json') as test_file:
            after_json_c = json.load(test_file)    

            
            
        users_x = []
        users_b = []
        users_c = []
        
        # 트윗 파일에서 username 받아오기
        for n in range(0, len(before_json_x)):
            users_x.append(before_json_x[n]['usernameTweet'])
        for n in range(0, len(attack_json_x)):
            users_x.append(attack_json_x[n]['usernameTweet'])
        for n in range(0, len(after_json_x)):
            users_x.append(after_json_x[n]['usernameTweet'])
            
        for n in range(0, len(before_json_b)):
            users_b.append(before_json_b[n]['usernameTweet'])
        for n in range(0, len(attack_json_b)):
            users_b.append(attack_json_b[n]['usernameTweet'])
        for n in range(0, len(after_json_b)):
            users_b.append(after_json_b[n]['usernameTweet'])
            
        for n in range(0, len(before_json_c)):
            users_c.append(before_json_c[n]['usernameTweet'])
        for n in range(0, len(attack_json_c)):
            users_c.append(attack_json_c[n]['usernameTweet'])
        for n in range(0, len(after_json_c)):
            users_c.append(after_json_c[n]['usernameTweet'])
            
        users_x = list(set(users_x))
        users_b = list(set(users_b))
        users_c = list(set(users_c))

            
        userid_x = []
        userid_b = []
        userid_c = []

        # username을 userid로 바꾸기
        for n in range(0, len(users_x)):
            try:
                userid_x.append(api.get_user(users_x[n]).id)
            except:
                userid_x.append(1)
        
        for n in range(0, len(users_b)):
            try:
                userid_b.append(api.get_user(users_b[n]).id)
            except:
                userid_b.append(1)        
        
        for n in range(0, len(users_c)):
            try:
                userid_c.append(api.get_user(users_c[n]).id)
            except:
                userid_c.append(1)        
        
        
        userid_score_x = []
        userid_score_b = []
        userid_score_c = []
        
        
        # userid에 맞는 userscore 넣기
        for n in range(0, len(userid_x)):
            try:
                userid_score_x.append(score_x[userids_x.index(userid_x[n])])
            except :
                userid_score_x.append(1)
       
        for n in range(0, len(userid_b)):
            try:
                userid_score_b.append(score_b[userids_b.index(userid_b[n])])
            except :
                userid_score_b.append(1)                
                
        for n in range(0, len(userid_c)):
            try:
                userid_score_c.append(score_c[userids_c.index(userid_c[n])])
            except :
                userid_score_c.append(1)                
                
                
                
        # weight 부여한 count 
        for n in range(0, len(before_json_x)):
            if before_json_x[n]['datetime'][0:10] in before:
                before_count_x += score_x[users_x.index(before_json_x[n]['usernameTweet'])]
                
        for n in range(0, len(after_json_x)):
            if after_json_x[n]['datetime'][0:10] in after:
                after_count_x += score_x[users_x.index(after_json_x[n]['usernameTweet'])]
        

        for n in range(0, len(attack_json_x)):
            if attack_json_x[n]['datetime'][0:10] in before:
                before_count_x += score_x[users_x.index(attack_json_x[n]['usernameTweet'])]
              
            elif attack_json_x[n]['datetime'][0:10] in attack:
                attack_count_x += score_x[users_x.index(attack_json_x[n]['usernameTweet'])]
                
            elif attack_json_x[n]['datetime'][0:10] in after:
                after_count_x += score_x[users_x.index(attack_json_x[n]['usernameTweet'])]
                
                
        before_count_list_x.append(before_count_x)
        attack_count_list_x.append(attack_count_x)
        after_count_list_x.append(after_count_x)
        
        
        for n in range(0, len(before_json_b)):
            if before_json_b[n]['datetime'][0:10] in before:
                before_count_b += score_b[users_b.index(before_json_b[n]['usernameTweet'])]
                
        for n in range(0, len(after_json_b)):
            if after_json_b[n]['datetime'][0:10] in after:
                after_count_b += score_b[users_b.index(after_json_b[n]['usernameTweet'])]
        
        for n in range(0, len(attack_json_b)):
            if attack_json_b[n]['datetime'][0:10] in before:
                before_count_b += score_b[users_b.index(attack_json_b[n]['usernameTweet'])]
              
            elif attack_json_b[n]['datetime'][0:10] in attack:
                attack_count_b += score_b[users_b.index(attack_json_b[n]['usernameTweet'])]
                
            elif attack_json_b[n]['datetime'][0:10] in after:
                after_count_b += score_b[users_b.index(attack_json_b[n]['usernameTweet'])]
                
                
        before_count_list_b.append(before_count_b)
        attack_count_list_b.append(attack_count_b)
        after_count_list_b.append(after_count_b)        
        
        for n in range(0, len(before_json_c)):
            if before_json_c[n]['datetime'][0:10] in before:
                before_count_c += score_c[users_c.index(before_json_c[n]['usernameTweet'])]
                
        for n in range(0, len(after_json_c)):
            if after_json_c[n]['datetime'][0:10] in after:
                after_count_c += score_c[users_c.index(after_json_c[n]['usernameTweet'])]
        
        for n in range(0, len(attack_json_c)):
            if attack_json_c[n]['datetime'][0:10] in before:
                before_count_c += score_c[users_c.index(attack_json_c[n]['usernameTweet'])]
              
            elif attack_json_c[n]['datetime'][0:10] in attack:
                attack_count_c += score_c[users_c.index(attack_json_c[n]['usernameTweet'])]
                
            elif attack_json_c[n]['datetime'][0:10] in after:
                after_count_c += score_c[users_c.index(attack_json_c[n]['usernameTweet'])]
                
                
        before_count_list_c.append(before_count_c)
        attack_count_list_c.append(attack_count_c)
        after_count_list_c.append(after_count_c)        
        


    # x raw data
    for i in range(0, len(attack_date)):
        print(float(before_count_list_x[i])/7)
        
    for i in range(0, len(attack_date)):
        print(float(attack_count_list_x[i])/1)        
        
    for i in range(0, len(attack_date)):
        print(float(after_count_list_x[i])/7)      
    
        # b raw data
    for i in range(0, len(attack_date)):
        print(float(before_count_list_b[i])/7)
        
    for i in range(0, len(attack_date)):
        print(float(attack_count_list_b[i])/1)        
        
    for i in range(0, len(attack_date)):
        print(float(after_count_list_b[i])/7)        
        
        
        
    # c raw data
    for i in range(0, len(attack_date)):
        print(float(before_count_list_c[i])/7)
        
    for i in range(0, len(attack_date)):
        print(float(attack_count_list_c[i])/1)        
        
    for i in range(0, len(attack_date)):
        print(float(after_count_list_c[i])/7)        
        

'''





    # x normalization
    for i in range(0, len(attack_date)):
        print((before_count_list_x[i]-min(before_count_list_x))/(max(before_count_list_x)-min(before_count_list_x)))
            
    for i in range(0, len(attack_date)):
        print((attack_count_list_x[i]-min(attack_count_list_x))/(max(attack_count_list_x)-min(attack_count_list_x)))
        
    for i in range(0, len(attack_date)):
        print((after_count_list_x[i]-min(after_count_list_x))/(max(after_count_list_x)-min(after_count_list_x)))        
        

    
    
        
        
        
    # b normalization
    for i in range(0, len(attack_date)):
        print((before_count_list_b[i]-min(before_count_list_b))/(max(before_count_list_b)-min(before_count_list_b)))
            
    for i in range(0, len(attack_date)):
        print((attack_count_list_b[i]-min(attack_count_list_b))/(max(attack_count_list_b)-min(attack_count_list_b)))
        
    for i in range(0, len(attack_date)):
        print((after_count_list_b[i]-min(after_count_list_b))/(max(after_count_list_b)-min(after_count_list_b)))        
        

        
        
        
        
        
    # c normalization
    for i in range(0, len(attack_date)):
        print((before_count_list_c[i]-min(before_count_list_c))/(max(before_count_list_c)-min(before_count_list_c)))
            
    for i in range(0, len(attack_date)):
        print((attack_count_list_c[i]-min(attack_count_list_c))/(max(attack_count_list_c)-min(attack_count_list_c)))
        
    for i in range(0, len(attack_date)):
        print((after_count_list_c[i]-min(after_count_list_c))/(max(after_count_list_c)-min(after_count_list_c)))        

        '''
    