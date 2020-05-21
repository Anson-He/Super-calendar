import pandas as pd
data = pd.read_csv('D:\\calendar\\-\\cities_code.txt',header = None,names=['cities','codes'])
l = {}
for i in range(0,len(data)):
    l[data.cities[i]] = data.codes[i]
n = input('请输入城市：')
code = l[n]
import requests
url = 'http://www.weather.com.cn/weather1d/'+str(code)+'.shtml#input'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
aqq = requests.get(url,headers=head)
from bs4 import BeautifulSoup
html=BeautifulSoup(aqq.content,'lxml')
#-------天气状况-------------
a=html.find_all(name='div',attrs={"class":"t"})
time=a[0].find_all('h1')
wea=a[0].find_all('p')
time1=time[0].text
time2=time[1].text
wea1=wea[0].text
tem1=wea[1].text
wind1=wea[2].span['title']+' '+wea[2].text
sun1=wea[3].span.text
time2=time[1].text
wea2=wea[4].text
tem2=wea[5].text
wind2=wea[6].span['title']+':'+wea[6].text
sun2=wea[7].text
def clear(string):
    string = string.replace('\n','')
    return string
s=[time1,wea1,tem1,wind1,sun1,time2,wea2,tem2,wind2,sun2]
s2=[]
for i in s:
    i = clear(str(i))
    s2.append(i)
dic1={'时间':s2[0],'天气':s2[1],'温度':s2[2],'风速':s2[3],'日出/日落时间':s2[4]}
dic2={'时间':s2[5],'天气':s2[6],'温度':s2[7],'风速':s2[8],'日出/日落时间':s2[9]}
#-----------------------

#----------生活指数------------
a=html.find_all(name='div',attrs={"class":"livezs"})
index=a[0].find_all('em')
uv=index[0].text
lw=index[6].text
health=index[7].text
dress=index[8]
wash_car=index[9].text
air=index[10].text
total=a[0].find_all('span')
uv_t=total[0].text
s=0
for i in total[1]:
    if '"star"' in str(i):
        s=s+1
lw_t=s*'⭐'
health_t=total[2].text
dress_t=total[3].text
wash_car_t=total[4].text
air_t=total[5].text
p=a[0].find_all('p')
uv_p=p[0].text
lw_p=p[1].text
health_p=p[2].text
dress_p=p[3].text
wash_p=p[4].text
air_p=p[5].text