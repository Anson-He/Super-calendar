def get_calculate():
    import tkinter as tk
    window = tk.Tk()
    window.geometry('500x200')
    window.title('计算器')
    input1 = tk.Text(window,width = 50,height = 3)
    input1.place(x=70,y=10)
    result1 = tk.Text(window,width = 50,height = 7)
    result1.place(x=70,y=70)


    #-------计算-------------
    def calculate():
        n = input1.get(0.0,tk.END)
        def factorial(m):
            if m <=1:
                return 1
            else:
                return (m * factorial(m-1))
        if '!' in n:
            r = []
            import re
            x = re.findall('([0-9]{1,})!',n)
            for i in x:
                r.append(factorial(int(i)))
            for i in range(0,len(r)):
                n = n.replace(str(x[i]),str(r[i]))
            n = n.replace('!','')
            r = []
        if 'sin' in n:
            r = []
            import re
            x = re.findall('sin([0-9]{1,})',n)
            import math
            for i in x:
                r.append(math.sin(int(i)))
            for i in range(0,len(r)):
                n = n.replace(str(x[i]),str(r[i]))
            n = n.replace('sin','')
            r = []
        if 'cos' in n:
            r = []
            import re
            x = re.findall('cos([0-9]{1,})',n)
            import math
            for i in x:
                r.append(math.sin(int(i)))
            for i in range(0,len(r)):
                n = n.replace(str(x[i]),str(r[i]))
            n = n.replace('cos','')
            r = []
        if 'tan' in n:
            r = []
            import re
            x = re.findall('tan([0-9]{1,})',n)
            import math
            for i in x:
                r.append(math.sin(int(i)))
            for i in range(0,len(r)):
                n = n.replace(str(x[i]),str(r[i]))
            n = n.replace('tan','')
            r = []
        if 'log' in n:
            r = []
            import re
            x = re.findall('log\(([0-9]{1,})\)([0-9]{1,})',n)
            import math
            for i in x:
                r.append(math.log(int(i[1]),int(i[0])))
            for i in range(0,len(r)):
                n = n.replace('('+str(x[i][0])+')'+str(x[i][1]),str(r[i]))
            n = n.replace('log','')
            r = []
        a = eval(n)
        #result=tk.Label(window,text=a,font=20,foreground='red')
        #result.place(x=230,y=70)
        result1.delete(0.0,tk.END)
        result1.insert(tk.END,a)
    #--------------------------------




    result = tk.Button(window,text='确定',width=5,height=1,command=calculate)
    result.place(x=430,y=15)