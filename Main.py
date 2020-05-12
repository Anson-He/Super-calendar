import tkinter as tk
import tkinter.font as tf

import calendar#日历制作
calendar.setfirstweekday(firstweekday=6)

import sxtwl#农历制作

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
cal = tk.Text(window)#日历窗口,,padx=120,pady=60
ft = tf.Font(family='宋体',size = 18)
cal.tag_add('tag_ym',0.0)
cal.tag_config('tag_ym',font =ft )
#cal.insert(tk.END,calendar.month(int(year.get()),int(month.get())),'tag_ym')
cal.insert(tk.END,"%s 年 %s 月"%(year.get(),month.get())+'\n','tag_ym')
cal.insert(tk.END,"周日\t 周一\t 周二\t 周三\t 周四\t 周五\t 周六\t"+ '\n','tag_ym')
def get_year_month():
    cal.delete(0.0,tk.END)
    cal.insert(tk.END,"%s 年 %s 月"%(year.get(),month.get())+'\n','tag_ym')
    cal.insert(tk.END,"周日\t 周一\t 周二\t 周三\t 周四\t 周五\t 周六\t"+ '\n','tag_ym')

def isLeapYear(year1):#判断是否是闰年

    return True if (year1 % 100 != 0 and year1 % 4 == 0) or year1 % 400 ==0 else False



def monthDay(year1,month1):#判断当前月天数

    li = [31,28,31,30,31,30,31,31,30,31,30,31]

    if isLeapYear(year1):

        li[1] = 29

    return li[month1-1]



def totalDay(year1, month1):#距1900年1月1日的天数

    days = 0

    for index_year in range(1900, year1):

        days += 366 if isLeapYear(index_year) else 365

    for index_month in range(1, month1):

        days += monthDay(year1, index_month)

    return days



def show(): #显示当前月

    year1 = year.get()
    month1 = month.get()

    space_num = totalDay(year1, month1) % 7 + 1

    #print("空格数",space_num)

    #print("星期",totalDay(year, month) % 7 + 1,"开始")

    #print("星期日\t一\t二\t三\t四\t五\t六")

    for i in range(1, monthDay(year1,month1) + 1):

        if (i == 1):

            for j in range(space_num % 7):

                print("\t",end="")

        print("\t%2d"%i,end="")

        if (i + space_num) % 7 == 0:

            print()

show()

button_sure = tk.Button(window, text='确定', font=('Arial', 10), width=7, height=1,command = get_year_month)
button_sure.place(x=380,y=15)


'''cal.insert(tk.END,calendar.month(int(year.get()),int(month.get())),'tag_ym')
def get_year_month():
    cal.delete(0.0,tk.END)
    cal.insert(tk.END,calendar.month(int(year.get()),int(month.get())),'tag_ym')
button_sure = tk.Button(window, text='确定', font=('Arial', 10), width=7, height=1,command = get_year_month)
button_sure.place(x=380,y=15)
'''
cal.place(x=10, y=50, width=500, height=300)







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