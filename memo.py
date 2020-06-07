def memo():
    '''
    import tkinter
    root = tkinter.Tk()
    root.title("日程")
    root.geometry("500x500")

    entry_font2 = myFont.Font(size=12, family="华文中宋")

    pull_list_date = ttk.Combobox(root, width=10)
    choice_list=["添加备忘录", "删除备忘录","查找备忘录","查看备忘录","清空备忘录","退出备忘录"]
    pull_list_date["values"] =choice_list
    pull_list_date.current(0)
    pull_list_date.place(x=50, y=20)



    sure_button = tkinter.Button(root, text="确定", bg="Orange",width=10)
    sure_button.place(x=290, y=20)


    dram_result_lab = tkinter.Label(root, text="您的备忘录", bg="Orange",width=10)
    dram_result_lab.place(x=170, y=70)

    result_text = tkinter.Text(root, width=53, height=20, font=entry_font2)
    result_text.place(x=12, y=100)

    root.mainloop()
    '''
    #-----------------
    import os
    file = os.getcwd()+'\\memo.txt'
    memo = open(os.getcwd()+'\\memo.txt','a+')#创建备忘录文件
    memo.close()
    import pandas as pd
    import tkinter as tk
    root = tk.Tk()
    root.title("日程")
    root.geometry("400x200")

    import sys
    import pickle
    import time
    import os
    from color_me import ColorMe

    # 定义备忘录用户的名称

    # 记录事件与时间
    user_list = []     #用来储存备忘录的列表

    def user_add():         #定义新建一个备忘录的函数
        import tkinter as tk
        add = tk.Tk()
        add.title('增加事件')
        add.geometry('500x300')
        label1 = tk.Label(add,text = '请您输入备忘录标题：')
        label1.pack()
        input1 = tk.Text(add,width = 50,height = 2)
        input1.pack()
        label2 = tk.Label(add,text = '请您输入提醒时间：')
        label2.pack()
        input2 = tk.Text(add,width = 50,height = 2)
        input2.pack()
        label3 = tk.Label(add,text = '请您输入备忘录事件：')
        label3.pack()
        input3 = tk.Text(add,width = 50,height = 10)
        input3.pack()
        def get1():
            user_list = []
            Your_title = input1.get(0.0,tk.END)
            Your_event = input3.get(0.0,tk.END)
            Your_date = input2.get(0.0,tk.END)
            time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            #memo = Memo(Your_title, Your_event, Your_date, time1)
            if Your_title != '\n' and Your_event != '\n' and Your_date != '\n':
                user_result = {'标题':Your_title,'事件':Your_event,'提醒时间':Your_date,'创建时间':time1}
                user_list.append(user_result)
                memo = open(file,'a+')
                for i in user_list:
                    memo.write(str(i)+'\n')
                memo.close()

                import tkinter
                import tkinter.messagebox
                tkinter.messagebox.showinfo('提示',"创建成功！")
            else:
                import tkinter
                import tkinter.messagebox
                tkinter.messagebox.showinfo('提示',"所填内容不能为空！")
        sure = tk.Button(add,text='确定',command=get1)
        sure.pack()



    def user_delete():             #定义删除备忘录的数据的函数
        import tkinter as tk
        delete = tk.Tk()
        delete.title('删除事件')
        delete.geometry('500x100')
        label1 = tk.Label(delete,text = '请您输入需要删除的备忘录ID：')
        label1.pack()
        input1 = tk.Text(delete,width = 50,height = 2)
        input1.pack()
        def delete1():
            data = pd.read_csv(file,encoding='gbk',header = None)
            data = data.drop(labels=int(input1.get(0.0,tk.END)))
            data = data.reset_index(drop = True)

            import tkinter
            import tkinter.messagebox
            tkinter.messagebox.showinfo('提示',"删除成功！")
            data.to_csv(file,header=None,index=None,encoding='gbk')

        del_Button = tk.Button(delete,text='确定',command=delete1)
        del_Button.pack()

    def load():
        import tkinter.font as tf
        load = tk.Tk()
        load.title('查看事件')
        load.geometry('500x500')
        label1 = tk.Text(load,width = 70,height = 38)
        label1.pack()
        ft = tf.Font(family='宋体',size = 18)
        label1.tag_add('tag_ym',0.0)
        label1.tag_config('tag_ym',font =ft )
        label1.delete(0.0,tk.END)
        import pandas as pd
        data = pd.read_csv(file,encoding='gbk',header = None)
        import re
        for i in range(0,len(data)):
            total = re.findall("(标题)\'(:) \'(.{1,})\\\\n\'\\n1 {1,}\'(事件)\'(:) \'(.{1,})\\\\n\'\\n2 {1,}\'(提醒时间)\'(:) \'(.{1,})\\\\n\'\\n3 {1,}\'(创建时间)\'(:) \'(.{1,})\'",str(data.iloc[i,]))
            label1.insert(tk.END,total[0][0]+total[0][1]+total[0][2]+'\n'+total[0][3]+total[0][4]+total[0][5]+'\n'+total[0][6]+total[0][7]+total[0][8]+'\n'+total[0][9]+total[0][10]+total[0][11]+'\n'+'\n'+'\n')



    def delete():               #清除整个备忘录
        '''if os.path.isfile("db.pkl"):
            os.remove("db.pkl")
            delete_success = ColorMe("恭喜您，清除备忘录成功！！！").green()'''
        import os
        os.remove(file)
        import tkinter
        import tkinter.messagebox
        tkinter.messagebox.showinfo('提示','删除成功！')

    add_Button = tk.Button(root,text = '添加备忘录数据',width = 15,height = 2,command=user_add)
    add_Button.pack()
    del_Button = tk.Button(root,text = '删除备忘录数据',width = 15,height = 2,command=user_delete)
    del_Button.pack()
    check_Button = tk.Button(root,text = '查看备忘录数据',width = 15,height = 2,command = load)
    check_Button.pack()
    clear_Button = tk.Button(root,text = '清空备忘录数据',width = 15,height = 2,command=delete)
    clear_Button.pack()