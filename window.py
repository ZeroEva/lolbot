import threading
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from pywinauto import Desktop, Application, keyboard


def chose_file():
    val_file_chose.set(askopenfilename(filetypes=[('文本文档', '*.txt')]))


def refresh_app():
    windows.clear()
    for w in Desktop(backend="uia").windows():
        if w.window_text() != title:
            windows[w.window_text()] = w.class_name()
    lb_app_chose['value'] = list(windows.keys())


def read_txt(path):
    with open(path, 'r', encoding='utf8') as f:
        return f.readlines()


def send_enter(flag):
    if flag.get():
        keyboard.send_keys('{ENTER}')


def start_send():
    app = Application(backend='uia').connect(class_name=windows.get(lb_app_chose.get()))
    lb_app_chose.configure(state='readonly')
    app.top_window().set_focus()
    txt = read_txt(val_file_chose.get())
    print(val_before_enter.get(), val_before_enter.get())
    for i in txt:
        if stop_flat:
            return
        if i.strip() != '':
            send_enter(val_before_enter)
            keyboard.send_keys(i)
            send_enter(val_before_enter)


def start():
    thread.start()


def stop():
    global stop_flat
    stop_flat = True


thread = threading.Thread(target=start_send)
stop_flat = False

title = '牛逼闪闪的消息发送器'

wd = tk.Tk()
wd.title(title)
wd.geometry('500x300')

windows = {}
val_file_chose = tk.StringVar()
val_before_enter = tk.BooleanVar()
val_after_enter = tk.BooleanVar()

lb_app_chose_name = tk.Label(wd, text='程序选择', width=6, height=1, justify=tk.RIGHT)
lb_app_chose = ttk.Combobox(wd, width=35, justify=tk.LEFT, state='normal')
bt_app_refresh = tk.Button(wd, text='刷新', command=refresh_app)

refresh_app()

lb_file_chose_name = tk.Label(wd, text='文件路径', width=6, height=1, justify=tk.RIGHT)
lb_file_chose = tk.Label(wd, textvariable=val_file_chose, width=35, height=1, relief=tk.RIDGE, justify=tk.LEFT)
bt_file_chose = tk.Button(wd, text='选择文件', command=chose_file)

bt_send_enter_before = tk.Checkbutton(wd, text='输入文字前回车', variable=val_before_enter)
bt_send_enter_after = tk.Checkbutton(wd, text='输入文字后回车', variable=val_after_enter)

bt_start = tk.Button(wd, text='开始', command=start)
bt_stop = tk.Button(wd, text='停止', command=stop)

lb_app_chose_name.grid(row=0, column=0)
lb_app_chose.grid(row=0, column=1)
bt_app_refresh.grid(row=0, column=2)
lb_file_chose_name.grid(row=1, column=0)
lb_file_chose.grid(row=1, column=1)
bt_file_chose.grid(row=1, column=2)
bt_send_enter_before.grid(row=2, column=0)
bt_send_enter_after.grid(row=2, column=1)
bt_start.grid(row=4, column=0)
bt_stop.grid(row=4, column=1)

wd.mainloop()
