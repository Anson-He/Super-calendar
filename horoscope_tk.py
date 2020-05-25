from tkinter import ttk
import fate_day
import fate_tomorrow



root = tkinter.Tk()
root.title("星座运势")
root.geometry("500x500")

entry_font2 = myFont.Font(size=12, family="华文中宋")

pull_list_date = ttk.Combobox(root, width=10)
choice_list=["今日运势", "明日运势"]
pull_list_date["values"] =choice_list
pull_list_date.current(0)
pull_list_date.place(x=50, y=20)

pull_list_horoscope = ttk.Combobox(root, width=10)
xingzuo_list=["白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","魔羯座","水瓶座","双鱼座"]
pull_list_horoscope["values"] =xingzuo_list
pull_list_horoscope.current(0)
pull_list_horoscope.place(x=170, y=20)


sure_button = tkinter.Button(root, text="确定", bg="Orange",width=10)
sure_button.place(x=290, y=20)


dram_result_lab = tkinter.Label(root, text="查询结果", bg="Orange",width=10)
dram_result_lab.place(x=170, y=70)

result_text = tkinter.Text(root, width=53, height=20, font=entry_font2)
result_text.place(x=12, y=100)

root.mainloop()




