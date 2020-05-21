import tkinter as tk
import tkinter.font as tf

import calendar#日历制作
calendar.setfirstweekday(firstweekday=6)


import time

localtime = time.localtime(time.time())#(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)

from music import *
from lunar import *

from weather import weather

window = tk.Tk()
'''#------------设置背景图片--------------
im = Image.open('背景.jpg').resize((1000,500))
b_im = ImageTk.PhotoImage(im)
cv = tk.Canvas(window,width=1000,height=500)
cv.create_image(500,250,image=b_im)
cv.pack()
#-------------------------------------'''

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
for i in range(1991,10000):
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
cal = tk.Text(window,padx=120,pady=30)#日历窗口,,
ft = tf.Font(family='宋体',size = 18)
ft2 = tf.Font(family='宋体',size = 14)
cal.tag_add('tag_ym',0.0)
cal.tag_config('tag_ym',font =ft )
cal.tag_add('tag_yn',0.0)
cal.tag_config('tag_yn',font =ft2 )
cal.insert(tk.END,calendar.month(int(year.get()),int(month.get())),'tag_ym')
cal.insert(tk.END,"\n"+"今天是：%s 年 %s 月 %s 日"%(localtime.tm_year,localtime.tm_mon,localtime.tm_mday),'tag_yn')
def get_year_month():
    cal.delete(0.0,tk.END)
    cal.insert(tk.END,calendar.month(int(year.get()),int(month.get())),'tag_ym')
    cal.insert(tk.END,"\n"+"今天是：%s 年 %s 月 %s 日"%(localtime.tm_year,localtime.tm_mon,localtime.tm_mday),'tag_yn')
button_sure = tk.Button(window, text='确定', font=('Arial', 10), width=7, height=1,command = get_year_month)
button_sure.place(x=380,y=15)

cal.place(x=10, y=50, width=500, height=300)
#--------------------------------------------


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

#--------------每日鸡汤----------------------
from chicken_soup import get_chicken_soup
chicken_soup = tk.Label(window,text = get_chicken_soup(),font=('宋体', 12),wraplength=948,justify='left')
chicken_soup.place(x=20,y=400)
#---------------------------------------




button_weather = tk.Button(window, text='天气', font=('Arial', 12), width=15, height=3,command=weather)
button_weather.place(x=600,y=100)
button_memo = tk.Button(window, text='日程', font=('Arial', 12), width=15, height=3) #command=memo
button_memo.place(x=800,y=100)
button_lunar = tk.Button(window, text='农历', font=('Arial', 12), width=15, height=3,command = get_lunar)
button_lunar.place(x=600,y=200)
button_else = tk.Button(window, text='其他', font=('Arial', 12), width=15, height=3) #command=else
button_else.place(x=800,y=200)
button_music = tk.Button(window, text='▶', font=('Arial', 25), width=5, height=1,command = music)
button_music.place(x=700,y=300)
window.mainloop()