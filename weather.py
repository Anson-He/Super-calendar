
#----------主体框架-------------
import tkinter as tk
window = tk.Tk()
window.title('天气')
window.geometry('1000x500')# 设定窗口的大小(长 * 宽)
label = tk.Label(window,text='请输入需要查询天气的城市，如：佛山')
label.pack()
input_text = tk.Text(window,width=50,height=2)
input_text.pack()
#-------------------------------
#---------打开网页-----------
def open_url():
    n = input_text.get('0.0', 'end')
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
    html = driver.page_source
    #print(html)
    driver.close()
    return html
#--------------------------------
botton_morning = tk.Button(window,text='白天',width=10,height=2)#,command=morning(a))
botton_morning.place(x=350,y=60)
botton_night = tk.Button(window,text='夜晚',width=10,height=2)#,command=night(a))
botton_night.place(x=550,y=60)
botton_sure = tk.Button(window,text='确定',width=3,height=1,command=open_url)
botton_sure.place(x=700,y=25)
main = tk.Text(window,width=120,height=25)
main.place(x=80,y=120)
window.mainloop()