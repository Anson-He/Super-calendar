import tkinter as tk
import tkinter.font as tf

import time

localtime = time.localtime(time.time())#(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)

from music import *

window = tk.Tk()
window.title('超级万年历')
window.geometry('1000x500')# 设定窗口的大小(长 * 宽)

#-----------------日历年月日选择-----------
year = ttk.Combobox(window,width=10)
year.place(x=65,y=20)
year_label = tk.Label(window,text='年')
year_label.place(x=165,y=20)
month = ttk.Combobox(window,width=10)
month.place(x=245,y=20)
month_label = tk.Label(window,text='月')
month_label.place(x=345,y=20)
year_list = []
for i in range(1991,localtime.tm_year+100):
    year_list.append(i)
year['value'] = year_list
year.current(year_list.index(localtime.tm_year))
month_list = []
for i in range(1,13):
    month_list.append(i)
month['value'] = month_list
month.current(month_list.index(localtime.tm_mon))

#-----------------------------------------


#---------------日历制作----------------------
calendar = tk.Text(window)#日历窗口
ft = tf.Font(family='微软雅黑',size=15)
calendar.tag_add('tag_ym',0.0)
calendar.tag_config('tag_ym',font =ft )
calendar.insert(1.1,"%s年 %s月"%(year.get(),month.get())+'\n','tag_ym')
def get_year_month():
    calendar.delete(1.0,tk.END)
    calendar.insert(1.1,"%s年 %s月"%(year.get(),month.get())+'\n','tag_ym')
    calendar.insert(2.1,"   周日     周一     周二     周三     周四     周五     周六"+'\n','tag_ym')
button_sure = tk.Button(window, text='确定', font=('Arial', 10), width=7, height=1,command = get_year_month)
button_sure.place(x=380,y=15)
calendar.insert(2.1,"   周日     周一     周二     周三     周四     周五     周六"+'\n','tag_ym')
calendar.place(x=10, y=50, width=500, height=300)



#-----------------动态显示时间-----------------
def get_time():
    current_time = time.strftime("%H:%M:%S")
    time1 = ''
    time2 = current_time
    if time2 != time1:
        time1 = time2
        current_time_model = tk.Label(window,text = time1,font = 100)
        current_time_model.config(text = time2)
        current_time_model.place(x=730,y=25)
        current_time_model.after(1000,get_time)#每一千毫秒（即一秒）后执行get_time()
get_time()
#------------------------------------------------





button_weather = tk.Button(window, text='天气', font=('Arial', 12), width=15, height=3) #command=weather
button_weather.place(x=600,y=100)
button_memo = tk.Button(window, text='备忘录', font=('Arial', 12), width=15, height=3) #command=memo
button_memo.place(x=800,y=100)
button_lunar = tk.Button(window, text='农历', font=('Arial', 12), width=15, height=3) #command=lunar
button_lunar.place(x=600,y=200)
button_else = tk.Button(window, text='其他', font=('Arial', 12), width=15, height=3) #command=else
button_else.place(x=800,y=200)
button_music = tk.Button(window, text='▶', font=('Arial', 25), width=5, height=1,command = music)
button_music.place(x=700,y=300)
window.mainloop()