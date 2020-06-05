def weather():
    #----------主体框架-------------
    import tkinter as tk
    window = tk.Tk()
    window.title('天气')
    window.geometry('700x650')# 设定窗口的大小(长 * 宽)
    label = tk.Label(window,text='请输入需要查询天气的城市，如：佛山')
    label.pack()
    input_text = tk.Entry(window)
    input_text.pack()
    main = tk.Text(window,width=60,height=40)
    main.place(x=130,y=80)
    #-------------------------------
    #---------打开网页-----------
    def open_url(n):
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
        search_btn.clear()
        search_btn.send_keys(n)
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
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html,'lxml')
        a = soup.find_all('p')
        return a
    #------------------------------------
    #-------------白天----------------
    def morning():
        main.delete(0.0,tk.END)
        import re
        n = input_text.get()
        a = open_url(n)
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
        main.insert(tk.END,'================白天==============='+'\n')
        main.insert(tk.END,'城市:'+n+'\n')
        dic = {'天气':wea,'温度':tem,'体感温度':b_tem,'云量':cloud,
                '飞行延误预报':flight,'观星预报':star,'哮喘预报':asthma,'风向':wind_d,
                '风速':wind_s,'阵风风向':gust_d,'阵风风速':gust_s,'下雨概率':rain_pre,
                '下雪概率':snow_pre,'冻雪概率':w_snow_pre,'雷暴概率':thunderstorms_pre,
                '日出时间':sunrise,'日落时间':sunset,'月出时间':moonrise,'月落时间':moonset}
        for i in dic:
            main.insert(tk.END,i+':'+dic[i]+'\n')
    #--------------------------------
    #--------------夜晚-----------------
    def night():
        main.delete(0.0,tk.END)
        n = input_text.get()
        a = open_url(n)
        import re
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
        main.insert(tk.END,'================夜晚==============='+'\n')
        main.insert(tk.END,'城市:'+n+'\n')
        dic = {'天气':wea,'温度':tem,'体感温度':b_tem,'云量':cloud,
                '飞行延误预报':flight,'观星预报':star,'哮喘预报':asthma,'风向':wind_d,
                '风速':wind_s,'阵风风向':gust_d,'阵风风速':gust_s,'下雨概率':rain_pre,
                '下雪概率':snow_pre,'冻雪概率':w_snow_pre,'雷暴概率':thunderstorms_pre,
                '日出时间':sunrise,'日落时间':sunset,'月出时间':moonrise,'月落时间':moonset}
        for i in dic:
            main.insert(tk.END,i+':'+dic[i]+'\n')
    #--------------------------------------------
    #--------------逐小时汇报-----------------
    def hour_report():
        import tkinter as tk
        window = tk.Tk()
        window.title('天气')
        window.geometry('700x650')# 设定窗口的大小(长 * 宽)
        label = tk.Label(window,text='请输入城市,例如：佛山')
        label.pack()
        input_text = tk.Entry(window)
        input_text.pack()
        label2 = tk.Label(window,text='需要查询多少个小时后的天气，请输入1-72')
        label2.pack()
        input_text2 = tk.Entry(window)
        input_text2.pack()
        main = tk.Text(window,width=60,height=40)
        main.place(x=130,y=100)
        def hr():
            p = int(input_text2.get())
            p = p-1
            n = input_text.get()
            main.delete(0.0,tk.END)
            main.insert(tk.END,'城市:'+n+'\n')
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
            search_btn.send_keys(n)
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
            #p = 0#-------------get text,对p进行传参，用time模块，明天0-23,后天24-27,大后天48-72
            x = a[l1[p]].find_all('p')
            time = x[0].text
            date = a[l1[p]].span.text
            main.insert(tk.END,date+time+'\n')
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
                main.insert(tk.END,i+':'+dic[i]+'\n')
        botton_sure = tk.Button(window,text='确定',width=6,height=2,command = hr)#,command=lambda :open_url(input_text.get()))
        botton_sure.place(x=500,y=13)
        window.mainloop()
    #--------------------------------------------
    botton_morning = tk.Button(window,text='白天',width=15,height=3,command=morning)
    botton_morning.place(x=560,y=150)
    botton_night = tk.Button(window,text='夜晚',width=15,height=3,command=night)
    botton_night.place(x=560,y=300)
    botton_hr = tk.Button(window,text='72小时汇报',width=15,height=3,command = hour_report)#,command=lambda :open_url(input_text.get()))
    botton_hr.place(x=560,y=450)
#