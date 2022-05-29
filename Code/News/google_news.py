import re
import requests
from bs4 import BeautifulSoup
import json
import collections
from multiprocessing import Pool
from itertools import product

#기사 내용 받아오기


def google():
    
    keyword = input()
    
    i = 0
    
    while i<= 10:
        
        res = requests.get('https://www.google.com/search?q='+keyword+'&tbm=nws&start='+str(i)+'&dpr=2')
        
        soup = BeautifulSoup(res.content,'html.parser')
                
        titles = soup.select('h3 > a')
        subs = soup.select('.slp > span')               
                
        for sub in subs:
            print(sub.text)
            
        i = i + 10
        
        
        
import requests
import driver

driver.get("https://twitter.com/login")
url = "https://twitter.com/login"


element = driver.find_element_by_id("session[username_or_email]")  




payload = { 'session[username_or_email]': 'dlwnsgk2012@gmail.com', 'session[password]': 'dlwnsgk94!'}
r = requests.post(url, data=payload)

r = requests.post("https://www.naver.com/")
        
res = requests.get('https://twitter.com/Bo1210Cap/following')
res = requests.get('https://www.naver.com/')

soup = BeautifulSoup(res.content,'html.parser')
        
followings = soup.find_all('span',{'class' : 'u-linkComplex-target'})

followings = soup.select('b')

followings

for following in followings:
    print(following.text)
  


def twitter():

if __name__ == '__main__':
	google()

	