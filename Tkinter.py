from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import dialog
from tkinter import filedialog
from tkinter import colorchooser
import threadingfs
from collections import OrderedDict
# root = Tk()
# root.title('我是窗口标题')
# w = Label(root, text = "Hello Tkinter")
# w.pack()
# root.mainloop()

# class Application (Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.initWidgets()
#     def initWidgets(self):
#         w = Label(self)
#         bm = PhotoImage(file = 'images/serial.gif')
#         w.x = bm
#         w['image'] = bm
#         w.pack()
#         okBottom = Button(self, text="確定")
#         okBottom['background'] = 'yellow'
#         okBottom.pack()
#
# app = Application()
# print(type(app.master))
# app.master.title('窗戶标题')
# app.mainloop()

# root = Tk()
#
# root.title('Pack 布局')
# for i in range(3):
#     lab = Label(root, text='第%d个Label' % (i + 1), bg='#ffffff')
#     lab.pack()
# root.mainloop()

# class App:
#     def __init__ (self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         fml = Frame(self.master)
#         fml.pack(side=LEFT, fill=BOTH, expand=YES)
#         Button(fml, text='第一个').pack(side=TOP, fill=X, expand=YES)
#         Button(fml, text='第二个').pack(side=TOP, fill=X, expand=YES)
#         Button(fml, text='第三个').pack(side=TOP, fill=X, expand=YES)
#         fm2 = Frame(self.master)
#         fm2.pack(side = LEFT, padx = 10, expand=YES)
#         Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
#         Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
#         Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)
#         fm3 = Frame(self.master)
#         fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
#         Button(fm2, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
#         Button(fm2, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
#         Button(fm2, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)
# root = Tk()
# root.title('Pack')
# display = App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
#         e.pack()
#         p = Frame(self.master)
#         p.pack(side=TOP)
#         names = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "=")
#         for i in range(len(names)):
#             b = Button(p, text=names[i], font=('verdana', 20), width=6)
#             b.grid(row=i // 4, column = i % 4)
#
# root = Tk()
# root.title("Grid布局")
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets (self):
#         boks = ('0疯狂python讲义', '疯狂python讲义', '疯狂python讲义', '疯狂python讲义', '疯狂python讲义', '疯狂python讲义')
#         for i in range(len(boks)):
#             ct = [random.randrange(256) for x in range(3)]
#             grayness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114 * ct[2]))
#             bg_color = '#%02x%02x%02x' % tuple(ct)
#             lb = Label(root, text=boks[i], fg = 'White' if grayness < 125 else 'Black', bg = bg_color)
#             lb.place(x = 20, y = 36 + i * 36, width = 180, height = 30)
#
# root = Tk()
# root.title('Place布局')
# root.geometry("250x250+30+30")
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets (self):
#         self.label = Label(self.master, width = 30)
#         self.label['font'] = ('Courier', 20)
#         self.label['bg'] = 'white'
#         self.label.pack()
#         bn = Button(self.master, text='单击我', command=self.change)
#         bn.pack()
#     def change(self):
#         self.label['text'] = '欢迎学习python'
#         ct = [random.randrange(256) for x in range(3)]
#         grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
#         bg_color = '#%02x%02x%02x' % tuple(ct)
#         self.label['bg'] = bg_color
#         self.label['fg'] = 'black' if grayness > 125 else 'white'
# root = Tk()
# root.title('简单事件处理')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets (self):
#         self.show = Label(self.master, width = 30)
#         self.show['font'] = ('Courier', 20)
#         self.show['bg'] = 'white'
#         self.show.pack()
#         bn = Button(self.master, text='单击我双击我')
#         bn.pack(fill=BOTH, expand=YES)
#         bn.bind('<Button-1>', self.one)
#         bn.bind('<Double-1>', self.double)
#     def one(self, event):
#         self.show['text'] = "左键单击：%s" % event.widget['text']
#     def double(self, event):
#         self.show['text'] = "左键双击，退出程序：%s" % event.widget['text']
#         import sys; sys.exit()
# root = Tk()
# root.title('简单绑定')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets (self):
#         lb = Label(self.master, width=40, height=3)
#         lb.config(bg='lightgreen', font=('Times', 20))
#         lb.bind('<Motion>', self.motion)
#         lb.bind('<B1-Motion>', self.press_motion)
#         lb.pack()
#         self.show = Label(self.master, width = 38, height = 1)
#         self.show.config(bg='white', font=('Courier New', 20))
#         self.show.pack()
#     def motion(self, event):
#         self.show['text'] = "鼠标移动到: (%s %s)" % (event.x, event.y)
#         return
#     def press_motion(self, event):
#         self.show['text'] = "按住鼠标的位置为: (%s %s)" % (event.x, event.y)
#         return
# root = Tk()
# root.title('鼠标事件')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#         self.expr = None
#     def initWidgets(self):
#         # e = Entry(relief=SUNKEN, font=('Courier New', 24), width=25)
#         # e.pack()
#         self.show = Label(relief=SUNKEN, font=('Courier New', 24), width = 25, bg = 'white', anchor=E)
#         self.show.pack()
#         p = Frame(self.master)
#         p.pack(side=TOP)
#         names = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "=")
#         for i in range(len(names)):
#             b = Button(p, text=names[i], font=('verdana', 20), width=6)
#             b.grid(row=i // 4, column = i % 4)
#             b.bind('<Button-1>', self.click)
#             if b['text'] == "=": b.bind('<Double-1>', self.clean)
#     def click (self, event):
#         if (event.widget['text'] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '.')):
#             self.show['text'] = self.show['text'] + event.widget['text']
#             return
#         if (event.widget['text'] in ('+', '-', '*', '/')):
#             if self.expr is None:
#                 self.expr = self.show['text'] + event.widget['text']
#             else:
#                 self.expr = self.expr + self.show['text'] + event.widget['text']
#             self.show['text'] = ''
#             return
#         if (event.widget['text'] == '=' and self.expr is not None):
#             self.expr = self.expr + self.show['text']
#             print(self.expr)
#             self.show['text'] = str(eval(self.expr))
#             self.expr = None
#             return
#     def clean(self, event):
#         self.expr = None
#         self.show['text'] = ''
# root = Tk()
# root.title("Grid布局")
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         # cb = Listbox(self.master, font=24)
#         # for s in ('python', 'swift', 'kotlin'):
#         #     cb.insert(END, s)
#         cb = ttk.Combobox(self.master, font=24)
#         cb['values'] = ('python', 'swift', 'kotlin')
#         cb.pack(side=LEFT, fill=X, expand=YES)
#         # f = Frame(self.master)
#         f = ttk.Frame(self.master)
#         f.pack(side=RIGHT, fill=BOTH, expand=YES)
#         # lab = Label(self.master, text = "我的標簽", font=24)
#         lab = ttk.Label(self.master, text = "我的標簽", font=24)
#         lab.pack(side=TOP, fill=BOTH, expand=YES)
#         # btn = Button(self.master, text='我的按钮')
#         btn = Button(self.master, text='我的按钮')
#         btn.pack()
# root = Tk()
# root.title('简单事件处理')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets (self):
#         self.st = StringVar()
#         ttk.Entry(self.master, textvariable = self.st, width=24, font=('StSONG', 20, 'bold'), foreground='red').pack(fill=BOTH, expand=YES)
#         f = Frame(self.master)
#         f.pack()
#         ttk.Button(f, text='修改', command=self.change).pack(side=LEFT)
#         ttk.Button(f, text='HUOQU ', command=self.get).pack(side=LEFT)
#     def change (self):
#         books = ('1', '2', '3')
#         import random
#         self.st.set(books[random.randint(0, 2)])
#     def get (self):
#         from tkinter import messagebox
#         messagebox.showinfo(title='请输入内容', message=self.st.get())
# root = Tk()
# root.title('variable测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         bm = PhotoImage(file = 'images/serial.gif')
#         self.label = ttk.Label(self.master, text = '文本', image = bm, font=('StSong', 20, 'bold'), foreground='red')
#         self.label.bm = bm
#         self.label['compound'] = None
#         self.label.pack()
#         f = ttk.Frame(self.master)
#         f.pack(fill=BOTH, expand=YES)
#         compounds = ('None', "LEFT", "RIGHT", "TOP", "BOTTOM", 'CENTER')
#         self.var = StringVar()
#         self.var.set('None')
#         for val in compounds:
#             rb = Radiobutton(f,
#              text = val,
#              padx = 20,
#              variable = self.var,
#              command = self.change_compound,
#              value = val).pack(side=LEFT, anchor=CENTER)
#     def change_compound(self):
#             self.label['compound'] = self.var.get().lower()
# root = Tk()
# root.title('compound测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.entry = ttk.Entry(self.master,
#                                width=44,
#                                font=("StSong", 14),
#                                foreground='green')
#         self.entry.pack(fill=BOTH, expand=YES)
#         self.text = Text(self.master,
#                          width=44,
#                          height=4,
#                          font=('StSong', 14),
#                          foreground='green')
#         self.text.pack(fill=BOTH, expand=YES)
#         f = Frame(self.master)
#         f.pack()
#
#         ttk.Button(f, text='开始插入', command=self.insert_start).pack(side=LEFT)
#         ttk.Button(f, text='编辑处', command=self.insert_edit).pack(side=LEFT)
#         ttk.Button(f, text='结尾', command=self.insert_end).pack(side=LEFT)
#         ttk.Button(f, text='获取entry', command=self.get_entry).pack(side=LEFT)
#         ttk.Button(f, text='获取text', command=self.get_text).pack(side=LEFT)
#     def insert_start(self):
#         self.entry.insert(0, 'Kotling')
#         self.text.insert(0.0, 'kotling')
#     def insert_edit(self):
#         self.entry.insert(INSERT, 'Python')
#         self.text.insert(INSERT, 'Python')
#     def insert_end(self):
#         self.entry.insert(END, 'Python2')
#         self.text.insert(END, 'Python2')
#     def get_entry(self):
#         messagebox.showinfo(title="输入内容", message=self.entry.get())
#     def get_text(self):
#         messagebox.showinfo(title="输入内容", message=self.text.get(0.0, END))
# root = Tk()
# root.title('Entry测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         text1 = Text(self.master, height=27, width=32)
#         book = PhotoImage(file='images/serial.gif')
#         text1.bm = book
#         text1.insert(END, '\n')
#         text1.image_create(END, image=book)
#         text1.pack(side=LEFT, fill=BOTH, expand=YES)
#         text2 = Text(self.master, height=33, width=50)
#         text2.pack(side=LEFT, fill=BOTH, expand=YES)
#         self.text = text2
#         scroll = Scrollbar(self.master, command = text2.yview)
#         scroll.pack(side=RIGHT, fill=Y)
#         text2.configure(yscrollcommand=scroll.set)
#         text2.tag_configure('title', font=('宋体', 20, 'bold'), foreground='red', justify=CENTER, spacing3=20)
#         text2.tag_configure('detail', foreground='darkgray', font=('微软雅黑', 11, 'bold'), spacing2=10, spacing3=15)
#         text2.insert(END, '\n')
#         text2.insert(END, 'FENGK JAVA\n', 'title')
#         star = PhotoImage(file='images/serial.gif')
#         text2.bm = star
#         details = ('疯狂是打发斯蒂芬阿斯顿发送到发斯蒂芬阿斯蒂芬阿斯顿发斯蒂芬挨打发送到发斯蒂芬安抚阿斯蒂芬萨达' + \
#                    '握金李珊的发送到发斯蒂芬撒旦法撒旦法师法阿萨德刚sadgas搭嘎sad发送到发斯蒂芬' +\
#                    'asdfasdfasdfasdgasdgasdgasdfasdgasdgasdg \n',
#                    'sadfasdgsadgasdgasdgfasdfasdfsadgasdgasgsdagf \n',
#                    '12312fgasdfasdfasdf "123123"' +\
#                    '"asdf"asdfsadgasgasdgasdgasdgsadfsadfasdfasdfssdgsadg' +\
#                    'asdfasgsadgasdgasdgasdf\n')
#         for de in details:
#             text2.image_create(END, image=star)
#             text2.insert(END, de, 'detail')
#             url = ['https://www.baidu.com', 'https://www.baidu.com']
#             name = ['连接1', '连接2']
#             m = 0
#             for each in name:
#                 text2.tag_configure(m, foreground='blue', underline=True, font=('微軟雅黑', 13, 'bold'))
#                 text2.tag_bind(m, '<Enter>',  self.show_arraw_cursor)
#                 text2.tag_bind(m, '<Enter>',  self.show_common_cursor)
#                 text2.tag_bind(m, '<Button-1>', self.handlerAdaptor(self.click, x = url[m]))
#                 text2.insert(END, each + '\n', m)
#                 m += 1
#     def show_arraw_cursor(self, event):
#         self.text.config(cursor='arrow')
#     def show_common_cursor(self, event):
#         self.text.config(cursor='xterm')
#     def click(self, event, x):
#         import webbrowser
#         webbrowser.open(x)
#     def handlerAdaptor(self, fun, **kwds):
#         return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)
#
# root = Tk()
# root.title('Text测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Label(self.master, text="选择您喜欢的图书：").pack(fill=BOTH, expand=YES)
#         self.intVar = IntVar()
#         books = ('1', '2', '3', '4')
#         i = 1
#         for book in books:
#             ttk.Radiobutton(self.master, text = book, variable = self.intVar, command = self.change, value=i).pack(anchor=W)
#             i += 1
#         self.intVar.set(2)
#     def change (self):
#         from tkinter import messagebox
#         messagebox.showinfo(title=None, message = self.intVar.get())
#
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Label(self.master, text="选择您喜欢的图书：").pack(fill=BOTH, expand=YES)
#         self.intVar = IntVar()
#         races = ('serial.gif', 'serial.gif', 'serial.gif')
#         raceNames = ('哈哈', '呵呵', '嘻嘻')
#         i = 1
#         for rc in races:
#             bm = PhotoImage(file = 'images/' + rc)
#             r = ttk.Radiobutton(self.master,
#                                 image = bm,
#                                 text = raceNames[i - 1]
#                                 compound = RIGHT,
#                                 variable = self.intVar,
#                                 command = self.change,
#                                 value=i)
#             r.bm = bm
#             r.pack(anchor = W)
#             i += 1
#         self.intVar.set(2)
#     def change (self):
#         from tkinter import messagebox
#         messagebox.showinfo(title=None, message = self.intVar.get())
#
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Label(self.master, text="选择您喜欢的任务：").pack(fill=BOTH, expand=YES)
#         self.chars = []
#         characters = ('孙悟空', '猪八戒', '唐生', '牛魔王')
#         for ch in characters:
#             intVar = IntVar()
#             self.chars.append(intVar)
#             cb = ttk.Checkbutton(self.master,
#                               text = ch,
#                               variable = intVar,
#                               command = self.change)
#             cb.pack(anchor = W)
#         ttk.Label(self.master, text = '选择您喜欢的图书：').pack(fill=BOTH, expand=YES)
#         self.books = []
#         books = ('111', '222', '333', '444')
#         vals = ('444', '555', '666', '777')
#         i = 0
#         for book in books:
#             strVar = StringVar()
#             self.books.append(strVar)
#             cb = ttk.Checkbutton(self.master,
#                                  text = book,
#                                  variable = strVar,
#                                  onvalue = vals[i],
#                                  offvalue = '无',
#                                  command = self.books_changes)
#             cb.pack(anchor = W)
#             i += 1
#     from tkinter import messagebox
#     def change(self):
#         new_li = [str(e.get()) for e in self.chars]
#         st = ', '.join(new_li)
#         messagebox.showinfo(title=None, message=st);
#     def books_changes(self):
#         new_li = [str(e.get()) for e in self.books]
#         st = ', '.join((new_li))
#         messagebox.showinfo(title=None, message=st)
#
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         topF = Frame(self.master)
#         topF.pack(fill = Y, expand = YES)
#         self.lb = Listbox(topF)
#         self.lb.pack(side = LEFT, fill = Y, expand = YES)
#         for item in ['python', 'kotlin', 'swift', 'ruby']:
#             self.lb.insert(END, item)
#         self.lb.insert(ANCHOR,'python', 'kotlin', 'swift', 'ruby')
#         self.lb.insert(ANCHOR,'python', 'kotlin', 'swift', 'ruby')
#         scroll = Scrollbar(topF, command=self.lb.yview)
#         scroll.pack(side=RIGHT, fill=Y)
#         self.lb.configure(yscrollcommand=scroll.set)
#         f = Frame(self.master)
#         f.pack()
#         Label(f, text = '选择模式:').pack(side=LEFT)
#         modes = ('multiple', 'browse', 'single', 'extended')
#         self.strVar = StringVar()
#         for m in modes:
#             rb = ttk.Radiobutton(f, text = m, value = m, variable = self.strVar, command = self.choose_mode)
#             rb.pack(side=LEFT)
#         self.strVar.set('browse')
#     def choose_mode(self):
#         print(self.strVar.get())
#         self.lb['selectmode'] = self.strVar.get()
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         topF = Frame(self.master)
#         topF.pack(fill = Y, expand = YES)
#         self.v = StringVar()
#         self.lb = Listbox(topF, listvariable = self.v)
#         self.lb.pack(side=LEFT, fill=Y, expand=YES)
#         for item in range(20):
#             self.lb.insert(END, str(item))
#         scroll = Scrollbar(topF, command=self.lb.yview)
#         scroll.pack(side=RIGHT, fill=Y)
#         self.lb.configure(yscrollcommand=scroll.set)
#         f = Frame(self.master)
#         f.pack()
#         self.lb.bind("<Double-1>", self.click)
#         Button(f, text='选项中10项', command=self.select).pack(side=LEFT)
#         Button(f, text='清楚选中3项', command=self.clear_select).pack(side=LEFT)
#         Button(f, text='删除3项', command=self.detele).pack(side=LEFT)
#         Button(f, text='绑定变量', command=self.var_select).pack(side=LEFT)
#     def select(self):
#         self.lb.select_set(0, 9)
#     def clear_select(self):
#         self.lb.selection_clear(1, 3)
#     def detele(self):
#         self.lb.delete(5, 8)
#     def var_select(self):
#         self.v.set(('12', '15'))
#     def click(self, event):
#         from tkinter import messagebox
#         messagebox.showinfo(title=None, message=str(self.lb.curselection()))
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.strVar = StringVar()
#         self.cb = ttk.Combobox(self.master, textvariable=self.strVar, postcommand=self.choose)
#         self.cb.pack(side=TOP)
#         self.cb['values'] = ['Python', 'Ruby', 'Kotlin', 'Swift']
#         f = Frame(self.master)
#         f.pack()
#         self.isreadonly = IntVar()
#         Checkbutton(f, text = '是否只读', variable=self.isreadonly, command=self.change).pack(side=LEFT)
#         Button(f, text = '绑定变量设置', command=self.setvalue).pack(side=LEFT)
#     def choose(self):
#         from tkinter import  messagebox
#         messagebox.showinfo(title=None, message=str(self.cb.get()))
#     def change(self):
#         self.cb['state'] = 'readonly' if self.isreadonly.get() else 'enable'
#     def setvalue(self):
#         self.strVar.set('我爱python')
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Label(self.master, text = '指定 from to increment').pack()
#         self.sb1 = Spinbox(self.master, from_ = 20, to = 100, increment = 5)
#         self.sb1.pack(fill = X, expand=YES)
#         ttk.Label(self.master, text = '指定values').pack()
#         self.sb2 = Spinbox(self.master,
#                           values = ('python', 'swift', 'kotlin', 'ruby'),
#                           command = self.press)
#         self.sb2.pack(fill=X, expand = YES)
#         ttk.Label(self.master, text = '绑定变量').pack()
#         self.intVar = IntVar()
#         sb3 = Spinbox(self.master, values = list(range(20, 100, 4)), textvariable = self.intVar, command = self.press)
#         sb3.pack(fill = X, expand = YES)
#         self.intVar.set(33)
#     def press(self):
#         print(self.sb2.get())
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.scale = Scale(self.master,
#                            from_ = -100,
#                            to = 100,
#                            resolution = 5,
#                            label = '示範scale',
#                            length = 400,
#                            width = 39,
#                            troughcolor = 'lightblue',
#                            sliderlength = 20,
#                            sliderrelief = SUNKEN,
#                            showvalue=YES,
#                            orient = HORIZONTAL)
#         self.scale.pack()
#         f = Frame(self.master)
#         f.pack(fill = X, expand=YES, padx = 10)
#         Label(f, text = '是否显示值：').pack(side=LEFT)
#         i = 0
#         self.showVar = IntVar()
#         self.showVar.set(1)
#         for s in ('不显示', '显示'):
#             Radiobutton(f, text = s, value = i, variable=self.showVar, command = self.switch_show).pack(side=LEFT)
#             i += 1
#         f = Frame(self.master)
#         f.pack(fill = X, expand = YES, padx = 10)
#         Label(f, text = '方向：').pack(side=LEFT)
#         i = 0
#         self.orientVar = IntVar()
#         self.orientVar.set(0)
#         for s in ('水平', '垂直'):
#             Radiobutton(f, text = s, value = i, variable=self.orientVar, command=self.switch_orient).pack(side=LEFT)
#             i += 1
#     def switch_show(self):
#         self.scale['showvalue'] = self.showVar.get()
#     def switch_orient(self):
#         self.scale['orient'] = VERTICAL if self.orientVar.get() else HORIZONTAL
#     def press(self):
#         print(self.sb2.get())
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.scale = ttk.LabeledScale(self.master,
#                                       from_ = -100,
#                                       to = 100,
#                                       compound = BOTTOM)
#         self.scale.value = -20
#         self.scale.pack(fill=X, expand = YES)
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         lf = ttk.LabelFrame(self.master, text='请选择图书', padding=20)
#         lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
#         books = ['1', '2', '3', '4']
#         i = 0
#         self.intVar = IntVar()
#         for book in books:
#             Radiobutton(lf, text = '疯狂' + book + '讲义',
#                         value = i,
#                         variable = self.intVar).pack(side=LEFT)
#             i += 1
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.lf = ttk.LabelFrame(self.master, padding = 20)
#         self.lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
#         bm = PhotoImage(file = 'images/serial.gif')
#         lb = Label(self.lf, image=bm)
#         lb.bm = bm
#         self.lf['labelwidget'] = lb
#         self.books = ['e', 's', 'w', 'n', 'es', 'ws', 'en', 'wn', 'ne', 'nw', 'se', 'sw']
#         i = 0
#         self.intVar = IntVar()
#         for book in self.books:
#             Radiobutton(self.lf, text=book, value=i, command=self.change, variable=self.intVar).pack(side=LEFT)
#             i += 1
#         self.intVar.set(9)
#     def change(self):
#         self.lf['labelanchor'] = self.books[self.intVar.get()]
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         style = ttk.Style()
#         style.configure('fkit.TPanedwindow', background='red', relief = RAISED)
#         pwindow = ttk.PanedWindow(self.master, orient=VERTICAL, style="fkit.TPanedwindow")
#         pwindow.pack(fill = BOTH, expand=1)
#         first = ttk.Label(pwindow, text="第一个标签")
#         pwindow.add(first)
#         okBn = ttk.Button(pwindow, text = "第二个区域", command= lambda : pwindow.remove(okBn))
#         pwindow.add(okBn)
#         entry = ttk.Entry(pwindow, width = 30)
#         pwindow.add(entry)
#         pwindow.insert(1, Label(pwindow, text='插入的标签'))
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         style = ttk.Style()
#         style.configure('fkit.TPanedwindow', background='red', relief = RAISED)
#         pwindow = ttk.PanedWindow(self.master, orient=HORIZONTAL, style="fkit.TPanedwindow")
#         pwindow.pack(fill=BOTH, expand=YES)
#         left = ttk.Label(pwindow, text="左边标签", background='red')
#         pwindow.add(left)
#         rightwindow = PanedWindow(pwindow, orient=VERTICAL)
#         pwindow.add(rightwindow)
#         top = Label(rightwindow, text="右上标签", background='lightgreen')
#         rightwindow.add(top)
#         bottom = Label(rightwindow, text="右下标签", background='red')
#         rightwindow.add(bottom)
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         style = ttk.Style()
#         style.configure('fkit.TPanedwindow', background='red', relief = RAISED)
#         pwindow = ttk.PanedWindow(self.master, orient=HORIZONTAL, style="fkit.TPanedwindow")
#         pwindow.pack(fill=BOTH, expand=YES)
#         left = ttk.Label(pwindow, text="左边标签", background='red')
#         pwindow.add(left)
#         rightwindow = PanedWindow(pwindow, orient=VERTICAL)
#         pwindow.add(rightwindow)
#         top = Label(rightwindow, text="右上标签", background='lightgreen')
#         rightwindow.add(top)
#         bottom = Label(rightwindow, text="右下标签", background='red')
#         rightwindow.add(bottom)
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.sv = StringVar()
#         self.om = ttk.OptionMenu(root,
#                                  self.sv,
#                                  '1',
#                                  '2',
#                                  '3',
#                                  '4',
#                                  '5',
#                                  '6',
#                                  '7',
#                                  '8',
#                                  '9',
#                                  command=self.print_option)
#         self.om.pack()
#         lf = ttk.LabelFrame(self.master, padding=20, text='请选择菜单方向')
#         lf.pack(fill=BOTH, expand=YES, padx = 10, pady = 10)
#         self.directions = ['below', 'above', 'left', 'right', 'flush']
#         i = 0
#         self.intVar = IntVar()
#         for direct in self.directions:
#             Radiobutton(lf, text = direct, value = i, command= self.change, variable=self.intVar).pack(side=LEFT)
#             i += 1
#         self.intVar.set(9)
#     def print_option(self, val):
#         print(self.sv.get(), val)
#     def change(self):
#         self.om['direction'] = self.directions[self.intVar.get()]
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.msg = '疯sdfsdfasdfasdfasdfasdfasdfasdfasdfasdf'
#         ttk.Button(self.master, text = '打开', command=self.open_simpledialog).pack(side=LEFT, ipadx = 5, ipady = 5, padx = 10)
#         ttk.Button(self.master, text='打开doalog', command=self.open_dialog).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
#     def open_simpledialog(self):
#         d = simpledialog.SimpleDialog(self.master, title='simpleDialog', text=self.msg, buttons=['是', '否', '取消'], cancel=3, default=0)
#         print(d.go())
#     def open_dialog(self):
#         d = dialog.Dialog(self.master, {'title': '测试', 'text':self.msg, 'bitmap': 'question', 'default': 0, 'strings': ('确定', '取消', '退出')})
#         print(d.num)
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class MyDialog(Toplevel):
#     def __init__(self, parent, title = None, modal=True):
#         Toplevel.__init__(self, parent)
#         self.transient(parent)
#         if title: self.title(title)
#         self.parent = parent
#         self.result = None
#         frame = Frame(self)
#         self.initital_foucus = self.init_widgets(frame)
#         frame.pack(padx = 5, pady = 5)
#         self.init_buttoms()
#         if modal: self.grab_set()
#         if not self.initital_foucus:
#             self.initital_foucus = self
#         self.protocol('WM_DELETE_WINDOW', self.cancel_click)
#         self.geometry('+%d+%d' % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
#         print(self.initital_foucus)
#         self.initital_foucus.focus_set()
#         self.wait_window(self)
#     def init_widgets(self, master):
#         Label(master, text='用户名', font=12, width=10).grid(row=1, column=0)
#         self.name_entry = Entry(master, font=16)
#         self.name_entry.grid(row=1, column=1)
#         Label(master, text = '密码', font = 12, width = 10).grid(row = 2, column = 0)
#         self.pass_entry = Entry(master, font=16)
#         self.pass_entry.grid(row=2, column=1)
#     def init_buttoms(self):
#         f = Frame(self)
#         w = Button(f, text='确定', width=10, command=self.ok_click, default=ACTIVE)
#         w.pack(side=LEFT, padx=5, pady=5)
#         w = Button(f, text = '取消', width=10, command=self.cancel_click)
#         w.pack(side=LEFT, padx=5, pady=5)
#         self.bind('<Return>', self.ok_click)
#         self.bind('<Escape>', self.cancel_click)
#         f.pack()
#     def validate(self):
#         return True
#     def process_input(self):
#         use_name = self.name_entry.get()
#         use_pass = self.pass_entry.get()
#         messagebox.showinfo(message='用户输入的用户名： %s, 密码: %s' % (use_name, use_pass))
#     def ok_click(self, event=None):
#         print('确定')
#         if not self.validate():
#             self.initital_foucus.focus_set()
#             return
#         self.withdraw()
#         self.update_idletasks()
#         self.process_input()
#         self.parent.focus_set()
#         self.destroy()
#     def cancel_click(self, event=None):
#         print('取消')
#         self.parent.focus_set()
#         self.destroy()
#
# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Button(self.master, text='模式对话框', command=self.open_modal).pack(side=LEFT, ipadx=5, ipady = 5, padx=  10)
#         ttk.Button(self.master, text='非模式对话框', command=self.open_none_modal).pack(side=LEFT, ipadx=5, ipady = 5, padx=  10)
#     def open_modal(self):
#         d = MyDialog(self.master, title='模式对话框')
#     def open_none_modal(self):
#         d = MyDialog(self.master, title='非模式对话框', modal=False)
#
# root = Tk()
# root.title('颜色对话')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Button(self.master, text='输入整数对话框', command=self.open_integer).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='输入浮点数对话框', command=self.open_float).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='输入字符串对话框', command=self.open_string).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#     def open_integer(self):
#         print(simpledialog.askinteger("猜糖果", "你猜我手上有几个糖果", initialvalue=3, minvalue=1, maxvalue=10))
#     def open_float(self):
#         print(simpledialog.askfloat("猜体重", "你猜我体重多少斤", initialvalue=273, minvalue=10, maxvalue=50))
#     def open_string(self):
#         print(simpledialog.askstring("猜名字", "你猜我叫什么名", initialvalue="111"))
#
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()


# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Button(self.master, text='打开单个文件', command=self.open_file).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='打开多个文件', command=self.open_files).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='获取打开单个文件的文件名', command=self.open_filename).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='获取打开多个文件的文件名', command=self.open_filenames).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='获取保存文件', command=self.save_file).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='获取保存文件的名称', command=self.save_filename).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#         ttk.Button(self.master, text='打开目录', command=self.open_dir).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
#
#     def open_file(self):
#         print(filedialog.askopenfile(title='打开单个文件', filetypes=[('文本文件', '*.txt'), ('python文件', '*.py')], initialdir='g:/'))
#     def open_files(self):
#         print(filedialog.askopenfiles(title='打开多个文件', filetypes=[('文本文件', '*.txt'), ('python文件', '*.py')], initialdir='g:/'))
#     def open_filename(self):
#         print(filedialog.askopenfilename(title='获取打开单个文件的文件名', filetypes=[('文本文件', '*.txt'), ('python文件', '*.py')], initialdir='g:/'))
#     def open_filenames(self):
#         print(filedialog.askopenfilenames(title='获取打开多个文件的文件名', filetypes=[('文本文件', '*.txt'), ('python文件', '*.py')], initialdir='g:/'))
#     def save_file(self):
#         print(filedialog.asksaveasfile(title='获取保存文件', filetypes=[('文本文件', '*.txt'), ('python文件', '*.py')], initialdir='g:/'))
#     def save_filename(self):
#         print(filedialog.asksaveasfilename(title='获取保存文件的名称', filetypes=[('文本文件', '*.txt'), ('python文件', '*.py')], initialdir='g:/'))
#     def open_dir(self):
#         print(filedialog.askdirectory(title='获取保存文件的名称', initialdir='g:/'))
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         ttk.Button(self.master, text='选择颜色', command=self.choose_color).pack(side=LEFT, ipadx = 5, ipady = 5, padx = 10)
#     def choose_color(self):
#         print (colorchooser.askcolor(parent=self.master, title='选择画笔颜色', color = 'blue'))
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         topF = Frame(self.master)
#         topF.pack(fill=BOTH)
#         lfl = ttk.LabelFrame(topF, text = '请选择图标类型')
#         lfl.pack(side=LEFT, fill=BOTH, expand=YES, padx = 10, pady = 5)
#         i = 0
#         self.iconVar = IntVar()
#         self.icons = [None, "error", "info", "question", "warning"]
#         for icon in self.icons:
#             Radiobutton(lfl, text = icon if icon is not None else '默认', value = i, variable=self.iconVar).pack(side=TOP, anchor=W)
#             i += 1
#         self.iconVar.set(0)
#         lf2 = ttk.LabelFrame(topF, text='请选择按钮类型')
#         lf2.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=5)
#         i = 0
#         self.typeVar = IntVar()
#         self.types = [None, "abortretryignore", "ok", "okcancel", "retrycancel", "yesno", "yesnocancel"]
#         for tp in self.types:
#             Radiobutton(lf2, text=tp if tp is not None else '默认', value=i, variable=self.typeVar).pack(side=TOP,
#                                                                                                            anchor=W)
#             i += 1
#         self.typeVar.set(0)
#         bottomF = Frame(self.master)
#         bottomF.pack(fill=BOTH)
#         btn1 = ttk.Button(bottomF, text="showinfo", command=self.showinfo_clicked)
#         btn1.pack(side=LEFT, fill=X, ipadx = 5, ipady = 5, pady = 5, padx = 5)
#         btn2 = ttk.Button(bottomF, text="showwaring", command=self.showwaring_clicked)
#         btn2.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#         btn3 = ttk.Button(bottomF, text="showerror", command=self.showerror_clicked)
#         btn3.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#         btn4 = ttk.Button(bottomF, text="askquestion", command=self.askquestion_clicked)
#         btn4.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#         btn5 = ttk.Button(bottomF, text="askokcancel", command=self.askokcancel_clicked)
#         btn5.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#         btn6 = ttk.Button(bottomF, text="askyesno", command=self.askyesno_clicked)
#         btn6.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#         btn7 = ttk.Button(bottomF, text="askyesnocancel", command=self.askyesnocancel_clicked)
#         btn7.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#         btn8 = ttk.Button(bottomF, text="askretrycancel", command=self.askretrycancel_clicked)
#         btn8.pack(side=LEFT, fill=X, ipadx=5, ipady=5, pady=5, padx=5)
#     def showinfo_clicked(self):
#         print(messagebox.showinfo("Info", "showinfo测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def showwaring_clicked(self):
#         print(messagebox.showinfo("Warning", "showwaring测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def showerror_clicked(self):
#         print(messagebox.showinfo("Error", "showerror测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def askquestion_clicked(self):
#         print(messagebox.askquestion("Question", "askquestion测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def askokcancel_clicked(self):
#         print(messagebox.askokcancel("OkCancel", "askokcancel测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def askyesno_clicked(self):
#         print(messagebox.askyesno("YesNo", "askyesno测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def askyesnocancel_clicked(self):
#         print(messagebox.askyesnocancel("YesNoCancel", "askyesnocancel测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
#     def askretrycancel_clicked(self):
#         print(messagebox.askretrycancel("Retrycancel", "askretrycancel测试", icon = self.icons[self.iconVar.get()], type = self.types[self.typeVar.get()]))
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.init_menu()
#     def init_menu(self):
#         menubar = Menu(self.master)
#         self.master.filenew_icon = PhotoImage(file = "images/serial.gif")
#         self.master.fileopen_icon = PhotoImage(file = "images/serial.gif")
#         self.master['menu'] = menubar
#         file_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label = '文件', menu=file_menu)
#         lang_menu = Menu(menubar, tearoff=0)
#         menubar.add_cascade(label='选择语言', menu = lang_menu)
#         file_menu.add_command(labnel='新建', command = None, image = self.master.filenew_icon, compound=LEFT)
#         file_menu.add_command(labnel='打开', command = None, image = self.master.fileopen_icon, compound=LEFT)
#         file_menu.add_separator()
#         sub_menu = Menu(file_menu, tearoff = 0)
#         file_menu.add_cascade(label = '选择性别', menu = sub_menu)
#         self.genderVar = IntVar()
#         for i , im in enumerate(['男', '女', '保密']):
#             sub_menu.add_radiobutton(label = im, command = self.choose_gender, variable=self.genderVar, value = i)
# root = Tk()
# root.title('radiobuttom测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.init_menu()
#     def init_menu(self):
#         menubar = Menu(self.master)
#         self.master.filenew_icon = PhotoImage(file='images/serial.gif')
#         self.master.fileopen_icon = PhotoImage(file='images/serial.gif')
#         self.master['menu'] = menubar
#         file_menu = Menu(menubar, tearoff = 0)
#         menubar.add_cascade(label = '文件', menu = file_menu)
#         lang_menu = Menu(menubar, tearoff = 0)
#         menubar.add_cascade(label = '选择语言', menu = lang_menu)
#         file_menu.add_command(label = '新建', command = None, image = self.master.filenew_icon, compound = LEFT)
#         file_menu.add_command(label = '打开', command = None, image = self.master.fileopen_icon, compound = LEFT)
#         file_menu.add_separator()
#         sub_menu = Menu(file_menu, tearoff = 0)
#         file_menu.add_cascade(label = '选择性别', menu = sub_menu)
#         self.genderVar = IntVar()
#         for i, im in enumerate(['男', '女', '保密']):
#             sub_menu.add_radiobutton(label = im, command = self.cloose_gender, variable = self.genderVar, value = i)
#         self.langVars = [StringVar(), StringVar(), StringVar(), StringVar()]
#         for i, im in enumerate(('p', 'j', 'r', 'g')):
#             lang_menu.add_checkbutton(label = im, command=self.cloose_lang, onvalue=im, variable = self.langVars[i])
#     def cloose_gender(self):
#         messagebox.showinfo(message=('选择的性别为: %s' % self.genderVar.get()))
#     def cloose_lang(self):
#         rt_list = [e.get() for  e in self.langVars]
#         messagebox.showinfo(message=('选择的语言为: %s' % ','.join(rt_list)))
# root = Tk()
# root.title('菜单测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.init_icons()
#         self.init_menu()
#         self.init_toolbar()
#         leftframe = ttk.Frame(self.master, width = 40)
#         leftframe.pack(side=LEFT, fill=Y)
#         lb = Listbox(leftframe, font=('Courier New', 20))
#         lb.pack(fill=Y, expand = YES)
#         for s in ('p', 'r', 's', 'k', 'j'):
#             lb.insert(END, s)
#         mainframe = ttk.Frame(self.master)
#         mainframe.pack(side=LEFT, fill=BOTH)
#         text = Text(mainframe, width = 40, font=('Courier New', 16))
#         text.pack(fill = BOTH,  side = LEFT)
#         scroll = ttk.Scrollbar(mainframe)
#         scroll.pack(side=LEFT, fill = Y)
#         scroll['command'] = text.yview
#         text.configure(yscrollcommand = scroll.set)
#     def init_menu(self):
#         menus = ('文件', '編輯', '帮助')
#         items = (OrderedDict([
#             ('新建', (self.master.filenew_icon, None)),
#             ('打开', (self.master.fileopen_icon, None)),
#             ('保存', (self.master.save_icon, None)),
#             ('另存为', (self.master.saveas_icon, None)),
#             ('-1', (None, None)),
#             ('退出', (self.master.signout_icon, None)),
#         ]), OrderedDict([('撤销', (None, None)),
#                          ('重做', (None, None)),
#                          ('-1', (None, None)),
#                          ('剪切', (None, None)),
#                          ('复制', (None, None)),
#                          ('粘贴', (None, None)),
#                          ('删除', (None, None)),
#                          ('删除', (None, None)),
#                          ('选择', (None, None)),
#                          ('-2', (None, None)),
#                          ('更多', OrderedDict([
#
#                              ('显示数据', (None, None)),
#                              ('显示统计', (None, None)),
#                              ('显示图表', (None, None))
#                          ])),
#                          ]), OrderedDict([('帮助主题', (None, None)), ('-1', (None, None)), ('关于', (None, None))]))
#         menubar= Menu(self.master)
#         self.master['menu'] = menubar
#         for i, m_title in enumerate(menus):
#             m = Menu(menubar, tearoff = 0)
#             menubar.add_cascade(label = m_title, menu = m)
#             tm = items[i]
#             for label in tm:
#                 print(label)
#                 if isinstance(tm[label], OrderedDict):
#                     sm = Menu(m, tearoff = 0)
#                     m.add_cascade(label=label, menu = sm)
#                     sub_dict = tm[label]
#                     for sub_label in sub_dict:
#                         if sub_label.startswith('-'):
#                             sm.add_separator()
#                         else:
#                             sm.add_command(label=sub_label, image=sub_dict[sub_label][0], command = sub_dict[sub_label][1], compound =LEFT)
#                 elif label.startswith('-'):
#                     m.add_separator()
#                 else:
#                     m.add_command(label=label, image = tm[label][0], command = tm[label][1], compound = LEFT)
#     def init_icons(self):
#         self.master.filenew_icon = PhotoImage(file='images/serial.gif')
#         self.master.fileopen_icon = PhotoImage(file='images/serial.gif')
#         self.master.save_icon = PhotoImage(file='images/serial.gif')
#         self.master.saveas_icon = PhotoImage(file='images/serial.gif')
#         self.master.signout_icon = PhotoImage(file='images/serial.gif')
#     def init_toolbar(self):
#         toolframe = Frame(self.master, height = 20, bg = 'lightgray')
#         toolframe.pack(fill = X)
#         frame = ttk.Frame(toolframe)
#         frame.pack(side =LEFT)
#         for i, e in enumerate(dir(self.master)):
#             if e.endswith('_icon'):
#                 ttk.Button(frame, width = 20, image = getattr(self.master, e), command = None).grid(row = 0, column = i, padx = 1, pady = 1, sticky = E)
# root = Tk()
# root.title('菜单测试')
# App(root)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.initWidgets()
#     def initWidgets(self):
#         self.text = Text(self.master, height=12, width = 60, foreground='darkgray', font=('微软雅黑', 12), spacing2=8, spacing3 = 12)
#         self.text.pack()
#         st = '1111123123123123123sdfasdfasdgasdgasdgasdgdasgasdgasdgasdgasdfasfsadgasgasdgasdgasdgasdgasdgasdfasdf'
#         self.text.insert(END, st)
#         self.text.bind('<Button-3>', self.popup)
#         self.popup_menu = Menu(self.master, tearoff = 0)
#         self.my_items = (OrderedDict([('超大', 16), ('大', 14), ('中', 12), ('小', 10), ('超小', 8)]),
#                          OrderedDict([('红色', 'red'), ('绿色', 'green'), ('蓝色', 'blue')]))
#         i = 0
#         for k in ['字体大小', '颜色']:
#             m = Menu(self.popup_menu, tearoff = 0)
#             self.popup_menu.add_cascade(label = k, menu = m)
#             for im in self.my_items[i]:
#                 m.add_command(label = im, command = self.handlerAdaptor(self.choose, x = im))
#             i += 1
#     def popup (self, event):
#         self.popup_menu.post(event.x_root, event.y_root)
#     def choose(self, x):
#         if x in self.my_items[0].keys():
#             self.text['font'] = ('微软雅黑', self.my_items[0][x])
#         if x in self.my_items[1].keys():
#             self.text['foreground'] = self.my_items[1][x]
#     def handlerAdaptor(self, fun, **kwds):
#         return lambda fun = fun, kwds = kwds: fun (**kwds)
# root = Tk()
# root.title('菜单测试')
# App(root)
# root.mainloop()

# root = Tk()
# cv = Canvas(root, background='white')
# cv.pack(fill=BOTH, expand=YES)
# cv.create_rectangle(30, 30, 200, 200,
#                     outline='red',
#                     stipple='question',
#                     fill='red',
#                     width=5)
# cv.create_oval(240, 30, 330, 200,
#                outline='yellow',
#                fill='pink',
#                width=4)
# root.mainloop()

# root = Tk()
# root.title('绘制图形项')
# cv = Canvas(root, background='white', width = 830, height = 830)
# cv.pack(fill = BOTH, expand = YES)
# columnFont = ('微软雅黑', 18)
# titleFont =('微软雅黑', 20, 'bold')
# for i, st in enumerate(['默认', '指定边宽', '指定填充', '边框颜色', '位图填充']):
#     cv.create_text((130 + i * 140, 20), text = st, font = columnFont, fill = 'gray', anchor = W, justify = LEFT)
# cv.create_text(10, 60, text = '绘制矩形', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# options = [(None, None, None, None), (4, None, None, None), (4, 'pink', None, None), (4, 'pink', 'blue', None),  (4, 'pink', 'blue', 'error')]
# for i, op in enumerate(options):
#     cv.create_rectangle(130 + i * 140, 59, 240 + i * 140, 120, width = op[0], fill = op[1], outline = op[2], stipple = op[3])
# cv.create_text(10, 160, text = '绘制椭圆', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# options = [(None, None, None, None), (4, None, None, None), (4, 'pink', None, None), (4, 'pink', 'blue', None),  (4, 'pink', 'blue', 'error')]
# for i, op in enumerate(options):
#     cv.create_oval(130 + i * 140, 150, 240 + i * 140, 220, width = op[0], fill = op[1], outline = op[2], stipple = op[3])
# cv.create_text(10, 260, text = '绘制多边形', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# options = [(None, None, None, None), (4, None, None, None), (4, 'pink', None, None), (4, 'pink', 'blue', None),  (4, 'pink', 'blue', 'error')]
# for i, op in enumerate(options):
#     cv.create_polygon(130 + i * 140, 320, 185 + i * 140, 250, 240 + i * 140, 320, width = op[0], fill = op[1], outline = op[2], stipple = op[3])
# cv.create_text(10, 360, text = '绘制扇形', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# options = [(None, None, None, None), (4, None, None, None), (4, 'pink', None, None), (4, 'pink', 'blue', None),  (4, 'pink', 'blue', 'error')]
# for i, op in enumerate(options):
#     cv.create_arc(130 + i * 140, 350, 240 + i * 140, 420, width = op[0], fill = op[1], outline = op[2], stipple = op[3])
# cv.create_text(10, 460, text = '绘制弓形', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# options = [(None, None, None, None), (4, None, None, None), (4, 'pink', None, None), (4, 'pink', 'blue', None),  (4, 'pink', 'blue', 'error')]
# for i, op in enumerate(options):
#     cv.create_arc(130 + i * 140, 450, 240 + i * 140, 520, width = op[0], fill = op[1], outline = op[2], start = 30, extent = 60, style = CHORD, stipple = op[3])
# cv.create_text(10, 560, text = '弧形', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
#
# options = [(None, None, None, None), (4, None, None, None), (4, 'pink', None, None), (4, 'pink', 'blue', None),  (4, 'pink', 'blue', 'error')]
# for i, op in enumerate(options):
#     cv.create_arc(130 + i * 140, 550, 240 + i * 140, 620, width = op[0], fill = op[1], outline = op[2], start = 30, extent = 60, style = ARC, stipple = op[3])
# cv.create_text(10, 560, text = '绘制直线', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# options = [(None, None, None, None, None), (6, None, None, BOTH, (20, 40, 10)), (6, 'pink', None, FIRST, (40, 40, 10)),  (6, 'pink', None, LAST, (60, 50, 10)),  (4, 'pink', 'error', None, None)]
# for i, op in enumerate(options):
#     cv.create_line(130 + i * 140, 650, 240 + i * 140, 720, width = op[0], fill = op[1], stipple = op[2], arrow = op[3], arrowshape = op[4])
# cv.create_text(10, 760, text = '绘制位图', font = titleFont, fill = 'magenta', anchor = W, justify = LEFT)
#
# funcs = [Canvas.create_bitmap, Canvas.create_image, Canvas.create_window]
# items = [{'bitmap': 'questhead'}, {'image': PhotoImage(file = 'images/serial.gif')}, {'window': Button(cv, text = '单机我', padx = 10, pady = 5, command = lambda  :print('按钮点击')), 'anchor': W}]
# for i, func in enumerate(funcs):
#     func(cv, 230 + i * 140, 780, **items[i])
# root.mainloop()

# BOARD_WIDTH = 535
# BOARD_HEIGHT = 536
# BOARD_SIZE = 15
# X_OFFSET = 21
# Y_OFFSET = 23
# X_RATE = (BOARD_WIDTH - X_OFFSET * 2) / (BOARD_SIZE - 1)
# Y_RATE = (BOARD_WIDTH - Y_OFFSET * 2) / (BOARD_SIZE - 1)
# BLACK_CHESS = '黑'
# WIDTH_CHESS = '白'
# board = []
# for i in range(BOARD_SIZE):
#     row = ["+"] * BOARD_SIZE
#     board.append(row)
# root = Tk()
# root.resizable(width=False, height=False)
# root.title('五子棋')
# cv = Canvas(root, background='white', width = BOARD_WIDTH, height = BOARD_HEIGHT)
# cv.pack()
# bm = PhotoImage(file="images/serial.gif")
# cv.create_image(BOARD_HEIGHT / 2 + 1, BOARD_HEIGHT / 2 + 1, image = bm)
# selectedbm = PhotoImage(file="images/serial.gif")
# selected = cv.create_image(-100, -100, image = selectedbm)
# def move_handler(event):
#     selectedX = max(0, min(round((event.x - X_OFFSET) / X_RATE), 14))
#     selectedY = max(0, min(round((event.y - Y_OFFSET) / X_RATE), 14))
#     cv.coords(selected, (selectedX * X_RATE + X_OFFSET, selectedY * Y_RATE + Y_OFFSET))
# black = PhotoImage(file= 'images/serial.gif')
# white = PhotoImage(file= 'images/serial.gif')
# def click_handle(event):
#     userX = max(0, min(round((event.x - X_OFFSET) / X_RATE), 14))
#     userY = max(0, min(round((event.y - Y_OFFSET) / X_RATE), 14))
#     if board[userY][userX] == "+":
#         cv.create_image(userX * X_RATE + X_OFFSET, userY * Y_RATE + Y_OFFSET, image = black)
#         board[userY][userX] = '黑'
#         while(True):
#             comX = random.randint(0, BOARD_SIZE - 1)
#             comY = random.randint(0, BOARD_SIZE - 1)
#             if board[comY][comX] == "+": break
#         cv.create_image(comX * X_RATE + X_OFFSET, comX * Y_RATE + Y_OFFSET, image = white)
#         board[comY][comX] = '白'
# def leave_heandler(event):
#     cv.coords(selected, -100, -100)
#
# cv.bind('<Motion>', move_handler)
# cv.bind('<Button-1>', click_handle)
# cv.bind('<Leave>', leave_heandler)
# root.mainloop()

# root = Tk()
# root.title('操作标签')
# cv = Canvas(root, background='white', width = 620, height = 250)
# cv.pack(fill = BOTH, expand = YES)
# rt = cv.create_rectangle(40, 40, 300, 220, outline = 'blue', width = 2, tag = ('t1', 't2', 't3', 'tag4'))
# print(rt)
# oval = cv.create_oval(350, 50, 580, 200, fill = 'yellow', width = 0, tag = ('g1', 'g2', 'g3', 'tag4'))
# print(oval)
# print(cv.find_withtag('tag4'))
# print(cv.gettags(rt))
# print(cv.gettags(2))
# cv.dtag(1, 't1')
# cv.dtag(oval, 'g1')
# print(cv.gettags(rt))
# print(cv.gettags(2))
# cv.addtag_all('t5')
# print(cv.gettags(1))
# print(cv.gettags(oval))
# cv.addtag_withtag('t6', 'g2')
# print(cv.gettags(1))
# print(cv.gettags(oval))
# cv.addtag_above('t7', 't2')
# print(cv.gettags(1))
# print(cv.gettags(oval))
# cv.addtag_below('t8', 'g2')
# print(cv.gettags(1))
# print(cv.gettags(oval))
# cv.addtag_closest('t9', 360, 90)
# print(cv.gettags(1))
# print(cv.gettags(oval))
# cv.addtag_closest('t10', 30, 30, 600, 240)
# print(cv.gettags(1))
# print(cv.gettags(oval))
# cv.addtag_closest('t11', 250, 30, 400, 240)
# print(cv.gettags(1))
# print(cv.gettags(oval))
# root.mainloop()

# root = Tk()
# root.title('操作图形选项')
# cv = Canvas(root, background = 'white', width = 400, height = 300)
# cv.pack(fill = BOTH, expand = YES)
# current = None
# current_outline = None
# def show_current():
#     if current is not None:
#         if cv.itemcget(current, 'outline') == 'red':
#             cv.itemconfig(current, width = 2, outline = 'yellow')
#         else:
#             cv.itemconfig(current, width = 2, outline='red')
#     global t
#     t = threading.Timer(0.2, show_current)
#     t.start()
# t = threading.Timer(0.2, show_current)
# t.start()
# rect = cv.create_rectangle(30, 30, 250, 200, fill = 'magenta', width = '0')
# oval = cv.create_oval(180, 50, 380, 180, fill = 'yellow', width = '0')
# circle = cv.create_oval(120, 150, 300, 300, fill = 'pink', width = '0')
# bottomF = Frame(root)
# bottomF.pack(fill = X, expand = True)
# liftbn = Button(bottomF, text = '向上', command = lambda : cv.tag_raise(oval, cv.find_above(oval)))
# liftbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# lowerbn = Button(bottomF, text='向下', command = lambda : cv.tag_lower(oval, cv.find_below(oval)))
# lowerbn.pack(side=LEFT, ipadx=10, ipady=5, padx = 3)
# def change_fill():
#     fill_color = colorchooser.askcolor(parent=root, title = '选择填充颜色', color = cv.itemcget(oval, 'fill'))
#     if fill_color is not None:
#         cv.itemconfig(oval, fill = fill_color[1])
# fillbn = Button(bottomF, text = '改变填充颜色', command=change_fill)
# fillbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# def change_outline():
#     outline_color = colorchooser.askcolor(parent = root, title = '选择边框颜色', color = cv.itemcget(oval, 'outline'))
#     if outline_color is not None:
#         cv.itemconfig(oval, outline = outline_color[1], width = 4)
#
# outlinebn = Button(bottomF, text = '改变边框颜色', command=change_outline)
# fillbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# movebn = Button(bottomF, text = '右下移动', command = lambda : cv.move(oval, 15, 10))
# movebn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# coordsbn = Button(bottomF, text = '位置复位', command = lambda : cv.coords(oval, 180, 50, 380, 180))
# coordsbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# bottomF = Frame(root)
# bottomF.pack(fill = X, expand = True)
# zoomoutbn = Button(bottomF, text = '缩小', command = lambda : cv.scale(oval, 180, 50, 0.8, 0.8))
# zoomoutbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# zoominbn = Button(bottomF, text = '放大', command = lambda : cv.scale(oval, 180, 50, 1.2, 1.2))
# zoominbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# def select_handler(ct):
#     global current, current_outline, current_width
#     if ct is not None and len(ct) > 0:
#         ct = ct[0]
#         if current is not None:
#             cv.itemconfig(current, outline = current_outline, width = current_width)
#             current_outline = cv.itemcget(ct, 'outline')
#             current_width = cv.itemcget(ct, 'width')
#             current = ct
# def click_handler(event):
#     ct = cv.find_closest(event.x, event.y)
#     select_handler(ct)
# def client_select():
#     cv.unbind('<B1-Motion>')
#     cv.unbind('<ButtonRelease-1>')
#     cv.bind('<Button-1>', click_handler)
# clickbn = Button(bottomF, text = '点选图形项', command = client_select)
# clickbn.pack(side=LEFT, ipadx = 19, ipady = 5, padx = 3)
# firstx = firsty = None
# prev_select = None
# def drag_handler(event):
#     global firstx, firsty, prev_select
#     if firstx is None and firsty is None:
#         firstx, firsty = event.x, event.y
#     leftx, lefty = min(firstx, event.x), min(firsty, event.y)
#     rightx, righty = max(firstx, event.x), max(firsty, event.y)
#     if prev_select is not None:
#         cv.delete(prev_select)
#     prev_select = cv.create_rectangle(leftx, lefty, rightx, righty, dash = 2)
# def release_handler(event):
#     global  firstx, firsty
#     if prev_select is not None:
#         cv.delete(prev_select)
#     if firstx is not None and firsty is not None:
#         leftx, lefty = min(firstx, event.x), min(firsty, event.y)
#         rightx, righty = max(firstx, event.x), max(firsty, event.y)
#         firstx = firsty = None
#         ct = cv.find_closest(leftx, lefty, rightx, righty)
#         select_handler(ct)
# def rect_select():
#     cv.unbind('<Button-1>')
#     cv.bind('<B1-Motion>', drag_handler)
#     cv.bind('<ButtonRelease-1>', release_handler)
# rectbn = Button(bottomF, text = '框选图形项')
# rectbn.pack(side=LEFT, ipadx = 10, ipady = 5, padx = 3)
# deletebtn = Button(bottomF, text = '删除', command = lambda : cv.delete(oval))
# deletebtn.pack(side = LEFT, ipadx = 10, ipady = 5, padx = 3)
# root.mainloop()

# class App:
#     def __init__(self, master):
#         self.master = master
#         self.width = IntVar()
#         self.width.set(1)
#         self.outline = 'black'
#         self.fill = None
#         self.prevx = self.prevy = -10
#         self.firstx = self.firsty = -10
#         self.mv_prevx = self.mv_prevy = -10
#         self.item_type = 0
#         self.points = []
#         self.init_widgets()
#         self.temp_item = None
#         self.temp_items = []
#         self.choose_item = None
#     def init_widgets(self):
#         self.cv = Canvas(root, background='white')
#         self.cv.pack(fill=BOTH, expand=True)
#         self.cv.bind('<B1-Motion>', self.drag_handler)
#         self.cv.bind('<ButtonRelease-1>', self.release_handler)
#         self.cv.bind('<Double-1>', self.double_handler)
#         f = ttk.Frame(self.master)
#         f.pack(fill=X)
#         self.bns = []
#         for i, lb in enumerate(('直线', '矩形', '椭圆', '多边形', '铅笔')):
#             bn = Button(f, text = lb, command = lambda i=i: self.choose_type(i))
#             bn.pack(side=LEFT, ipadx = 8, ipady = 5, padx = 5)
#             self.bns.append(bn)
#         self.bns[self.item_type]['relief'] = SUNKEN
#         ttk.Button(f, text = '边框颜色', command = self.choose_outline).pack(side=LEFT, ipadx = 8, ipady = 5, padx = 5)
#         ttk.Button(f, text = '填充颜色', command = self.choose_fill).pack(side=LEFT, ipadx = 8, ipady = 5, padx = 5)
#         om = ttk.OptionMenu(f,
#                             self.width,
#                             '1',
#                             '0',
#                             '1',
#                             '2',
#                             '3',
#                             '4',
#                             '5',
#                             '6',
#                             '7',
#                             '8',
#                             command = None)
#         om.pack(side=LEFT, ipadx = 8, ipady = 5, padx = 5)
#     def choose_type(self, i):
#         for b in self.bns: b['relief'] = RAISED
#         self.bns[i]['relief'] = SUNKEN
#         self.item_type = i
#     def choose_outline(self):
#         select_color = colorchooser.askcolor(parent=self.master, title="请选择边框颜色", color = self.outline)
#         if select_color is not None:
#             self.outline = select_color[1]
#     def choose_fill(self):
#         select_color = colorchooser.askcolor(parent = self.master, title = "请选择填充颜色", color = self.fill)
#         if select_color is not None:
#             self.fill = select_color[1]
#         else:
#             self.fill = None
#     def drag_handler(self, event):
#         if (self.item_type == 0):
#             if self.firstx < -1 and self.firsty < -1:
#                 self.firstx, self.firsty = event.x, event.y
#             if self.temp_item is not None:
#                 self.cv.delete(self.temp_item)
#             self.temp_item = self.cv.create_line(self.firstx, self.firsty, event.x, event.y, dash = 2)
#         if (self.item_type == 1 or self.item_type == 2):
#             if self.firstx < -1 and self.firsty < -1:
#                 self.firstx, self.firsty = event.x, event.y
#             if self.temp_item is not None:
#                 self.cv.delete(self.temp_item)
#             leftx, lefty = min(self.firstx, event.x), min(self.firsty, event.y)
#             rightx, righty = max(self.firstx, event.x), max(self.firsty, event.y)
#             self.temp_item = self.cv.create_rectangle(leftx, lefty, rightx, righty, dash = 2)
#         if (self.item_type == 3):
#             self.draw_polygon = True
#             if self.firstx < -1 and self.firsty < -1:
#                 self.firstx, self.firsty = event.x, event.y
#             if self.temp_item is not None:
#                 self.cv.delete(self.temp_item)
#             self.temp_item = self.cv.create_rectangle(self.firstx, self.firsty, event.x, event.y, dash = 2)
#         if self.item_type == 4:
#             if self.prevx > 0 and self.prevy:
#                 self.cv.create_line(self.prevx, self.prevy, event.x, event.y, fill = self.outline, width = self.width.get())
#         self.prevx, self.prevy = event.x, event.y
#     def item_bind(self, t):
#         self.cv.tag_bind(t, '<B3-Motion>', self.move)
#         self.cv.tag_bind(t, '<ButtonRelease-3>', self.move_end)
#     def release_handler(self, event):
#         print(self.temp_item)
#         if self.temp_item is not None:
#             if self.item_type != 3:
#                 self.cv.delete(self.temp_item)
#             else:
#                 self.temp_items.append(self.temp_item)
#         self.temp_item = None
#         if self.item_type == 0:
#             if self.firstx > 0 and self.firsty > 0:
#                 t = self.cv.create_line(self.firstx, self.firsty, event.x, event.y, fill = self.outline, width=self.width.get())
#                 self.cv.tag_bind(t, '<Button-1>', lambda event=event, t = t: self.choose_item_handler(event, t))
#                 self.item_bind(t)
#         if self.item_type == 1 or self.item_type == 2:
#             if self.firstx > 0 and self.firsty > 0:
#                 leftx, lefty = min(self.firstx, event.x), min(self.firsty, event.y)
#                 rightx, righty = max(self.firstx, event.x), max(self.firsty, event.y)
#                 if self.item_type == 1:
#                     t = self.cv.create_rectangle(leftx, lefty, rightx, righty, outline=self.outline, fill = self.fill, width = self.width.get())
#                 if self.item_type == 2:
#                     t = self.cv.create_oval(leftx, lefty, rightx, righty, outline = self.outline, fill = self.fill, width = self.width.get())
#                 self.cv .tag_bind(t, '<Button-1>', lambda  event=event, t=t: self.choose_item_handler(event, t))
#                 self.item_bind(t)
#         if self.item_type != 3:
#             self.prevx = self.prevy = -10
#             self.firstx = self.firsty = -10
#         elif(self.draw_polygon):
#             self.points.append((self.firstx, self.firsty))
#             self.firstx, self.firsty = event.x, event.y
#     def double_handler(self, event):
#         if self.item_type == 3:
#             t = self.cv.create_polygon(*self.points, outline = self.outline,
#                                        fill = "" if self.fill is None else self.fill, width = self.width.get())
#             self.cv.tag_bind(t, '<Button-1>', lambda  event=event, t=t: self.choose_item_handler(event, t))
#             self.item_bind(t)
#             self.points.clear()
#             self.firstx = self.firsty = -10
#             for it in self.temp_items: self.cv.delete(it)
#             self.temp_items.clear()
#             self.draw_polygon = False
#     def choose_item_handler(self, event, t):
#         self.choose_item = t
#     def move(self, event):
#                 if self.choose_item is not None:
#                     if self.mv_prevx > 0 and self.mv_prevy > 0:
#                         self.cv.move(self.choose_item, event.x - self.mv_prevx, event.y - self.mv_prevy)
#                     self.mv_prevx, self.mv_prevy = event.x, event.y
#     def move_end(self, event):
#         self.mv_prevx = self.mv_prevy = -10
#     def delete_item(self, event):
#         if self.choose_item is not None:
#             self.cv.delete(self.choose_item)
#
# root = Tk()
# root.title('绘图测试')
# root.geometry('800x680')
# app = App(root)
# root.bind('<Delete>', app.delete_item)
# root.mainloop()

GAME_WIDTH = 500
GAME_HEIGHT = 680
BOARD_X = 230
BOARD_Y = 600
BOARD_WIDTH = 80
BALL_RADTUS = 9
class App:
    def __init__(self, master):
        self.master = master
        self.ball_index = 0
        self.is_lose = False
        self.curx = 260
        self.cury = 30
        self.boardx = BOARD_X
        self.init_widgets()
        self.vx = random.randint(3, 6)
        self.vy = random.randint(5, 10)
        self.t = threadingfs.Timer(0.1, self.moveball)
        self.t.start()
    def init_widgets(self):
        self.cv = Canvas(root, background='white', width=GAME_WIDTH, height=GAME_HEIGHT)
        self.cv.pack()
        self.cv.focus_set()
        self.cv.bms = []
        for i in range(8):
            self.cv.bms.append(PhotoImage(file="images/serial.gif"))
        self.ball = self.cv.create_image(self.curx, self.cury, image=self.cv.bms[self.ball_index])
        self.board = self.cv.create_rectangle(BOARD_X, BOARD_Y, BOARD_X + BOARD_WIDTH, BOARD_Y + 20, width = 0, fill = 'lightblue')
        self.cv.bind('<Left>', self.move_left)
        self.cv.bind('<Right>', self.move_right)
    def move_left(self, event):
        if self.boardx <= 0:
            return
        self.boardx -= 5
        self.cv.coords(self.board, self.boardx, BOARD_Y, self.boardx + BOARD_WIDTH, BOARD_Y + 20)
    def move_right(self, event):
        if self.boardx + BOARD_WIDTH >= GAME_WIDTH:
            return
        self.boardx += 5
        self.cv.coords(self.board, self.boardx, BOARD_Y, self.boardx + BOARD_WIDTH, BOARD_Y + 20)
    def moveball(self):
        self.curx += self.vx
        self.cury += self.vy
        if self.curx + BALL_RADTUS >= GAME_WIDTH:
            self.vx = -self.vx
        if self.curx - BALL_RADTUS <= 0:
            self.vx = -self.vx
        if self.cury - BALL_RADTUS <= 0:
            self.vy = -self.vy
        if self.cury + BALL_RADTUS >= BOARD_Y:
            if self.boardx <= self.curx <= (self.boardx + BOARD_WIDTH):
                self.vy = -self.vy
            else:
                messagebox.showinfo(title="失敗", message='輸了')
                self.is_lose = True
        self.cv.coords(self.ball, self.curx, self.cury)
        self.ball_index += 1
        self.cv.itemconfig(self.ball, image=self.cv.bms[self.ball_index % 8])
        if not self.is_lose:
            self.t = threadingfs.Timer(0.1, self.moveball)
            self.t.start()
root = Tk()
root.title('弹球游戏')
root.geometry('%dx%d' % (GAME_WIDTH, GAME_HEIGHT))
root.resizable(width=False, height=False)
App(root)
root.mainloop()