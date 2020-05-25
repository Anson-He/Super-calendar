def else1():
#--------------主体框架---------------
    import tkinter as tk
    window = tk.Tk()
    window.title('其他')
    window.geometry('500x500')

#-----------------------------------------
#-------星座运势----------------------------
    def horoscope_tk():
        from tkinter import ttk
        import tkinter
        import tkinter.font as myFont



        root = tkinter.Tk()
        root.title("星座运势")
        root.geometry("700x550")

        entry_font2 = myFont.Font(size=12, family="华文中宋")

        pull_list_date = ttk.Combobox(root, width=10)
        choice_list=["今日运势", "明日运势"]
        pull_list_date["values"] =choice_list
        pull_list_date.current(0)
        pull_list_date.place(x=250, y=20)

        pull_list_horoscope = ttk.Combobox(root, width=10)
        xingzuo_list=["白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","魔羯座","水瓶座","双鱼座"]
        data={'白羊座':'Aries','金牛座':'Taurus','双子座':'Gemini','巨蟹座':'Cancer','狮子座':'leo','处女座':'Virgo','天秤座':'Libra','天蝎座':'Scorpio','射手座':'Sagittarius','魔羯座':'Capricorn','水瓶座':'Aquarius','双鱼座':'Pisces'}
        pull_list_horoscope["values"] =xingzuo_list
        pull_list_horoscope.current(0)
        pull_list_horoscope.place(x=380, y=20)

        #--------------白羊座---------------
        def get_fate_day_Aries():
            result_text.delete(0.0,tkinter.END)
            import requests
            from bs4 import BeautifulSoup
            n = pull_list_horoscope.get()
            n = data[n]
            m = pull_list_date.get()
            if m =='今日运势':
                m = 'day'
            else:
                m = 'tomorrow'
            url = 'http://astro.sina.com.cn/fate_'+m+'_'+n+'/'
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
            all={horoscope_name:date_time,
                 lucky_day_item:lucky_day_content,
                 love_item:love_content,
                 work_item:work_content,
                 money_item:money_content,
                 health_item:health_content,
                 lucky_number_item:lucky_number_content,
                 lucky_color_item:lucky_color_content,
                 noble_item:noble_content,
                 astronomical_item:astronomical__content,
                 evaluation_item:evaluation_content,
                 detailed_item:detailed_content}
            for i in all:
                result_text.insert(tkinter.END,i+':'+all[i]+'\n')
            #-----------------------------------------------
        sure_button = tkinter.Button(root, text="确定",width=10,command=get_fate_day_Aries)
        sure_button.place(x=500, y=15)


        dram_result_lab = tkinter.Label(root, text="查询结果",width=10)
        dram_result_lab.place(x=300, y=70)

        result_text = tkinter.Text(root, width=53, height=20, font=entry_font2)
        result_text.place(x=80, y=100)
    #---------------------------------------------------------



    button_horoscope = tk.Button(window, text='星座运势', font=('Arial', 12), width=15, height=3,command=horoscope_tk)
    button_horoscope.place(x=70,y=30)

