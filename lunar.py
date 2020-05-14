def get_lunar():
    #---------主窗口-------------
    import tkinter as tk
    window = tk.Tk()
    window.title = '农历'
    window.geometry('500x500')
    #---------------------------

    #---------年月日选择-----------
    import time
    localtime = time.localtime(time.time())#(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
    from tkinter import  ttk
    year1 = ttk.Combobox(window,width=10)
    year1.place(x=15,y=20)
    year_label = tk.Label(window,text='年')
    year_label.place(x=115,y=20)
    month1 = ttk.Combobox(window,width=10)
    month1.place(x=150,y=20)
    month_label = tk.Label(window,text='月')
    month_label.place(x=250,y=20)
    day1 = ttk.Combobox(window,width=10)
    day1.place(x=285,y=20)
    day_label = tk.Label(window,text='日')
    day_label.place(x=385,y=20)
    year_list = []
    for i in range(1991,10000):
        year_list.append(i)
    year1['value'] = year_list
    year1.current(year_list.index(localtime.tm_year))
    month_list = []
    for i in range(1,13):
        month_list.append(i)
    month1['value'] = month_list
    month1.current(month_list.index(localtime.tm_mon))
    day_list = []
    for i in range(1,32):
        day_list.append(i)
    day1['value'] = day_list
    day1.current(day_list.index(localtime.tm_mday))
    #---------------------------

    #----------农历制作---------
    lun = tk.Text(window,padx=120,pady=30)#日历窗口
    lun.place(x=15, y=55, width=470, height=430)
    #-------------------------




    #--------农历详情---------
    import sxtwl
    lunar = sxtwl.Lunar()

    Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    Zhi = ["子", "醜", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    ShX = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
    numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    Week = ["日", "一", "二", "三", "四", "五", "六"]
    jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "驚蟄", "春分", "清明", "穀雨", "立夏", "小滿", "芒種", "夏至", "小暑", "大暑", "立秋", "處暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
    ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
    rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]



    #打印做一箇中間轉換
    def log(*arg):
        import tkinter.font as tf
        s = ""
        for v in arg:
            s += str(v)
        ft = tf.Font(family='宋体',size = 15)
        lun.tag_add('tag_ym',0.0)
        lun.tag_config('tag_ym',font =ft )
        lun.insert(tk.END,s,'tag_ym')

    def printDay(day):
        log("========================================="+'\n')
        log("公曆:", day.y, "年", day.m, "月", day.d, "日"+'\n')
        if day.Lleap:
            log("潤", (day.Lyear0 + 1984), "年", ymc[day.Lmc], "月", rmc[day.Ldi], "日"+'\n')
        else:
            log((day.Lyear0 + 1984), "年", ymc[day.Lmc], "月", rmc[day.Ldi], "日"+'\n')

        if (day.qk >= 0):
            log("當日節氣:" + jqmc[day.jqmc]+'\n')
            log("節氣時間:" + day.jqsj+'\n')

        log("儒略日:JD", sxtwl.J2000 + day.d0,'\n')
        log("星期", Week[day.week],'\n')

        log(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], "年", Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], "月",Gan[day.Lday2.tg], Zhi[day.Lday2.dz], "日",'\n')

        log("距冬至", day.cur_dz, "天",'\n')
        log("距夏至", day.cur_xz, "天",'\n')
        log("距立秋", day.cur_lq, "天",'\n')
        log("距芒種", day.cur_mz, "天",'\n')
        log("距小暑", day.cur_xs, "天",'\n')


    day = lunar.getDayBySolar(int(year1.get()),int(month1.get()),int(day1.get()))
    printDay(day)

    log("========================================="+'\n')
    #獲取一年的信息(干支，生肖，)
    year = lunar.getYearCal(int(year1.get()))
    log("獲取年的干支:" + Gan[year.yearGan] + Zhi[year.yearZhi]+'\n')
    log("獲取年的生肖:" + ShX[year.ShX]+'\n')
    #--------------------------------------------
    #--------按钮刷新--------------------------------------
    def lunar2():
        lun.delete(0.0,tk.END)
        day = lunar.getDayBySolar(int(year1.get()),int(month1.get()),int(day1.get()))
        print(int(year1.get()))
        printDay(day)


        log("========================================="+'\n')
        #獲取一年的信息(干支，生肖，)
        year = lunar.getYearCal(int(year1.get()))
        log("獲取年的干支:" + Gan[year.yearGan] + Zhi[year.yearZhi]+'\n')
        log("獲取年的生肖:" + ShX[year.ShX]+'\n')
    #----------------------------------------------------------
    button_sure = tk.Button(window, text='确定', font=('Arial', 10), width=7, height=1,command = lunar2)
    button_sure.place(x=420,y=15)