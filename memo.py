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
import sys
import pickle
import time
import os
from color_me import ColorMe

init = ["系统提示：此信息为初始化信息，默认会有一条数据, 请忽略........"]
# 定义备忘录用户的名称
class Memo(object):
    def __init__(self, name, thing, date, time):
        self.name = name
        self.thing = thing
        self.date = date
        self.time = time
        self.__id = 0

    @property
    def id(self):
        return self.__id

    def set_id(self, restart):
        self.__id = restart + self.__id
        return self.__id

    def welcome(self):
        print(f"Welcome to the memo.".center(60, "-"))


# 记录事件与时间
class MemoAdmin(object):
    """"""

    def __init__(self):
        self.user_list = []     #用来储存备忘录的列表

    def user_add(self):         #定义新建一个备忘录的函数
        count = True
        while (count):
            Your_title = input("请您输入备忘录标题：".strip())
            Your_event = input("请您输入备忘录事件：".strip())
            Your_date = input("请您输入备忘录用时时间：".strip())
            time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            if Your_title == "":
                print("标题不能为空！！！")

            elif Your_event == "":
                print("备忘录事件不能为空")

            elif Your_date == "":
                print("备忘录用时不能为空")

            else:
                self.create(Your_title, Your_event, Your_date, time1)
                count = False

    def create(self, Your_title, Your_event, Your_date, time1):     #定义查找显示出来的信息的函数
        memo = Memo(Your_title, Your_event, Your_date, time1)
        user_result = (
            f"ID：{memo.set_id(self.count())}、标题：{Your_title}、事件：{Your_event}、用时时间：{Your_date}、创建时间 : {time1}")

        self.user_list.append(user_result)
        self.save()

    def user_delete(self):              #定义删除备忘录的数据的函数
        if os.path.isfile("db.pkl"):
            user_delete = int(input("请您输入您需要删除的id号：".strip()))
            with open('db.pkl', 'rb') as f:
                data = pickle.load(f)
                data.pop(user_delete)
                self.user_list = []
            for a in data:
                self.user_list.append(a)

            self.save()
        else:
            print("nonono")

    def user_search(self):          #定义查找备忘录数据的函数
        search_result = int(input("请您输入您需要查找的ID：".strip()))
        if os.path.isfile("db.pkl"):
            with open('db.pkl', 'rb') as f:
                data = pickle.load(f)
                print(data[search_result])
        else:
            search_result = ColorMe("没有备忘录信息，请您选择添加备忘录并创建").red()
            print(search_result)

    def save(self):             #查看当前有多少条备忘录数据
        with open('db.pkl', 'wb') as f:
            pickle.dump(self.user_list, f)
            save_result = ColorMe(f"您当前一共有{len(self.user_list)}条备忘录信息").green()
            print(save_result)

    def load(self):
        if os.path.isfile("db.pkl"):
            with open('db.pkl', 'rb') as f:
                data = pickle.load(f)
            load_welcome = ColorMe("备忘录信息，数据如下：".center(60, "-")).green()
            print(load_welcome)
            for line in data:
                print(line)
        else:
            load_warning = ColorMe("没有备忘录文件，请你添加并创建").red()
            print(load_warning)

    def count(self):
        with open('db.pkl', 'rb') as f:
            data = pickle.load(f)
            result = len(data)
            return result

    def exit(self):             #退出备忘录
        save_Tips = ColorMe("欢迎你再次使用，再见......".center(60, "-")).green()
        print(save_Tips)
        sys.exit()

    def delete(self):               #清除整个备忘录
        if os.path.isfile("db.pkl"):
            os.remove("db.pkl")
            delete_success = ColorMe("恭喜您，清除备忘录成功！！！").green()
            print(delete_success)
        else:
            delete_warning = ColorMe("没有备忘录文件，请你添加并创建").red()
            print(delete_warning)

    def user_input(self):               #根据选项进行创建、删除、查找备忘录等操作
        print(f"Welcome to the  memo .".center(60, "-"))
        user_menu = {
            "1": "添加备忘录数据",
            "2": "删除备忘录数据",
            "3": "查找备忘录数据",
            "p": "查看备忘录数据",
            "d": "清空备忘录数据",
            "Q": "退出备忘录数据"
        }

        user_menu2 = {
            "1": "user_add",
            "2": "user_delete",
            "3": "user_search",
            "p": "load",
            "d": "delete",
            "Q": "exit"
        }

        if os.path.isfile("db.pkl"):
            with open('db.pkl', 'rb') as f:
                data = pickle.load(f)
                for a in data:
                    self.user_list.append(a)
                Os_Tips_result = ColorMe(f"系统提示，初始备忘录信息成功,目前一共有{len(self.user_list)}条数据").green()
                print(Os_Tips_result)

        else:
            with open('db.pkl', 'wb') as f:
                C = ColorMe("系统提示：备忘录程序初始化完毕，请再次打开.....").green()
                print(C)
                pickle.dump(init, f)
                sys.exit()

        try:
            while True:
                for k, v in user_menu.items():
                    print(f"""
                    {k}、{v}
                    """)
                User_choice = input("请您输入选项：".strip())
                if User_choice.strip() == "":
                    error_warning = ColorMe("请您输入正确的数值！！！").red()
                    print(error_warning)
                else:
                    if hasattr(self, user_menu2.get(User_choice)):
                        func = getattr(self, user_menu2.get(User_choice))
                        func()
                    else:
                        error_warning2 = ColorMe("系统检测错误，请您输入正确的选项").red()
                        print(error_warning2)
        except Exception as f:
            print(f)


if __name__ == "__main__":
    Admin = MemoAdmin()
    Admin.user_input()