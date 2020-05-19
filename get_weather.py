#----------打开网页---------------------
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
url = 'http://m.weathercn.com/daily-weather-forecast.do?partner=1000001043_hfaw&id=101924&p_source=&p_type=jump&day=3'
driver.get(url)
driver.find_element_by_xpath('/html/body/header/section/section/a[1]').click()
#before = driver.current_window_handle
#print(before)
#print(driver.page_source)
wait = WebDriverWait(driver,10)
search_btn = driver.find_element_by_css_selector('#search')
#search_btn = driver.find_element_by_xpath('//*[@id="search"]')
search_btn.send_keys(input_text.get())
confirm_btn = wait.until(
    EC.element_to_be_clickable(
            (By.CSS_SELECTOR,'#linkcity > li:nth-child(1)')
    )
)
confirm_btn.click()
driver.switch_to.window(driver.window_handles[0])
html = driver.page_source
#print(html)
driver.close()
#----------------------------------------
#------------网页解析--------------
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
a = soup.find_all('p')
b = soup.find_all('a')
def morning(a):
    wea = a[3].text
    tem = a[4].strong.text
    b_tem = a[5].strong.text
    #rain_pre = a[6].text.replace('\n\t\t\t\t\t\t\t\t\t降水概率','')
    cloud = a[7].text.replace('\n\t\t\t\t\t\t\t\t\t云量','')
    flight = a[8].span.text.replace('\n\t\t\t\t\t\t\t\t\t','')
    flight.replace('\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t','')
    star = a[9].span.text.replace('\n\t\t\t\t\t\t\t\t\t','')
    asthma = a[10].span.text.replace('\n\t\t\t\t\t\t\t\t\t','')
    asthma.replace('\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t','')
    wind_d = a[12].span.text
    wind_s = re.findall('.{0,}风速:(.+)',a[12].text)[0]
    gust_d = a[13].span.text
    gust_s = re.findall('.{0,}阵风风速:(.+)',a[13].text)[0]
    rain_pre = a[14].text
    snow_pre = a[15].text
    w_snow_pre = a[16].text
    thunderstorms_pre = a[17].span.text
    sunrise = a[18].strong.text
    sunset = re.findall('.{0,}日落：(.+)',a[18].text)[0]
    moonset = a[19].strong.text
    moonrise = re.findall('.{0,}月落：(.+)',a[19].text)[0]#网页中的月出月落反了
    print('================白天===============')
    print('城市:')
    dic = {'天气':wea,'温度':tem,'体感温度':b_tem,'云量':cloud,
            '飞行延误预报':flight,'观星预报':star,'哮喘预报':asthma,'风向':wind_d,
            '风速':wind_s,'阵风风向':gust_d,'阵风风速':gust_s,'下雨概率':rain_pre,
            '下雪概率':snow_pre,'冻雪概率':w_snow_pre,'雷暴概率':thunderstorms_pre,
            '日出时间':sunrise,'日落时间':sunset,'月出时间':moonrise,'月落时间':moonset}
    for i in dic:
        print(i+':'+dic[i])
    #return wea,tem,b_tem,cloud,flight,star,asthma,wind_d,wind_s,gust_d,gust_s,rain_pre,snow_pre,w_snow_pre,thunderstorms_pre,sunrise,sunset,moonset,moonrise
