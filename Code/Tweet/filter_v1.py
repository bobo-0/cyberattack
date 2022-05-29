import json 
import pandas as pd



def keyword_filter(n):
    

    
    #get original keyword list
    with open('/Users/junha_lee/Desktop/keyword.json') as json_file: 
            data = json.load(json_file) 
    print('keyword open'+str(n))
    
    #remove one length key word and assign index
    leng = len(data)-1
    for i in range(0,leng):
        #print(i)
        #print(data[i]['keyword'])
        #print('this is iteration '+str(i))
        if(len(data[i]['keyword'])==1):
            data.pop(i)
            #print(len(data))
            leng = leng-1
            #print(leng)
        #print('this is out of if' +str(leng) +'and '+str(i))
        
        if(i==leng):
            break
   
    #split the key phrase to a word
    for i in range(0,len(data)):
        data[i]['keyword'] = data[i]['keyword'].split()

        
    #open tweets
#    with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/X_100/'+str(n)+'.json') as test_file: 
#    with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Betweenness_100/'+str(n)+'.json') as test_file: 
#    with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Closeness_100/'+str(n)+'.json') as test_file: 
    with open('/Users/junha_lee/Desktop/scrapyresult/1000/1000_user.json') as test_file:   

        test = json.load(test_file)    

    #split the text to a word
    for i in range(0,len(test)):
        test[i]['text'] = test[i]['text'].split()
    
    #check the key words is contain in text
    result = []
    for i in range(0,len(test)):
        for j in range(0,len(data)):
            check = all(item in test[i]['text'] for item in data[j]['keyword'])
            if check:
                result.append(test[i])

                    
    #Save tweets with True
#    with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Filtered_X_100/'+str(n)+'.json','w') as makefile :
#    with open('/Users/boyoung/Documents/PredictCyberAttacks/Crawling/Tweets/Filtered_B_100/'+str(n)+'.json','w') as makefile :
    with open('/Users/junha_lee/Desktop/scrapyresult/1000/1000_user_filtered.json','w') as makefile:   
        json.dump(result,makefile)


    print('filtered tweets saved')
    
if __name__ == '__main__':
    for i in range(2008,2020):
        keyword_filter(str(i))
        print(i)
              