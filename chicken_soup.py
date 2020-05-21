import requests
from bs4 import BeautifulSoup
import random

def get_chicken_soup():
    url = 'http://www.yuluju.com/lizhimingyan/10580.html'
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    strhtml = requests.get(url,headers=head)  

    #print(strhtml.text)
    soup=BeautifulSoup(strhtml.content,'lxml')
    data=soup.find_all('span')
    content=[]
    for i in data:
        #print(i.text) 
        content.append(i.text)
        #print(content)
    item= random.choice(content)
    return item
     

print(get_chicken_soup())   

    
      
     



