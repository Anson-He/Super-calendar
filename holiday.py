def get_holiday():
    import requests
    from bs4 import BeautifulSoup
    import tkinter.font as tf
    url = 'http://www.gov.cn/zhengce/content/2019-11/21/content_5454164.htm'
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    rqq = requests.get(url,headers=head)
    soup = BeautifulSoup(rqq.content,'lxml')
    a = soup.find_all('p')
    import tkinter as tk
    window = tk.Tk()
    window.title('节假日')
    window.geometry('500x500')
    ft = tf.Font(family='宋体',size = 13)
    main = tk.Text(window,width = 70,height = 37)
    main.pack()
    main.tag_add('tag_ym',0.0)
    main.tag_config('tag_ym',font = ft)
    main.insert(tk.END,'2020年'+a[1].text+':\n'+'\n','tag_ym')
    for i in range(6,13):
        main.insert(tk.END,a[i].text+'\n'+'\n','tag_ym')