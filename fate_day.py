
#====白羊座 ————今日运势 =======
def get_fate_day_Aries():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Aries/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
   #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all

#====金牛座 ————今日运势 =======
def get_fate_day_Taurus():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Taurus/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all

#====双子座 ————今日运势 =======
    
def get_fate_day_Gemini():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Gemini//'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
  #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all

#====巨蟹座 ————今日运势 =======
    
def get_fate_day_Cancer():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Cancer/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all


#====狮子座 ————今日运势 =======
    
def get_fate_day_leo():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_leo/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all

#====处女座 ————今日运势 =======
    
def get_fate_day_Virgo():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Virgo/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
   #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all

#====天秤座 ————今日运势 =======
    
def get_fate_day_Libra():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Libra/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    
   #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all


#====天蝎座 ————今日运势 =======
    
def get_fate_day_Scorpio():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Scorpio/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #==========================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all
#print(get_fate_day_Scorpio())

#====射手座 ————今日运势 =======
    
def get_fate_day_Sagittarius():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Sagittarius/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #=================================
    
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all
#print(get_fate_day_Sagittarius())


#====摩羯座 ————今日运势 =======
    
def get_fate_day_Capricorn():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Capricorn/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #=============================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all
#print(get_fate_day_Capricorn())
    
#====水瓶座 ————今日运势 =======
    
def get_fate_day_Aquarius():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Aquarius/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
  #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
    
    #=========================================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all
#print(get_fate_day_Aquarius())

#====双鱼座 ————今日运势 =======
    
def get_fate_day_Pisces():
    
    import requests
    from bs4 import BeautifulSoup
    
    url = 'http://astro.sina.com.cn/fate_day_Pisces/'  
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"lxml")
    contents=soup.find_all('td')
    time = soup.find_all('div',class_="time") #日期
    horoscope=soup.find_all('div',class_='tit_d')#星座
    #print(contents)
    
    
    #===题目=============================
    lucky_day_item=contents[0].text#今日幸运值
    love_item=contents[2].text#爱情指数
    work_item=contents[4].text#工作指数
    money_item=contents[6].text#财运指数
    health_item=contents[8].text#健康指数
    lucky_number_item=contents[10].text#幸运数字 
    lucky_color_item=contents[12].text#幸运颜色 
    noble_item=contents[14].text#贵人星座 
    astronomical_item=contents[16].text#今日重要天象
    evaluation_item=contents[18].text#精评
    detailed_item=contents[20].text#详述
    
    #===内容==========
    lucky_day_content=contents[1].text#今日幸运值
    love_content=contents[3].text#爱情指数
    work_content=contents[5].text#工作指数
    money_content=contents[7].text#财运指数
    health_content=contents[9].text#健康指数
    lucky_number_content=contents[11].text#幸运数字 
    lucky_color_content=contents[13].text#幸运颜色 
    noble_content=contents[15].text#贵人星座 
    astronomical__content=contents[17].text#今日重要天象
    evaluation_content=contents[19].text#精评
    detailed_content=contents[21].text#详述
    
    
    #========时间=================
    date_time=time[0].text
    #====星座名称=============
    horoscope_name=horoscope[0].text
   
    
    #==================================
    all=(horoscope_name
         +date_time
         +lucky_day_item+": "+lucky_day_content+'\n'
         +love_item+": "+love_content+'\n'
         +work_item+": "+work_content+'\n'
         +money_item+": "+money_content+'\n'
         +health_item+": "+health_content+'\n'
         +lucky_number_item+": "+lucky_number_content+'\n'
         +lucky_color_item+": "+lucky_color_content+'\n'
         +noble_item+": "+noble_content+'\n'
         +astronomical_item+": "+astronomical__content+'\n'
         +evaluation_item+": "+ evaluation_content+'\n'
         +detailed_item+": "+ detailed_content+'\n')
        
    return all

#print(get_fate_day_Pisces())
