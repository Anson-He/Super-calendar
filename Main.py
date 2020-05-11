import tkinter as tk
from music import *
window = tk.Tk()
window.title('超级万年历')#给窗口的可视化起名字
window.geometry('1000x500')# 设定窗口的大小(长 * 宽)
calendar = tk.Text(window)#日历窗口
calendar.place(x=10, y=50, width=500, height=300)
current_time = tk.Text(window)#时间窗口
current_time.place(x=625,y=20,width=300, height=50)
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