def night(a):
    wea = a[20].text
    tem = a[21].strong.text
    b_tem = a[22].strong.text
    #rain_pre = a[23].text.replace('\n\t\t\t\t\t\t\t\t\t降水概率','')
    cloud = a[24].text.replace('\n\t\t\t\t\t\t\t\t\t云量','')
    flight = a[25].span.text.replace('\n\t\t\t\t\t\t\t\t\t','')
    flight.replace('\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t','')
    star = a[26].span.text.replace('\n\t\t\t\t\t\t\t\t\t','')
    star.replace('\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t','')
    asthma = a[27].span.text.replace('\n\t\t\t\t\t\t\t\t\t','')
    asthma.replace('\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t','')
    wind_d = a[29].span.text
    wind_s = re.findall('.{0,}风速:(.+)',a[29].text)[0]
    gust_d = a[30].span.text
    gust_s = re.findall('.{0,}阵风风速:(.+)',a[30].text)[0]
    rain_pre = a[31].text
    snow_pre = a[32].text
    w_snow_pre = a[33].text
    thunderstorms_pre = a[34].span.text
    sunrise = a[35].strong.text
    sunset = re.findall('.{0,}日落：(.+)',a[35].text)[0]
    moonset = a[36].strong.text
    moonrise = re.findall('.{0,}月落：(.+)',a[36].text)[0]#网页中的月出月落反了
    print('================夜晚===============')
    print('城市:')
    dic = {'天气':wea,'温度':tem,'体感温度':b_tem,'云量':cloud,
            '飞行延误预报':flight,'观星预报':star,'哮喘预报':asthma,'风向':wind_d,
            '风速':wind_s,'阵风风向':gust_d,'阵风风速':gust_s,'下雨概率':rain_pre,
            '下雪概率':snow_pre,'冻雪概率':w_snow_pre,'雷暴概率':thunderstorms_pre,
            '日出时间':sunrise,'日落时间':sunset,'月出时间':moonrise,'月落时间':moonset}
    for i in dic:
        print(i+':'+dic[i])
    #return wea,tem,b_tem,cloud,flight,star,asthma,wind_d,wind_s,gust_d,gust_s,rain_pre,snow_pre,w_snow_pre,thunderstorms_pre,sunrise,sunset,moonset,moonrise




    #----------------逐小时报告----------------
def hour_report(p):
    from selenium import webdriver
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    driver = webdriver.Chrome()
    url = 'http://m.weathercn.com/daily-weather-forecast.do?partner=1000001043_hfaw&id=101924&p_source=&p_type=jump&day=3'
    driver.get(url)
    driver.find_element_by_xpath('/html/body/header/section/section/a[1]').click()
    #before = driver.current_window_handle
    #print(before)
    #print(driver.page_source)
    wait = WebDriverWait(driver,10)
    search_btn = driver.find_element_by_css_selector('#search')
    #search_btn = driver.find_element_by_xpath('//*[@id="search"]')
    search_btn.send_keys(input_text.get())
    confirm_btn = wait.until(
        EC.element_to_be_clickable(
                (By.CSS_SELECTOR,'#linkcity > li:nth-child(1)')
        )
    )
    confirm_btn.click()
    driver.switch_to.window(driver.window_handles[0])
    #print(html)
    driver.switch_to.frame('other_html')
    driver.find_element_by_xpath('//*[@id="nav_column"]/a[2]').click()
    driver.switch_to.window(driver.window_handles[0])
    html = driver.page_source
    driver.close()
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html,'lxml')
    a = soup.find_all('li')
    #a[0]-a[71]为后三天的每小时温度，a[72]-a[143]为对应具体天气情况
    l1 = []
    l2 = []
    for i in range(0,72):
        l1.append(i)
    for i in range(72,144):
        l2.append(i)
    #p = 0#-------------get text,对p进行传参，用time模块，明天0-23,后台24-27,大后天48-72
    x = a[l1[p]].find_all('p')
    time = x[0].text
    date = a[l1[p]].span.text
    print(date,time)
    tem = x[1].text
    y = a[l2[p]].find_all('span')
    z = a[l2[p]].find_all('p')
    b_tem = z[0].text
    rain_pre = z[1].text
    wind_d = y[2].text
    wind_s = z[2].text
    wet = z[3].text
    gust_s = z[4].text
    dew_point = z[5].text
    can_see = z[6].text
    cloud = z[7].text
    dic = {'温度':tem,'体感温度':b_tem,'云量':cloud,
            '风向':wind_d,'风速':wind_s,y[4].text:gust_s,
            '湿度':wet,'露点':dew_point,'能见度':can_see,'降雨概率':rain_pre}
    for i in dic:
        print(i+':'+dic[i])
#-----------------------------------------------