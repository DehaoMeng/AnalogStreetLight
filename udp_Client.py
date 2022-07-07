# -*- coding: utf-8 -*-

import socket
from tkinter import Tk, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL, Button, messagebox
LocalHost = "您的ip地址"

class Client:
    client_socket = None

    def __init__(self):
        self.initialize_socket()

    def initialize_socket(self):
        # 创建套接字
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class Gui:
    def __init__(self, master):
        self.root = master
        self.height = 200
        self.width = 450
        self.client = Client()
        self.initialize_gui()  # 图形化界面

    def initialize_gui(self):
        self.root.title("终端")  # 初始化
        self.root.resizable(0, 0)
        self.root.geometry("900x600")
        self.status()
        self.display_light_a()
        self.display_light_b()
        self.display_light_c()


    def status(self):
        Label(self.root, text=" 路灯终端A ", font=('heiti', 15), width=10, height=2).place(x=100, y=50)
        Label(self.root, text=" 状 态  ", font=('heiti', 30), width=7, height=2).place(x=200, y=37)
        Label(self.root, text=" 路灯终端B ", font=('heiti', 15), width=10, height=2).place(x=100, y=250)
        Label(self.root, text=" 状 态", font=('heiti', 30), width=7, height=2).place(x=200, y=237)
        Label(self.root, text=" 状 态", font=('heiti', 30), width=7, height=2).place(x=200, y=437)
        Label(self.root, text=" 路灯终端C ", font=('heiti', 15), width=10, height=2).place(x=100, y=450)
        # def server(self):
        # Button(self.root,text=" 开 始 服 务",font=('heiti',8),width=13,height=1,relief="groove").place(x=10,y=10)
        # Button(self.root,text=" 终 止 服 务 ",font=('heiti',8),width=13,height=1,relief="groove").place(x=10,y=27)


    def display_light_a(self):
        frame = Frame(self.root, height=self.height, width=self.width, bd=20, relief="groove")
        frame.place(x=450, y=0)
        Label(frame, text=" 温度：", font=('heiti', 15), width=5, height=2).place(x=10, y=15)
        Label(frame, text=" 湿度：", font=('heiti', 15), width=5, height=2).place(x=10, y=55)
        Label(frame, text=" 亮度：", font=('heiti', 15), width=5, height=2).place(x=10, y=95)
        self.t_a = Entry(frame, width=10)
        self.t_a.place(x=60, y=30)
        self.w_a = Entry(frame, width=10)
        self.w_a.place(x=60, y=70)
        self.l_a = Entry(frame, width=10)
        self.l_a.place(x=60, y=110)
        Button(frame, text=" 上 传 数 据", font=('heiti', 8), width=13, height=2, relief="groove",
               command=lambda: self.send_message(self.t_a, self.w_a, self.l_a, frame)).place(x=200, y=55)
        # self.status_light()
        # 接收数据
        # 根据收到的数据改变当前状态
        # Label(frame,text=" 状态：",font=('heiti',30),width=7,height=2).place(x=200,y=37)
        # Entry(frame,width=4).place(x=310,y=75)


    def display_light_b(self):
        frame = Frame(self.root, height=self.height, width=self.width, bd=20, relief="groove")
        frame.place(x=450, y=200)
        Label(frame, text=" 温度：", font=('heiti', 15), width=5, height=2).place(x=10, y=15)
        Label(frame, text=" 湿度：", font=('heiti', 15), width=5, height=2).place(x=10, y=55)
        Label(frame, text=" 亮度：", font=('heiti', 15), width=5, height=2).place(x=10, y=95)
        self.t_b = Entry(frame, width=10)
        self.t_b.place(x=60, y=30)
        self.w_b = Entry(frame, width=10)
        self.w_b.place(x=60, y=70)
        self.l_b = Entry(frame, width=10)
        self.l_b.place(x=60, y=110)
        Button(frame, text=" 上 传 数 据", font=('heiti', 8), width=13, height=2, relief="groove",
               command=lambda: self.send_message(self.t_b, self.w_b, self.l_b, frame)).place(x=200, y=55)
        # 接收数据
        # 根据收到的数据改变当前状态
        # Label(frame,text=" 状态：",font=('heiti',30),width=7,height=2).place(x=200,y=37)
        # Entry(frame,width=4).place(x=310,y=75)


    def display_light_c(self):
        frame = Frame(self.root, height=self.height, width=self.width, bd=20, relief="groove")
        frame.place(x=450, y=400)
        Label(frame, text=" 温度：", font=('heiti', 15), width=5, height=2).place(x=10, y=15)
        Label(frame, text=" 湿度：", font=('heiti', 15), width=5, height=2).place(x=10, y=55)
        Label(frame, text=" 亮度：", font=('heiti', 15), width=5, height=2).place(x=10, y=95)
        self.t_c = Entry(frame, width=10)
        self.t_c.place(x=60, y=30)
        self.w_c = Entry(frame, width=10)
        self.w_c.place(x=60, y=70)
        self.l_c = Entry(frame, width=10)
        self.l_c.place(x=60, y=110)
        Button(frame, text=" 上 传 数 据", font=('heiti', 8), width=13, height=2, relief="groove", command=lambda: self.send_message(self.t_c, self.w_c, self.l_c, frame)).place(x=200, y=55)
        # Label(frame,text=" 状态：",font=('heiti',30),width=7,height=2).place(x=200,y=37)


    def recvfrom_server(self, frame):
        self.status, self.address = self.client.clientsocket.recvfrom(1024)
        if self.status == b'open':
            Label(frame, text="OPEN", font=('heiti', 10), width=5, height=2, relief="groove").place(x=300, y=55)
        else:
            Label(frame, text="CLOSE", font=('heiti', 10), width=5, height=2, relief="groove").place(x=300, y=55)


    def send_message(self, t, w, l, frame):
        self.client.initialize_socket()
        data_t = t.get()
        # print(data_t)
        data_w = w.get()
        data_l = l.get()
        self.client.clientsocket.sendto(data_t.encode("utf8"), (LocalHost, 8000))
        self.client.clientsocket.sendto(data_w.encode("utf8"), (LocalHost, 8000))
        self.client.clientsocket.sendto(data_l.encode("utf8"), (LocalHost, 8000))
        if data_l == '#' or data_w == 'w' or data_t == '#':
            self.on_close_window()
        self.recvfrom_server(frame)


    def on_close_window(self):
        if messagebox.askokcancel("退出", "确定退出吗?"):
            self.root.destroy()
            self.client.clientsocket.close()
            exit(0)


if __name__ == "__main__":
    root = Tk()
    gui = Gui(root)
    root.protocol("WM_DELETE_WINDOW", gui.on_close_window)
    root.mainloop()
