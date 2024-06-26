import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox 
from threading import Thread
from time import sleep
from api import api
import requests
import pyperclip  # Module để truy cập clipboard
import os
import gop
import threading
import subprocess
import socket
from tkinter import Toplevel, Label

class giaodien():
    def __init__(self) -> None:
        self.nameacc = []
        self.tokenacc = []
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Tool Gộp By VoLeTrieuLan")
        self.root.geometry("1105x650")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab4 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        self.tab5 = ttk.Frame(self.notebook)
        self.tab6 = ttk.Frame(self.notebook)
        self.tab7 = ttk.Frame(self.notebook)
        # self.tab8 = ttk.Frame(self.notebook)

        # self.notebook.add(self.tab8, text='Quản Lí Tool')
        self.notebook.add(self.tab1, text='Like Bằng Page')
        self.notebook.add(self.tab4, text='Cmt Bằng Page')
        self.notebook.add(self.tab6, text='Share Bằng Page')
        self.notebook.add(self.tab7, text='ViewLive Bằng Page')
        self.notebook.add(self.tab3, text='Cookie Acc')
        self.notebook.add(self.tab2, text='Cookie Or Token Pages')
        self.notebook.add(self.tab5, text='Quản Lí Cmt')

        self.stt = 0
        self.print_count = 0
        self.doick = 1
        self.doic = 0
       # Đường dẫn đến ảnh của bạn

    

    def savecmt(self):
        cmt = self.text_area.get("1.0", "end-1c")
        
        with open('cmt.txt','w', encoding='utf-8') as f:
            f.write(cmt)
            f.close()
        with open('cmt.txt','r', encoding='utf-8') as f:
            f = f.readlines()
        label1 = tk.Label(self.thongtinqlicmt, text=f'{len(f)}',fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=350,y=15)
        with open('cmt.txt','r',encoding='utf-8') as f:
            socmt = f.readlines()
        label1 = tk.Label(self.thongtincmt, text=f"{len(socmt)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=655,y=35)
    def resetpage(self):
        self.cookieortokenpage()
        os.remove('page.txt')
    def getnewtoken(self):
        os.remove('nameacc.txt')
        os.remove('access_tokenacc.txt')
        with open('acc.txt','r') as f:
            acc = f.readlines()
        api().threadgetnewtoken(acc,self.thongtinacc,self.thongtincookie1)
        sleep(3)

    def threadnewtoken(self):
        for _ in range(1):
            thread = threading.Thread(target=self.getnewtoken)
            thread.start()
    def runlikepage(self):
        gop.tool().bufflike(self.thanhchinhbufflike, self.thongtin,self.linktuslike.get(),self.soview.get(),self.dllay.get())
    def runcmtpage(self):
        with open('cmt.txt','r',encoding='utf-8') as f:
            f = f.readlines()
        if int(self.soviewcmt.get()) <= len(f):

            gop.buffcmt().main(self.thanhchinhbuffcmt,self.thongtincmt,self.linktuscmt.get(),self.soviewcmt.get(),self.dllaycmt.get())
        else:
            msg_box = tk.messagebox.showinfo(
                "Cảnh Báo",
                f"Bạn chỉ buff được nhỏ hơn hoặc bằng số cmt đang có trong file({len(f)})",
                icon="warning",
            )
    def runshareao(self):
        with open('tokenpage.txt','r',encoding='utf-8') as f:
            f = f.readlines()
        if int(self.soshare.get()) <= len(f):
            gop.buffshare().run_threads(self.thanhchinhbuffshare,self.thongtinshare,self.linktusshare.get(),self.soshare.get(),self.thread.get(),self.dllayshare.get())
        else:
            msg_box = tk.messagebox.showinfo(
                "Cảnh Báo",
                f"Bạn chỉ buff được số luồng nhỏ hơn hoặc bằng số token đang có trong file({len(f)})",
                icon="warning",
            )
    def viewlikestream(self):
        self.get_cookies = {
            'cf_clearance': 'LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
        }

        self.get_headers = {
            'authority': 'id.traodoisub.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'cf_clearance=LInT285MT09ex.W7etumJ3MhBKe0vREdILKMvGNoErc-1703686542-0-2-30d11ca0.cde8bdff.e0249095-150.0.0',
            'origin': 'https://id.traodoisub.com',
            'pragma': 'no-cache',
            'referer': 'https://id.traodoisub.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
                'link': f'{self.linktusview.get()}',
            }
        # lấy id bài viết
        response = requests.post('https://id.traodoisub.com/api.php', cookies=self.get_cookies, headers=self.get_headers, data=data)
        sleep(2)
        response_json = response.json()
        try:
            getid = response_json['id']
        except:
            print('Link sai hoặc bài viết chưa công khai')
        gop.threadviewlive(self.thanhchinhbuffview,self.thongtinview,getid,self.soviewlive.get(),self.timeview.get(),self.dllayview.get())
    
    def threadshareao(self):
        for _ in range(1):
            thread = threading.Thread(target=self.runshareao)
            thread.start()
    def threadcmt(self):
        for _ in range(1):
            thread = threading.Thread(target=self.runcmtpage)
            thread.start()
    def threadlikepage(self):
        for _ in range(1):
            thread = threading.Thread(target=self.runlikepage)
            thread.start()
    def threadgetpage(self):
        for _ in range(1):
            thread = threading.Thread(target=self.getpage1)
            thread.start()
    def threadviewlive(self):
        for _ in range(1):
            thread = threading.Thread(target=self.viewlikestream)
            thread.start()
    def reset(self):
        try:
            os.remove('acc.txt')
            os.remove('nameacc.txt')
            os.remove('access_tokenacc.txt')
            
            for item_id in self.thongtinacc.get_children():
                self.thongtinacc.delete(item_id)
        except:pass

    def getpage1(self):
        try:
            os.remove('cookiepage.txt')
            os.remove('tokenpage.txt')
            os.remove('lenpage.txt')
            for item_id in self.getpageeee.get_children():
                self.getpageeee.delete(item_id)

            
        except:pass

        api().threadgetpage(self.getpageeee,self.thongtincookiepage1)
    
    def paste(self):
        api().thread_savecookie(self.ck,self.thongtinacc,self.thongtincookie1,self.thongtin)
    def threadpaste(self):
        copied_text = pyperclip.paste()
        self.ck = copied_text.split()
        for _ in range(1):
            thread = threading.Thread(target=self.paste)
            thread.start()
    def toggle_color(self,label, colors, idx):
        label.config(foreground=colors[idx])
        idx = (idx + 1) % len(colors)
        label.after(100, lambda: self.toggle_color(label, colors, idx))
    def show_context_menu(self,event):
        context_menu.post(event.x_root, event.y_root)
    def deletecookie(self):
        selected_items = self.thongtinacc.selection()
        with open('acc.txt','r') as f:
            xetacc = f.readlines()
        with open('acc.txt','w') as f:
            f.close()
        with open('nameacc.txt','r',encoding='utf-8') as f:
            nameacc = f.readlines()
        with open('nameacc.txt','w',encoding='utf-8') as f:
            f.close()
        namedetele = []
        iddetele = []
        for item in selected_items:
            # Lưu giá trị của các mục đã chọn
            current_values = self.thongtinacc.item(item, 'values')
            self.thongtinacc.delete(item)
            namedetele.append(current_values[1])
            iddetele.append(current_values[2])
        for i in range(len(xetacc)):
            if (xetacc[i].split()[0] in iddetele) == False:
                with open('acc.txt','a') as f:
                    try:
                        f.write(f'{xetacc[i].split()[0]} {xetacc[i].split()[1]} {xetacc[i].split()[2]} \n')
                        f.close()
                    except:
                        f.write(f'{xetacc[i].split()[0]} {xetacc[i].split()[1]}  \n')
                        f.close()
        for i in range(len(nameacc)):
            if (nameacc[i].split()[0] in iddetele) == False:
                with open('nameacc.txt','a',encoding='utf-8') as f:
                    try:
                        f.write(f'{nameacc[i].split()[0]} {nameacc[i].split()[1]} {nameacc[i].split()[2]}\n')
                        f.close()
                    except:
                        try:
                            f.write(f'{nameacc[i].split()[0]} {nameacc[i].split()[1]}\n')
                            f.close()
                        except:
                            f.write(f'{nameacc[i].split()[0]} \n')
                            f.close()
          

    def proxy(self):
        new_window = Toplevel(self.showdevice,bg='#708090')
        new_window.title("Proxy")
        new_window.geometry("300x75")


        label = Label(new_window, text="Proxy: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=10,y=10)

        self.proxys= tk.StringVar()
        inputlink = tk.Entry(new_window,textvariable=self.proxys, width=30, bd =0, font=('Arial 10'), borderwidth=2, relief="solid")
        inputlink.place(x=75,y=10, height=23)
        with open('acc.txt','r') as f:
                saveprx = f.readlines()
        def saveproxy():
            listproxy = []
            
            with open('acc.txt','w') as f:
                f.close()
            selected_item = self.thongtinacc.selection()
            for item_id in selected_item:
                current_values = self.thongtinacc.item(item_id, 'values')
                print(current_values)
                self.thongtinacc.item(item_id, values=(current_values[0], current_values[1], current_values[2], current_values[3], current_values[4], current_values[5], current_values[6],self.proxys.get()))
                listproxy.append( f'{current_values[2]}')
            for i in range(len(saveprx)):
                print(saveprx[i])
                if saveprx[i].split()[0] in listproxy:
                    with open('acc.txt','a') as f:
                        try:
                            f.write(f'{saveprx[i].split()[0]} {saveprx[i].split()[1]} {saveprx[i].split()[2]} {self.proxys.get()}\n')
                        except:
                            f.write(f'{saveprx[i].split()[0]} {saveprx[i].split()[1]} {self.proxys.get()}\n')
                        f.close()
                else:
                    with open('acc.txt','a') as f:
                        try:
                            f.write(f'{saveprx[i].split()[0]} {saveprx[i].split()[1]} {saveprx[i].split()[2]} {saveprx[i].split()[3]}\n')
                        except:
                            try:
                                f.write(f'{saveprx[i].split()[0]} {saveprx[i].split()[1]} {saveprx[i].split()[3]}\n')
                            except:
                                try:
                                    f.write(f'{saveprx[i].split()[0]} {saveprx[i].split()[1]} {saveprx[i].split()[2]}\n')
                                except:
                                    f.write(f'{saveprx[i].split()[0]} {saveprx[i].split()[1]}\n')
                        f.close()
            new_window.destroy()
        def checkproxy1():
            proxy = self.proxys.get()
            try:
                res = requests.get("https://www.facebook.com/",
                                proxies={'http':f'http://{proxy}',
                                            'https': f'http://{proxy}'})
                if res.status_code == 200:
                    msg_box = tk.messagebox.showinfo(
                        "Thông Báo",
                        f"Proxy {proxy} LIVE",
                    )
                else:
                    msg_box = tk.messagebox.showinfo(
                        "Thông Báo",
                        f"Proxy {proxy} DIE",
                    )
            except:
                msg_box = tk.messagebox.showinfo(
                    "Thông Báo",
                    f"Proxy {proxy} DIE",
                )
           
        def threadcheckproxy():
            for _ in range(1):
                thread = threading.Thread(target=checkproxy1)
                thread.start()
        buttonstop =  tk.Button(new_window,  text='Save', 
                                command = saveproxy,
                                fg='black',
                                bg='green',
                                height= 1, 
                                width=10,).place(x=210,y=40)
        checkproxy = tk.Button(new_window,  text='Check Proxy', 
                                command = threadcheckproxy,
                                fg='black',
                                bg='cyan',
                                height= 1, 
                                width=10,).place(x=100,y=40)
        
    def tab(self):
        self.showlistreg = tk.Frame(self.tab1,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.showlistreg.pack(side=tk.LEFT,fill="both", expand=True)
        self.showlistreg.pack_propagate(False)
        self.showlistreg.configure(width = 1100, height = 850  )
        self.showlistreg.place(x=0,y=0)

        self.showdevice = tk.Frame(self.tab3,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.showdevice.pack(side=tk.LEFT)
        self.showdevice.pack_propagate(False)
        self.showdevice.configure(width = 1100, height = 850  )
        self.showdevice.place(x=0,y=0)
      
        self.getpage = tk.Frame(self.tab2,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.getpage.pack(side=tk.LEFT)
        self.getpage.pack_propagate(False)
        self.getpage.configure(width = 1100, height = 850  )
        self.getpage.place(x=0,y=0)


        self.cmtpage = tk.Frame(self.tab4,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.cmtpage.pack(side=tk.LEFT)
        self.cmtpage.pack_propagate(False)
        self.cmtpage.configure(width = 1100, height = 850  )
        self.cmtpage.place(x=0,y=0)

        self.cmt = tk.Frame(self.tab5,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.cmt.pack(side=tk.LEFT)
        self.cmt.pack_propagate(False)
        self.cmt.configure(width = 1100, height = 850  )
        self.cmt.place(x=0,y=0)

        self.shareaopage = tk.Frame(self.tab6,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.shareaopage.pack(side=tk.LEFT)
        self.shareaopage.pack_propagate(False)
        self.shareaopage.configure(width = 1100, height = 850  )
        self.shareaopage.place(x=0,y=0)   

        self.viewlive = tk.Frame(self.tab7,bg='#708090',highlightbackground='black',
                    highlightthickness=2)
        self.viewlive.pack(side=tk.LEFT)
        self.viewlive.pack_propagate(False)
        self.viewlive.configure(width = 1100, height = 850  )
        self.viewlive.place(x=0,y=0)      

        # self.quanli = tk.Frame(self.tab8,bg='#708090',highlightbackground='black',
        #             highlightthickness=2)
        # self.quanli.pack(side=tk.LEFT)
        # self.quanli.pack_propagate(False)
        # self.quanli.configure(width = 1100, height = 850  )
        # self.quanli.place(x=0,y=0)      
        
        self.notebook.pack(expand=True, fill='both')
        self.cookieacc()
        self.cookieortokenpage()
        self.likebangpage()
        self.quailicmt()
        self.cmtbangpage()
        self.shareao()
        self.viewlivestream()
        # self.quanlitool()
        self.root.mainloop()
        
    
    # def quanlitool(self):
    #     global context_menu
        
    #     self.quanlitoolframe = tk.Frame(self.getpage,bg='#2f4f4f')
    #     self.quanlitoolframe.pack(side=tk.LEFT)
    #     self.quanlitoolframe.pack_propagate(False)
    #     self.quanlitoolframe.configure(width = 1100, height = 550  )
    #     self.quanlitoolframe.place(x=0,y=0)

    def cookieortokenpage(self):
        global context_menu
        
        self.thongtincookiepage = tk.Frame(self.getpage,bg='#2f4f4f')
        self.thongtincookiepage.pack(side=tk.LEFT)
        self.thongtincookiepage.pack_propagate(False)
        self.thongtincookiepage.configure(width = 1100, height = 550  )
        self.thongtincookiepage.place(x=0,y=0)
        
        scrollbar = tk.Scrollbar(self.thongtincookiepage, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        self.getpageeee = ttk.Treeview(self.thongtincookiepage, yscrollcommand=scrollbar.set) 
        self.getpageeee.configure(style="Treeview", height=60)
        self.getpageeee.pack(expand=True, fill="both")
        self.getpageeee["columns"] = ("one", "two", "three", "four", "five", 'six','seven')
        self.getpageeee.column("one", width=50)
        self.getpageeee.column("two", width=150)
        self.getpageeee.column("three", width=150)
        self.getpageeee.column("four", width=150)
        self.getpageeee.column("five", width=200)
        self.getpageeee.column("six", width=200)
        self.getpageeee.column("seven", width=150)
        
        self.getpageeee.heading("one", text="Index", anchor=tk.W)
        self.getpageeee.heading("two", text="Name Acc", anchor=tk.W)
        self.getpageeee.heading("three", text="ID Acc", anchor=tk.W)
        self.getpageeee.heading("four", text="ID Page", anchor=tk.W)
        self.getpageeee.heading("five", text="Cookie Page", anchor=tk.W)
        self.getpageeee.heading("six", text="Token Page", anchor=tk.W)
        self.getpageeee.heading("seven", text="Status", anchor=tk.W)

        self.thongtincookiepage1 = tk.Frame(self.getpage,bg='#708090')
        self.thongtincookiepage1.pack(side=tk.LEFT)
        self.thongtincookiepage1.pack_propagate(False)
        self.thongtincookiepage1.configure(width = 1100, height = 650  )
        self.thongtincookiepage1.place(x=0,y=550)
        try:
            soacc = 0
            chuyenname = 0
            with open('acc.txt','r') as f:
                showacc = f.readlines()
            with open('nameacc.txt','r', encoding='utf-8') as f:
                nameacc = f.readlines()
            with open('cookiepage.txt','r') as f:
                page = f.readlines()
            with open('lenpage.txt','r') as f:
                lenpage = f.readlines()
            for i in range(len(page)):

                try:
                    
                    self.getpageeee.insert("", "end", values=(i+1,nameacc[chuyenname],showacc[chuyenname].split()[0],page[i].split()[0],page[i].split()[1],' ','Get_Lai_Token'))
                    soacc += int(lenpage[chuyenname])
                    if i+1 == int(lenpage[chuyenname]):
                        chuyenname += 1
                    label1 = tk.Label(self.thongtincookiepage1, text=f"{len(showacc)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                    label1.place(x=120,y=20)
                    label1 = tk.Label(self.thongtincookiepage1, text=f"{len(page)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                    label1.place(x=320,y=20)
                except:
                    
                    self.getpageeee.insert("", "end", values=(i+1,nameacc[-1],showacc[-1].split()[0],page[i].split()[0],page[i].split()[1],' ','Get_Lai_Token'))
            # self.getpageeee.insert("", "end", values=(self.i,name,self.lckie[self.i].split('c_user=')[1].split(';')[0],self.lckie[self.i],gettoken,len(self.idp),'Get Thanh Cong'))
        except:
            label1 = tk.Label(self.thongtincookiepage1, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=120,y=20)
            label1 = tk.Label(self.thongtincookiepage1, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=320,y=20)

        self.getpageeee['show'] = 'headings'
        # data = [
        #     (1, 'ID001', 'Device 1', 'Proxy 1', 'John', '1990-01-01', 'Male', 'password1', 'john@example.com', '123456', 'Active', '2024-03-14'),
        #     (2, 'ID002', 'Device 2', 'Proxy 2', 'Jane', '1995-05-05', 'Female', 'password2', 'jane@example.com', '654321', 'Inactive', '2024-03-15')
        # ]

        # for item in data:
        #     self.thanhchinh.insert("", "end", values=item)



        

        label = tk.Label(self.thongtincookiepage1, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=15)

        # Các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng

        
        # self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)

        label1 = tk.Label(self.thongtincookiepage1, text=f"Số Acc",fg='#7fff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=100,y=0)
        

        label1 = tk.Label(self.thongtincookiepage1, text=f"Số Page",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=300,y=0)
        

        buttonget =  tk.Button(self.thongtincookiepage1,  text='Get Pages', 
                            command=self.threadgetpage,
                            fg='black',
                            bg='green',
                            height= 1, 
                            width=10,).place(x=690,y=15)
        
        buttonreset =  tk.Button(self.thongtincookiepage1,  text='Reset Pages',
                            command=self.resetpage,
                            fg='black',
                            bg='yellow',
                            height= 1, 
                            width=10,).place(x=605,y=15)
    
    def viewlivestream(self):
        global context_menu
        
        self.framerun = tk.Frame(self.viewlive,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.framerun.pack(side=tk.LEFT)
        self.framerun.pack_propagate(False)
        self.framerun.configure(width = 1100, height = 510  )
        self.framerun.place(x=0,y=50)

        self.thongtinview = tk.Frame(self.viewlive,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.thongtinview.pack(side=tk.LEFT)
        self.thongtinview.pack_propagate(False)
        self.thongtinview.configure(width = 1100, height = 510  )
        self.thongtinview.place(x=0,y=560)

        self.nhapycau = tk.Frame(self.viewlive,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.nhapycau.pack(side=tk.LEFT)
        self.nhapycau.pack_propagate(False)
        self.nhapycau.configure(width = 1100, height = 50  )
        self.nhapycau.place(x=0,y=0)
        label = tk.Label(self.nhapycau, text="Input Link Tus: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=0,y=10)

        label = tk.Label(self.nhapycau, text="Input Số View Buff: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=275,y=10)

        label = tk.Label(self.nhapycau, text="Time(M): ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=510,y=10)

        label = tk.Label(self.nhapycau, text="Input Delay(S): ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=675,y=10)

        self.linktusview = tk.StringVar()
        inputlink = tk.Entry(self.nhapycau,textvariable=self.linktusview, width=20, bd =0, font=('Arial 10'), borderwidth=2, relief="solid")
        inputlink.pack(padx=5, pady=5)
        inputlink.place(x=125,y=13, height=20)

        self.soviewlive= tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.soviewlive).place(x=425,y=13)
        
        self.timeview = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.timeview).place(x=590,y=13)

        self.dllayview = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.dllayview).place(x=795,y=13)
        

        buttonrun =  tk.Button(self.nhapycau,  text='Run', command=self.threadviewlive,
                                fg='black',
                                bg='green',
                                height= 1, 
                                width=10,).place(x=1000,y=10)
        buttonstop =  tk.Button(self.nhapycau,  text='Stop', 
                                fg='black',
                                bg='red',
                                height= 1, 
                                width=10,).place(x=900,y=10)

        label = tk.Label(self.thongtinview, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=15)

        # Các màu của bảy sắc cầu vồng
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        # self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)
        soacc = 0
            
        try:
            with open('tokenpage.txt','r') as f:
                showacc = f.readlines()
            with open('lenpage.txt','r') as f:
                lenpage = f.readlines()
            for i in range(len(lenpage)):
                soacc += int(lenpage[i])
            label1 = tk.Label(self.thongtinview, text=f"{soacc}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
        except:
            

            
            label1 = tk.Label(self.thongtinview, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
    
        label1 = tk.Label(self.thongtinview, text=f"Số Page",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=500,y=0)
        label1 = tk.Label(self.thongtinview, text=f"Buff Success",fg='#7fff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=50,y=0)
        label1 = tk.Label(self.thongtinview, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=85,y=35)

        label1 = tk.Label(self.thongtinview, text=f"Buff Error",fg='#dc143c',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=250,y=0)
        label1 = tk.Label(self.thongtinview, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=285,y=35)
        scrollbar = tk.Scrollbar(self.framerun, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        

        self.thanhchinhbuffview = ttk.Treeview(self.framerun, yscrollcommand=scrollbar.set) 
        self.thanhchinhbuffview.configure(style="Treeview", height=60)
        self.thanhchinhbuffview.pack(expand=True, fill="both")
        self.thanhchinhbuffview["columns"] = ("one",  "three", "four", "five", 'six','seven','two','proxy')
        self.thanhchinhbuffview.column("one", width=50)
        self.thanhchinhbuffview.column("three", width=150)
        self.thanhchinhbuffview.column("four", width=250)
        self.thanhchinhbuffview.column("five", width=150)
        self.thanhchinhbuffview.column("six", width=100)
        self.thanhchinhbuffview.column("seven", width=150)
        self.thanhchinhbuffview.column("two", width=50)
        self.thanhchinhbuffview.column("proxy", width=100)
        
        self.thanhchinhbuffview.heading("one", text="Index", anchor=tk.W)
        self.thanhchinhbuffview.heading("three", text="ID Page", anchor=tk.W)
        self.thanhchinhbuffview.heading("four", text="Cookie Page", anchor=tk.W)
        self.thanhchinhbuffview.heading("five", text="Link Tus", anchor=tk.W)
        self.thanhchinhbuffview.heading("six", text="Tiến Độ", anchor=tk.W)
        self.thanhchinhbuffview.heading("seven", text="Status", anchor=tk.W)
        self.thanhchinhbuffview.heading("two", text="Delay(s)", anchor=tk.W)
        self.thanhchinhbuffview.heading("proxy", text="Proxy", anchor=tk.W)

        self.thanhchinhbuffview['show'] = 'headings'
    
    def shareao(self):
        global context_menu
        
        self.framerun = tk.Frame(self.shareaopage,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.framerun.pack(side=tk.LEFT)
        self.framerun.pack_propagate(False)
        self.framerun.configure(width = 1100, height = 510  )
        self.framerun.place(x=0,y=50)

        self.thongtinshare = tk.Frame(self.shareaopage,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.thongtinshare.pack(side=tk.LEFT)
        self.thongtinshare.pack_propagate(False)
        self.thongtinshare.configure(width = 1100, height = 510  )
        self.thongtinshare.place(x=0,y=560)

        self.nhapycau = tk.Frame(self.shareaopage,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.nhapycau.pack(side=tk.LEFT)
        self.nhapycau.pack_propagate(False)
        self.nhapycau.configure(width = 1100, height = 50  )
        self.nhapycau.place(x=0,y=0)
        
        label = tk.Label(self.nhapycau, text="Input Link Tus: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=0,y=10)

        label = tk.Label(self.nhapycau, text="Input Số Share Buff: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=275,y=10)

        label = tk.Label(self.nhapycau, text="THREAD: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=510,y=10)

        label = tk.Label(self.nhapycau, text="Input Delay: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=675,y=10)

        self.linktusshare = tk.StringVar()
        inputlink = tk.Entry(self.nhapycau,textvariable=self.linktusshare, width=20, bd =0, font=('Arial 10'), borderwidth=2, relief="solid")
        inputlink.pack(padx=5, pady=5)
        inputlink.place(x=125,y=13, height=20)

        self.soshare= tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.soshare).place(x=425,y=13)
        
        self.thread = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.thread).place(x=590,y=13)

        self.dllayshare = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.dllayshare).place(x=775,y=13)

        buttonrun =  tk.Button(self.nhapycau,  text='Run', command=self.threadshareao,
                                fg='black',
                                bg='green',
                                height= 1, 
                                width=10,).place(x=1000,y=10)
        buttonstop =  tk.Button(self.nhapycau,  text='Stop', 
                                fg='black',
                                bg='red',
                                height= 1, 
                                width=10,).place(x=900,y=10)

        label = tk.Label(self.thongtinshare, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=15)

        # Các màu của bảy sắc cầu vồng
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        # self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)
        soacc = 0
            
        try:
            with open('tokenpage.txt','r') as f:
                showacc = f.readlines()
            with open('lenpage.txt','r') as f:
                lenpage = f.readlines()
            for i in range(len(lenpage)):
                soacc += int(lenpage[i])
            label1 = tk.Label(self.thongtinshare, text=f"{soacc}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
        except:
            

            
            label1 = tk.Label(self.thongtinshare, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
    
        label1 = tk.Label(self.thongtinshare, text=f"Số Page",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=500,y=0)
        label1 = tk.Label(self.thongtinshare, text=f"Buff Success",fg='#7fff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=50,y=0)
        label1 = tk.Label(self.thongtinshare, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=85,y=35)

        label1 = tk.Label(self.thongtinshare, text=f"Buff Error",fg='#dc143c',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=250,y=0)
        label1 = tk.Label(self.thongtinshare, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=285,y=35)
        scrollbar = tk.Scrollbar(self.framerun, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        

        self.thanhchinhbuffshare = ttk.Treeview(self.framerun, yscrollcommand=scrollbar.set) 
        self.thanhchinhbuffshare.configure(style="Treeview", height=60)
        self.thanhchinhbuffshare.pack(expand=True, fill="both")
        self.thanhchinhbuffshare["columns"] = ("one",  "three", "four", "five", 'six','seven','two')
        self.thanhchinhbuffshare.column("one", width=50)
        self.thanhchinhbuffshare.column("three", width=150)
        self.thanhchinhbuffshare.column("four", width=300)
        self.thanhchinhbuffshare.column("five", width=150)
        self.thanhchinhbuffshare.column("six", width=100)
        self.thanhchinhbuffshare.column("seven", width=200)
        self.thanhchinhbuffshare.column("two", width=50)
        
        self.thanhchinhbuffshare.heading("one", text="Index", anchor=tk.W)
        self.thanhchinhbuffshare.heading("three", text="ID Page", anchor=tk.W)
        self.thanhchinhbuffshare.heading("four", text="Token Page", anchor=tk.W)
        self.thanhchinhbuffshare.heading("five", text="Link Tus", anchor=tk.W)
        self.thanhchinhbuffshare.heading("six", text="Tiến Độ", anchor=tk.W)
        self.thanhchinhbuffshare.heading("seven", text="Status", anchor=tk.W)
        self.thanhchinhbuffshare.heading("two", text="Delay(s)", anchor=tk.W)

        self.thanhchinhbuffshare['show'] = 'headings'
    def quailicmt(self):
        global context_menu
        
        self.framerun = tk.Frame(self.cmt,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.framerun.pack(side=tk.LEFT)
        self.framerun.pack_propagate(False)
        self.framerun.configure(width = 1100, height = 560  )
        self.framerun.place(x=0,y=0)

        self.thongtinqlicmt = tk.Frame(self.cmt,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.thongtinqlicmt.pack(side=tk.LEFT)
        self.thongtinqlicmt.pack_propagate(False)
        self.thongtinqlicmt.configure(width = 1100, height = 510  )
        self.thongtinqlicmt.place(x=0,y=560)



        buttonrun =  tk.Button(self.thongtinqlicmt,  text='SAVE', command=self.savecmt,
                                fg='black',
                                bg='green',
                                height= 1, 
                                width=10,).place(x=700,y=15)

        label = tk.Label(self.thongtinqlicmt, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=15)
        

        # Các màu của bảy sắc cầu vồng
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        # self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)
        
        

        # Tạo widget Text
        self.text_area = tk.Text(self.framerun, height=35, width=137)
        self.text_area.place(x=0, y=0)

        # Tạo scrollbar cho widget Text
        scrollbar = tk.Scrollbar(self.framerun, command=self.text_area.yview)
        scrollbar.place(x=1080, y=0, height=550)

        # Liên kết scrollbar với widget Text
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        label1 = tk.Label(self.thongtinqlicmt, text=f"Số Cmt Có:",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=250,y=15)
        try:
            with open('cmt.txt','r', encoding='utf-8') as f:
                f = f.readlines()
                for i in range(len(f)):
                    self.text_area.insert(tk.END, f[i])
            label1 = tk.Label(self.thongtinqlicmt, text=f"{len(f)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=350,y=15)
        except:
            label1 = tk.Label(self.thongtinqlicmt, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=350,y=15)
        
    def cmtbangpage(self):
        global context_menu
        
        self.framerun = tk.Frame(self.cmtpage,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.framerun.pack(side=tk.LEFT)
        self.framerun.pack_propagate(False)
        self.framerun.configure(width = 1100, height = 510  )
        self.framerun.place(x=0,y=50)

        self.thongtincmt = tk.Frame(self.cmtpage,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.thongtincmt.pack(side=tk.LEFT)
        self.thongtincmt.pack_propagate(False)
        self.thongtincmt.configure(width = 1100, height = 510  )
        self.thongtincmt.place(x=0,y=560)

        self.nhapycau = tk.Frame(self.cmtpage,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.nhapycau.pack(side=tk.LEFT)
        self.nhapycau.pack_propagate(False)
        self.nhapycau.configure(width = 1100, height = 50  )
        self.nhapycau.place(x=0,y=0)
        
        label = tk.Label(self.nhapycau, text="Input Link Tus: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=0,y=10)

        label = tk.Label(self.nhapycau, text="Input Số Cmt Buff: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=400,y=10)

        label = tk.Label(self.nhapycau, text="Input Delay: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=650,y=10)

        self.linktuscmt = tk.StringVar()
        inputlink = tk.Entry(self.nhapycau,textvariable=self.linktuscmt, width=35, bd =0, font=('Arial 10'), borderwidth=2, relief="solid")
        inputlink.pack(padx=5, pady=5)
        inputlink.place(x=125,y=13, height=20)

        self.soviewcmt = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.soviewcmt).place(x=550,y=13)

        self.dllaycmt = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.dllaycmt).place(x=750,y=13)

        buttonrun =  tk.Button(self.nhapycau,  text='Run', command=self.threadcmt,
                                fg='black',
                                bg='green',
                                height= 1, 
                                width=10,).place(x=1000,y=10)
        buttonstop =  tk.Button(self.nhapycau,  text='Stop', 
                                fg='black',
                                bg='red',
                                height= 1, 
                                width=10,).place(x=900,y=10)

        label = tk.Label(self.thongtincmt, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=15)

        # Các màu của bảy sắc cầu vồng
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        # self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)
        soacc =0
        try:
            with open('tokenpage.txt','r') as f:
                showacc = f.readlines()

   
            label1 = tk.Label(self.thongtincmt, text=f"{len(showacc)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=480,y=35)
        except:
            

            
            label1 = tk.Label(self.thongtincmt, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=480,y=35)
        
        try:
            with open('cmt.txt','r',encoding='utf-8') as f:
                socmt = f.readlines()
            label1 = tk.Label(self.thongtincmt, text=f"{len(socmt)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=655,y=35)
        except:
            label1 = tk.Label(self.thongtincmt, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=655,y=35)


        label1 = tk.Label(self.thongtincmt, text=f"Số Cmt Có",fg='#00ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=620,y=0)
        label1 = tk.Label(self.thongtincmt, text=f"Số Acc",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=450,y=0)
        label1 = tk.Label(self.thongtincmt, text=f"Buff Success",fg='#7fff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=50,y=0)
        label1 = tk.Label(self.thongtincmt, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=85,y=35)

        label1 = tk.Label(self.thongtincmt, text=f"Buff Error",fg='#dc143c',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=250,y=0)
        label1 = tk.Label(self.thongtincmt, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=285,y=35)
        scrollbar = tk.Scrollbar(self.framerun, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        

        self.thanhchinhbuffcmt = ttk.Treeview(self.framerun, yscrollcommand=scrollbar.set) 
        self.thanhchinhbuffcmt.configure(style="Treeview", height=60)
        self.thanhchinhbuffcmt.pack(expand=True, fill="both")
        self.thanhchinhbuffcmt["columns"] = ("one",  "three", "four", "five",'eight', 'six','seven','two','proxy')
        self.thanhchinhbuffcmt.column("one", width=50)
        self.thanhchinhbuffcmt.column("three", width=150)
        self.thanhchinhbuffcmt.column("four", width=150)
        self.thanhchinhbuffcmt.column("five", width=100)
        self.thanhchinhbuffcmt.column("eight", width=200)
        self.thanhchinhbuffcmt.column("six", width=100)
        self.thanhchinhbuffcmt.column("seven", width=100)
        self.thanhchinhbuffcmt.column("two", width=50)
        self.thanhchinhbuffcmt.column("proxy", width=100)
        
        self.thanhchinhbuffcmt.heading("one", text="Index", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("three", text="ID Acc", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("four", text="Cookie Acc", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("five", text="Link Tus", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("eight", text="NDung Cmt", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("six", text="Tiến Độ", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("seven", text="Status", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("two", text="Delay(s)", anchor=tk.W)
        self.thanhchinhbuffcmt.heading("proxy", text="Proxy", anchor=tk.W)

        self.thanhchinhbuffcmt['show'] = 'headings'
        # data = [
        #     (1, 'ID001', 'Device 1', 'Proxy 1', 'John', '1990-01-01', 'Male', 'password1', 'john@example.com', '123456', 'Active', '2024-03-14'),
        #     (2, 'ID002', 'Device 2', 'Proxy 2', 'Jane', '1995-05-05', 'Female', 'password2', 'jane@example.com', '654321', 'Inactive', '2024-03-15')
        # ]

        # for item in data:
        #     self.thanhchinh.insert("", "end", values=item)

        
    
    def likebangpage(self):
        global context_menu
        
        self.framerun = tk.Frame(self.showlistreg,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.framerun.pack(side=tk.LEFT)
        self.framerun.pack_propagate(False)
        self.framerun.configure(width = 1100, height = 510  )
        self.framerun.place(x=0,y=50)

        self.thongtin = tk.Frame(self.showlistreg,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.thongtin.pack(side=tk.LEFT)
        self.thongtin.pack_propagate(False)
        self.thongtin.configure(width = 1100, height = 510  )
        self.thongtin.place(x=0,y=560)

        self.nhapycau = tk.Frame(self.showlistreg,bg='#708090',highlightbackground='black',
                    highlightthickness=1)
        self.nhapycau.pack(side=tk.LEFT)
        self.nhapycau.pack_propagate(False)
        self.nhapycau.configure(width = 1100, height = 50  )
        self.nhapycau.place(x=0,y=0)
        
        label = tk.Label(self.nhapycau, text="Input Link Tus: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=0,y=10)

        label = tk.Label(self.nhapycau, text="Input Số Like Buff: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=400,y=10)

        label = tk.Label(self.nhapycau, text="Input Delay: ",fg='white',bg='#708090', font=("Arial", 13))
        label.place(x=650,y=10)

        self.linktuslike = tk.StringVar()
        inputlink = tk.Entry(self.nhapycau,textvariable=self.linktuslike, width=35, bd =0, font=('Arial 10'), borderwidth=2, relief="solid")
        inputlink.pack(padx=5, pady=5)
        inputlink.place(x=125,y=13, height=20)

        self.soview = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.soview).place(x=550,y=13)

        self.dllay = tk.StringVar()
        Thread = tk.Spinbox(self.nhapycau, from_=0, to=10000000000000,width=10,
                                textvariable = self.dllay).place(x=750,y=13)

        buttonrun =  tk.Button(self.nhapycau,  text='Run', command=self.threadlikepage,
                                fg='black',
                                bg='green',
                                height= 1, 
                                width=10,).place(x=1000,y=10)
        buttonstop =  tk.Button(self.nhapycau,  text='Stop', 
                                fg='black',
                                bg='red',
                                height= 1, 
                                width=10,).place(x=900,y=10)

        label = tk.Label(self.thongtin, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=15)

        # Các màu của bảy sắc cầu vồng
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        # self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)
        soacc = 0
        try:
            with open('acc.txt','r') as f:
                showacc = f.readlines()
            with open('lenpage.txt','r') as f:
                lenpage = f.readlines()
            for i in range(len(lenpage)):
                try:
                    soacc += int(lenpage[i])

                    label1 = tk.Label(self.thongtin, text=f"{soacc}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                    label1.place(x=530,y=35)
                except:
                    

                    
                    label1 = tk.Label(self.thongtin, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                    label1.place(x=530,y=35)
        except:
            label1 = tk.Label(self.thongtin, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
        
        label1 = tk.Label(self.thongtin, text=f"Số Page",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=500,y=0)
        label1 = tk.Label(self.thongtin, text=f"Buff Success",fg='#7fff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=50,y=0)
        label1 = tk.Label(self.thongtin, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=85,y=35)

        label1 = tk.Label(self.thongtin, text=f"Buff Error",fg='#dc143c',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=250,y=0)
        label1 = tk.Label(self.thongtin, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=285,y=35)
        scrollbar = tk.Scrollbar(self.framerun, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        

        self.thanhchinhbufflike = ttk.Treeview(self.framerun, yscrollcommand=scrollbar.set) 
        self.thanhchinhbufflike.configure(style="Treeview", height=60)
        self.thanhchinhbufflike.pack(expand=True, fill="both")
        self.thanhchinhbufflike["columns"] = ("one",  "three", "four", "five", 'six','seven','two','proxy')
        self.thanhchinhbufflike.column("one", width=50)
        self.thanhchinhbufflike.column("three", width=150)
        self.thanhchinhbufflike.column("four", width=250)
        self.thanhchinhbufflike.column("five", width=100)
        self.thanhchinhbufflike.column("six", width=100)
        self.thanhchinhbufflike.column("seven", width=100)
        self.thanhchinhbufflike.column("proxy", width=200)
        self.thanhchinhbufflike.column("two", width=50)
        
        self.thanhchinhbufflike.heading("one", text="Index", anchor=tk.W)
        self.thanhchinhbufflike.heading("three", text="ID Page", anchor=tk.W)
        self.thanhchinhbufflike.heading("four", text="Cookie Page", anchor=tk.W)
        self.thanhchinhbufflike.heading("five", text="Link Tus", anchor=tk.W)
        self.thanhchinhbufflike.heading("six", text="Tiến Độ", anchor=tk.W)
        self.thanhchinhbufflike.heading("seven", text="Status", anchor=tk.W)
        self.thanhchinhbufflike.heading("proxy", text="Proxy", anchor=tk.W)
        self.thanhchinhbufflike.heading("two", text="Delay(s)", anchor=tk.W)

        self.thanhchinhbufflike['show'] = 'headings'
        # data = [
        #     (1, 'ID001', 'Device 1', 'Proxy 1', 'John', '1990-01-01', 'Male', 'password1', 'john@example.com', '123456', 'Active', '2024-03-14'),
        #     (2, 'ID002', 'Device 2', 'Proxy 2', 'Jane', '1995-05-05', 'Female', 'password2', 'jane@example.com', '654321', 'Inactive', '2024-03-15')
        # ]

        # for item in data:
        #     self.thanhchinh.insert("", "end", values=item)

        
    def cookieacc(self):

        global context_menu
        self.thongtincookie = tk.Frame(self.showdevice,bg='#2f4f4f')
        self.thongtincookie.pack(side=tk.LEFT)
        self.thongtincookie.pack_propagate(False)
        self.thongtincookie.configure(width = 1100, height = 550  )
        self.thongtincookie.place(x=0,y=0)
        
        scrollbar = tk.Scrollbar(self.thongtincookie, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        

        self.thongtinacc = ttk.Treeview(self.thongtincookie, yscrollcommand=scrollbar.set) 
        self.thongtinacc.configure(style="Treeview", height=60)
        self.thongtinacc.pack(expand=True, fill="both")
        self.thongtinacc["columns"] = ("one", "two", "three", "four", "five", 'six','seven','eight')
        self.thongtinacc.column("one", width=50)
        self.thongtinacc.column("two", width=100)
        self.thongtinacc.column("three", width=150)
        self.thongtinacc.column("four", width=200)
        self.thongtinacc.column("five", width=200)
        self.thongtinacc.column("six", width=100)
        self.thongtinacc.column("seven", width=100)
        self.thongtinacc.column("eight", width=100)
        
        self.thongtinacc.heading("one", text="Index", anchor=tk.W)
        self.thongtinacc.heading("two", text="Name Acc", anchor=tk.W)
        self.thongtinacc.heading("three", text="ID Acc", anchor=tk.W)
        self.thongtinacc.heading("four", text="Cookie Acc", anchor=tk.W)
        self.thongtinacc.heading("five", text="Token Acc", anchor=tk.W)
        self.thongtinacc.heading("six", text="Số Page", anchor=tk.W)
        self.thongtinacc.heading("seven", text="Status", anchor=tk.W)
        self.thongtinacc.heading("eight", text="Proxy", anchor=tk.W)
        
        self.thongtinacc['show'] = 'headings'
        context_menu = tk.Menu(self.thongtinacc, tearoff=0)
        context_menu.add_command(label="Paste",command=self.threadpaste)
        context_menu.add_command(label="Delete", command=self.deletecookie)
        context_menu.add_command(label="Reset",command=self.reset )
        context_menu.add_command(label="Getnewtoken",command=self.threadnewtoken )
        context_menu.add_command(label="Proxy",command=self.proxy)
        self.thongtinacc.bind("<Button-3>", self.show_context_menu) 
        scrollbar.config(command=self.thongtinacc.yview)
        self.thongtinacc.config(yscrollcommand=scrollbar.set)


        

        self.thongtincookie1 = tk.Frame(self.showdevice,bg='#708090')
        self.thongtincookie1.pack(side=tk.LEFT)
        self.thongtincookie1.pack_propagate(False)
        self.thongtincookie1.configure(width = 1100, height = 650  )
        self.thongtincookie1.place(x=0,y=550)

        label = tk.Label(self.thongtincookie1, text="Copyright By VoLeTrieuLan",fg='#00008b',bg='#708090', font=("Arial", 15))
        label.place(x=800,y=0)

        # Các màu của bảy sắc cầu vồng
        rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
        
        # Bắt đầu nhấp nháy chữ với các màu của bảy sắc cầu vồng

        # re = requests.get('https://anotepad.com/notes/bbx7tsqp').text
        # key = (re.split('<div class="plaintext ">')[1].split('</div>')[0])
        label1 = tk.Label(self.thongtincookie1, text=f"Tool Còn 99999 Day",fg='#00008b',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=850,y=35)
        self.toggle_color(label1, rainbow_colors, 0)
        self.toggle_color(label, rainbow_colors, 0)
        try:
            sopage = 0
            with open('acc.txt','r') as f:
                showacc = f.readlines()
            with open('nameacc.txt','r', encoding='utf-8') as f:
                nameacc = f.readlines()
            with open('access_tokenacc.txt','r', encoding='utf-8') as f:
                access_tokenacc = f.readlines()
            try:
                with open('lenpage.txt','r') as f:
                    lenpage = f.readlines()
            except:
                lenpage =''
            for i in range(len(showacc)):
                try:
                    sopage += int(lenpage[i])
                    try:
                        try:
                            self.thongtinacc.insert("", "end", values=(i,nameacc[i],showacc[i].split()[0],showacc[i].split()[1],access_tokenacc[i],lenpage[i].strip(),'Token Cu',showacc[i].split()[2]))
                        except:
                            self.thongtinacc.insert("", "end", values=(i,nameacc[i],showacc[i].split()[0],showacc[i].split()[1],access_tokenacc[i],lenpage[i].strip(),'Token Cu',' '))
                    except:
                        self.thongtinacc.insert("", "end", values=(i,nameacc[i],showacc[i].split()[0],showacc[i].split()[1],access_tokenacc[i],lenpage[i].strip(),'Token Cu'))
                    label1 = tk.Label(self.thongtincookie1, text=f"{sopage}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                    label1.place(x=530,y=35)
                except:
                    try:
                        try:
                            self.thongtinacc.insert("", "end", values=(i,nameacc[i],showacc[i].split()[0],showacc[i].split()[1],access_tokenacc[i],' ','Token Cu',showacc[i].split()[2]))
                        except:
                            self.thongtinacc.insert("", "end", values=(i,nameacc[i],showacc[i].split()[0],showacc[i].split()[1],access_tokenacc[i],' ','Token Cu',' '))
                    except:
                        self.thongtinacc.insert("", "end", values=(i,nameacc[i],showacc[i].split()[0],showacc[i].split()[1],access_tokenacc[i],' ','Token Cu'))
                    label1 = tk.Label(self.thongtincookie1, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
                    label1.place(x=530,y=35)
            label1 = tk.Label(self.thongtincookie1, text=f"{len(showacc)}",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=85,y=35)
            
        except:
            
            label1 = tk.Label(self.thongtincookie1, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=85,y=35)

            

            
            label1 = tk.Label(self.thongtincookie1, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
            label1.place(x=530,y=35)
        label1 = tk.Label(self.thongtincookie1, text=f"Số Acc Live",fg='#7fff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=50,y=0)
        label1 = tk.Label(self.thongtincookie1, text=f"Số Acc Die",fg='#dc143c',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=250,y=0)
        label1 = tk.Label(self.thongtincookie1, text=f"0",fg='#f0ffff',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=285,y=35)
        label1 = tk.Label(self.thongtincookie1, text=f"Số Page",fg='#ffff00',bg='#708090', font=("Times New Roman", 15))
        label1.place(x=500,y=0)

from datetime import date
# try:
    # calling the today
    # function of date class
re = requests.get('https://anotepad.com/notes/8fc6p68c').text
update = (re.split('<div class="plaintext ">')[1].split('</div>')[0])
today = date.today()
try:
    with open('activekey.txt','r') as active:
        key = active.readline()

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # 8.8.8.8 is a public DNS server by Google
        local_ip = s.getsockname()[0]

        re = requests.get('https://anotepad.com/notes/bgwt6amb').text
        keyactive = (re.split('<div class="plaintext ">')[1].split('</div>')[0])
        # Duyệt qua từng phần tử trong danh sách
        for i in range(len(keyactive.split())):
            if key == keyactive.split()[i]:
                if (keyactive.split()[i+1]) == str(local_ip):

                    if update == 'update':
                        msg_box = tk.messagebox.showinfo(
                                    "Thông Báo",
                                    f"Tool Đã Có Phiên Bản Mới",
                                )
                    else:
                        giaodien().tab()
                else:
                    msg_box = tk.messagebox.showinfo(
                        "Cảnh Báo",
                        f"Trùng Ip Vui Lòng Liên Hệ Admin Để Kích Hoạt Key Đa",
                        icon="warning",
                )
            
except:
    def checkkey():
        root = tk.Tk()
        root.title("INPUT KEY TOOL")
        root.geometry("550x200")

        thongtincookie = tk.Frame(root,bg='white')
        thongtincookie.pack(side=tk.LEFT)
        thongtincookie.pack_propagate(False)
        thongtincookie.configure(width = 550, height = 200  )
        thongtincookie.place(x=0,y=0)

        image = Image.open("avt.png") 
        image.thumbnail((100, 100))

        # Chuyển đổi ảnh sang định dạng mà Tkinter có thể sử dụng
        photo = ImageTk.PhotoImage(image)
        # Tạo widget Label và gán ảnh vào đó
        label = tk.Label(thongtincookie, image=photo)
        label.place(x=5,y=5)

        label = tk.Label(thongtincookie,text='Copyright By VoLeTrieuLan',bg='white', font=("Times New Roman", 15)).place(x=110,y=10)
        label = tk.Label(thongtincookie,text='-- Key Được Viết Chỉ Sử Dụng Được 1 Thiết Bị Duy Nhất',bg='white', font=("Times New Roman", 12)).place(x=110,y=35)
        label = tk.Label(thongtincookie,text='-- Muốn Kích Hoạt Key Đa Thiết Bị Vui Lòng INBOX ADMIN',bg='white', font=("Times New Roman", 12)).place(x=110,y=60)
        label = tk.Label(thongtincookie,text='                      Thông Tin ADMIN',bg='white', font=("Times New Roman", 12)).place(x=110,y=85)
        key= tk.StringVar()
    
        def savekey():
            def savekeyinweb(key):
                updatenew = ''
                if key.get().strip() in key1.split():
                    with open('activekey.txt','w') as save:
                        save.write(f'{key.get().strip()}')
                        save.close()
                    for i in range(len(key1.split())):
                        if int(len(key1.split()[i])) > 15:
                            if key.get().strip() == str(key1.split()[i]):
                                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                s.connect(("8.8.8.8", 80))  # 8.8.8.8 is a public DNS server by Google
                                local_ip = s.getsockname()[0]
                                updatenew += f'{key1.split()[i]} {local_ip}\n'
                            else:
                                try:
                                    if int(len(key1.split()[i+1])) < 15:
                                        updatenew += f'{key1.split()[i]} '
                                    else:
                                        updatenew += f'{key1.split()[i]} \n'
                                except:
                                    updatenew += f'{key1.split()[i]} \n'
                        else:
                            if int(len(key1.split()[i-1])) > (15):
                                if int(len(updatenew.split()[-1])) < 15:
                                    updatenew +=''
                                else:
                                    updatenew += f'{key1.split()[i]}\n'
                            else:
                                updatenew +=''
                    # Connect to an external site to determine the IP address used for the connection
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect(("8.8.8.8", 80))  # 8.8.8.8 is a public DNS server by Google
                    local_ip = s.getsockname()[0]
                    cookies = {
                        'AnotepadId': 'AA597494957B4C25A194E8521355849DA6D040732F900D71C876B59300EAA21AF501BCD5896215AD1D42327A0296D7492E7AE943B56F3B8DB1DA7426604D6AF1DDFC3DC5B91DFC1B6920C7B0CBADB6E6180421208B882540A1D27FB8A659C36B447804DA280EB4D9820BBEAE032793AA',
                        '_au_1d': 'AU1D-0100-001696346426-VG4ZV95K-OHN9',
                        'FCNEC': '%5B%5B%22AKsRol9iXUTJfyCMp8x64DnPto2dMYd7To7V5pdOpJP_aLolo5F3DD65xETJJM6_4VUBj_-wWoVAL7nlEuii8G2PyDKT48f8w_wkUHyUumaYmqC9rk4RqeVLqIVJhIJPUvjPVyvyMdInss0f4k4Cwt3AGW8WtdCT8Q%3D%3D%22%5D%5D',
                        '_awl': '2.1708341301.5-89a510596215f6f512abf0ebddb0c0af-6763652d617369612d6561737431-0',
                        '_lc2_fpi': 'd26cbca32d68--01hv5vbqfdabdv9p29y7ehpwgh',
                        '_lc2_fpi_meta': '%7B%22w%22%3A1712814677485%7D',
                        '_lr_env_src_ats': 'false',
                        '_pubcid': '04425f32-5c56-45a0-ac66-0422e9f45962',
                        '_pubcid_cst': 'zix7LPQsHA%3D%3D',
                        'pbjs-unifiedid_cst': 'zix7LPQsHA%3D%3D',
                        '_cc_id': 'd0e37ee34345d08a9873323c5bb187eb',
                        'pbjs_fabrickId': '%7B%22fabrickId%22%3A%22E1%3AWC24xXZI7ltIad1lsp_cioCHJr-Qd7c5OeVyFVp1NWkLqvAaicRNRW75fwH58_6zvdErxGBIeQieVgx1ZguQkDdMpyNCZqJZsOWxglETyhw%22%7D',
                        'pbjs_fabrickId_cst': 'zix7LPQsHA%3D%3D',
                        '_pbjs_userid_consent_data': '3524755945110770',
                        '_li_dcdm_c': '.anotepad.com',
                        '_lr_retry_request': 'true',
                        '__gads': 'ID=dfdebfb718c3532c:T=1691855447:RT=1716283382:S=ALNI_MYThIMldyeqRuCqsNvLGb_7Re3jUg',
                        '__gpi': 'UID=00000c2b517261eb:T=1691855447:RT=1716283382:S=ALNI_MY1F6lpxRgeiuH-alF99oum_iKN3A',
                        '__eoi': 'ID=2437adaacabb2378:T=1705723748:RT=1716283382:S=AA-AfjacSGSSF0IWdXGy3RC_dwVA',
                        '_gid': 'GA1.2.821650073.1716283384',
                        'panoramaId_expiry': '1716369794083',
                        'panoramaId': '2f8b5b5aa185de3d626f76a111d9a9fb927ad2105e19af6fedeac189b2b988c3',
                        'pbjs-unifiedid': '%7B%22TDID%22%3A%223ad9ffbf-d4a4-4937-8213-6bf51270dbca%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-21T09%3A23%3A14%22%7D',
                        'pbjs-unifiedid_last': 'Tue%2C%2021%20May%202024%2009%3A23%3A13%20GMT',
                        '_ga_FVWZ0RM4DH': 'GS1.1.1716283435.4.0.1716283435.60.0.0',
                        '_ga_6PG3MM86KX': 'GS1.1.1716283381.75.1.1716283435.0.0.0',
                        '_ga': 'GA1.2.1416292129.1691855444',
                    }
                    headers = {
                        'accept': '*/*',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cache-control': 'no-cache',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        # 'cookie': 'AnotepadId=AA597494957B4C25A194E8521355849DA6D040732F900D71C876B59300EAA21AF501BCD5896215AD1D42327A0296D7492E7AE943B56F3B8DB1DA7426604D6AF1DDFC3DC5B91DFC1B6920C7B0CBADB6E6180421208B882540A1D27FB8A659C36B447804DA280EB4D9820BBEAE032793AA; _au_1d=AU1D-0100-001696346426-VG4ZV95K-OHN9; FCNEC=%5B%5B%22AKsRol9iXUTJfyCMp8x64DnPto2dMYd7To7V5pdOpJP_aLolo5F3DD65xETJJM6_4VUBj_-wWoVAL7nlEuii8G2PyDKT48f8w_wkUHyUumaYmqC9rk4RqeVLqIVJhIJPUvjPVyvyMdInss0f4k4Cwt3AGW8WtdCT8Q%3D%3D%22%5D%5D; _awl=2.1708341301.5-89a510596215f6f512abf0ebddb0c0af-6763652d617369612d6561737431-0; _lc2_fpi=d26cbca32d68--01hv5vbqfdabdv9p29y7ehpwgh; _lc2_fpi_meta=%7B%22w%22%3A1712814677485%7D; _lr_env_src_ats=false; _pubcid=04425f32-5c56-45a0-ac66-0422e9f45962; _pubcid_cst=zix7LPQsHA%3D%3D; pbjs-unifiedid_cst=zix7LPQsHA%3D%3D; _cc_id=d0e37ee34345d08a9873323c5bb187eb; pbjs_fabrickId=%7B%22fabrickId%22%3A%22E1%3AWC24xXZI7ltIad1lsp_cioCHJr-Qd7c5OeVyFVp1NWkLqvAaicRNRW75fwH58_6zvdErxGBIeQieVgx1ZguQkDdMpyNCZqJZsOWxglETyhw%22%7D; pbjs_fabrickId_cst=zix7LPQsHA%3D%3D; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.anotepad.com; _lr_retry_request=true; __gads=ID=dfdebfb718c3532c:T=1691855447:RT=1716283382:S=ALNI_MYThIMldyeqRuCqsNvLGb_7Re3jUg; __gpi=UID=00000c2b517261eb:T=1691855447:RT=1716283382:S=ALNI_MY1F6lpxRgeiuH-alF99oum_iKN3A; __eoi=ID=2437adaacabb2378:T=1705723748:RT=1716283382:S=AA-AfjacSGSSF0IWdXGy3RC_dwVA; _gid=GA1.2.821650073.1716283384; panoramaId_expiry=1716369794083; panoramaId=2f8b5b5aa185de3d626f76a111d9a9fb927ad2105e19af6fedeac189b2b988c3; pbjs-unifiedid=%7B%22TDID%22%3A%223ad9ffbf-d4a4-4937-8213-6bf51270dbca%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-04-21T09%3A23%3A14%22%7D; pbjs-unifiedid_last=Tue%2C%2021%20May%202024%2009%3A23%3A13%20GMT; _ga_FVWZ0RM4DH=GS1.1.1716283435.4.0.1716283435.60.0.0; _ga_6PG3MM86KX=GS1.1.1716283381.75.1.1716283435.0.0.0; _ga=GA1.2.1416292129.1691855444',
                        'origin': 'https://anotepad.com',
                        'pragma': 'no-cache',
                        'priority': 'u=1, i',
                        'referer': 'https://anotepad.com/notes/bgwt6amb',
                        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                        'x-requested-with': 'XMLHttpRequest',
                    }
                    data = {
                        'number': 'bgwt6amb',
                        'notetype': 'PlainText',
                        'noteaccess': '2',
                        'notepassword': '',
                        'notequickedit': 'false',
                        'notequickeditpassword': '',
                        'notetitle': 'key bac',
                        'notecontent': f'{updatenew}',
                    }

                    response = requests.post('https://anotepad.com/note/save', cookies=cookies, headers=headers, data=data)
                    if key.get() == 'S0VZIENVQSBBRE1JTg==':
                        label_with_border = tk.Label(
                            thongtincookie,
                            text="ĐÃ ACTIVE KEY CỦA ADMIN",bg='#90EE90',
                            font=("Arial", 12),
                            relief="solid",  # Kiểu viền (solid, raised, sunken, groove, ridge)
                            bd=2,  # Độ dày viền
                            padx=150,  # Padding ngang
                            pady=1  # Padding dọc
                        ).place(x=55,y=175)
                    else:
                        label_with_border = tk.Label(
                            thongtincookie,
                            text="KEY ĐÃ ĐƯỢC ACTIVE VĨNH VIÊN",bg='#90EE90',
                            font=("Arial", 12),
                            relief="solid",  # Kiểu viền (solid, raised, sunken, groove, ridge)
                            bd=2,  # Độ dày viền
                            padx=150,  # Padding ngang
                            pady=1  # Padding dọc
                        ).place(x=55,y=175)
                else:
                    msg_box = tk.messagebox.showinfo(
                    "Cảnh Báo",
                    f"KEY SAI",
                    icon="warning",
                )
            re = requests.get('https://anotepad.com/notes/bgwt6amb').text
            key1 = (re.split('<div class="plaintext ">')[1].split('</div>')[0])

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))  # 8.8.8.8 is a public DNS server by Google
            local_ip = s.getsockname()[0]
            
            if len(key1.split()) >= 2:
                for i in range(len(key1.split())):
                    print(key1.split()[i],key.get())
                    if str(key.get().strip()) == str(key1.split()[i]):
                        try:
                            if int(len(key1.split()[i+1])) < 15:
                                if key1.split()[i+1] == local_ip:
                                    savekeyinweb(key)
                                            
                                else:
                                    label_with_border = tk.Label(
                                        thongtincookie,
                                        text="KEY ĐÃ DÍNH Ở MỘT IP KHÁC",bg='#FF0000',
                                        font=("Arial", 12),
                                        relief="solid",  # Kiểu viền (solid, raised, sunken, groove, ridge)
                                        bd=2,  # Độ dày viền
                                        padx=150,  # Padding ngang
                                        pady=1  # Padding dọc
                                    ).place(x=55,y=175)
                        except:
                            savekeyinweb(key)
                    else:
                        savekeyinweb(key)
                    

            else:
                savekeyinweb(key)
            
        buttonstop =  tk.Button(thongtincookie,  text='FACEBOOK', 
                        # command = saveproxy,
                        fg='white',
                        bg='#4267B2',
                        height= 1, 
                        width=35,).place(x=10,y=110)
        buttonstop =  tk.Button(thongtincookie,  text='ZALO', 
                        # command = saveproxy,
                        fg='white',
                        bg='#0095DA',
                        height= 1, 
                        width=35,).place(x=285,y=110)

        label = tk.Label(thongtincookie,text='INPUT KEY: ',bg='white', font=("Times New Roman", 12)).place(x=10,y=145)

        inputlink = tk.Entry(thongtincookie,textvariable=key, width=40, bd =0, font=('Arial 10'), borderwidth=2, relief="solid")
        inputlink.place(x=110,y=145, height=23)

        buttonstop =  tk.Button(thongtincookie,  text='SAVE', command=savekey,
                        # command = saveproxy,
                        fg='white',
                        bg='green',
                        height= 1, 
                        width=10,).place(x=450,y=145)


        label_with_border = tk.Label(
            thongtincookie,
            text="Chưa Kích Hoạt Key",bg='white',
            font=("Arial", 12),
            relief="solid",  # Kiểu viền (solid, raised, sunken, groove, ridge)
            bd=2,  # Độ dày viền
            padx=150,  # Padding ngang
            pady=1  # Padding dọc
        ).place(x=55,y=175)

        # Chạy vòng lặp chính của Tkinter
        root.mainloop()
    checkkey()

        
# except:
#     msg_box = tk.messagebox.showinfo(
#             "Cảnh Báo",
#             f"Bản Get Key Lỗi Vui Lòng Update Tool",
#             icon="warning",
#         )
