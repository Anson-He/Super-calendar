def get_zodiac():
    import tkinter as tk
    from tkinter import ttk
    window = tk.Tk()

    import time

    localtime = time.localtime(time.time())#(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)


    window.title('黄历')
    window.geometry('500x500')# 设定窗口的大小(长 * 宽)
    #-----------------日历年月日选择-----------
    year = ttk.Combobox(window,width=10)
    year.place(x=20,y=20)
    year_label = tk.Label(window,text='年')
    year_label.place(x=120,y=20)
    month = ttk.Combobox(window,width=10)
    month.place(x=150,y=20)
    month_label = tk.Label(window,text='月')
    month_label.place(x=250,y=20)
    year_list = [localtime.tm_year,localtime.tm_year+1]
    year['value'] = year_list
    year.current(year_list.index(localtime.tm_year))
    month_list = [localtime.tm_mon-3,localtime.tm_mon-2,localtime.tm_mon-1,localtime.tm_mon,localtime.tm_mon+1,localtime.tm_mon+2,localtime.tm_mon+3,localtime.tm_mon+4,localtime.tm_mon+5,localtime.tm_mon+6,localtime.tm_mon+7]
    for i in range(0,len(month_list)):
        if month_list[i]<1:
            month_list[i] = str(12-int(month_list[i]))
        if month_list[i]>12:
            month_list[i] = str(month_list[i]-12)
    month['value'] = month_list
    month.current(month_list.index(localtime.tm_mon))
    day = ttk.Combobox(window,width=10)
    day.place(x=280,y=20)
    day_label = tk.Label(window,text='日')
    day_label.place(x=380,y=20)
    day_list = []
    for i in range(1,32):
        day_list.append(i)
    day['value']=day_list
    day.current(day_list.index(localtime.tm_mday))

    #-----------------------------------------
    #--------------显示框-------------------
    zod = tk.Text(window, width=68, height=33)
    zod.place(x=10, y=50)

    #----------------黄历-----------------
    def zodiac():

        zod.delete(0.0,tk.END)
        import requests
        from bs4 import BeautifulSoup
        url = 'http://www.laohuangli.net/'+year.get()+'/'+year.get()+'-'+month.get()+'-'+day.get()+'.html'
        rqq = requests.get(url)
        soup = BeautifulSoup(rqq.content,'lxml')
        a = soup.find_all(name='td',attrs='t_4')
        b = soup.find_all(name='td',attrs='t_3')
        y = b[0].text
        n = b[1].text
        do = a[0].text
        undo = a[1].text
        zod.insert(tk.END,'宜:'+'\n'+do+'\n'+'==============='+'\n'+'\n'+'不宜:'+'\n'+undo+'\n'+'==============='+'\n'+'\n'+y+'\n'+'==============='+'\n'+'\n'+n+'\n'+'===============')
    #-----------------------------------




    result = tk.Button(window,text='确定',width=5,height=1,command=zodiac)
    result.place(x=430,y=15)
#