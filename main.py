# hello everyone!

import os
from tkinter import *
from tkinter import ttk
import subprocess
import shutil
### import tkinter.font 
#some for setup
win = Tk()
win.geometry("800x600")
win.resizable(False,False)
win.title("WoagEdit_ver0.1")
list_colors = ["#c44725",""]
debug1 = "-debug"
appdata1 = os.getenv('APPDATA')
currenta = os.getcwd()
img = PhotoImage(file='src/icon.png')
win.tk.call('wm', 'iconphoto', win._w, img)
print(currenta)
# functions
def st():
    StartGame()
def StartGame():
    #os.system(game)
    if params.get() == "":
        subprocess.call("PizzaTower2.exe")
    else:
        subprocess.call(f"PizzaTower2.exe {params.get()}")

def OpenFolder():
    os.startfile(f"{appdata1}/PizzaTower_GM2")

def OpenWoagules():
    os.startfile("woagules")

def UseWoagules():
    ### source1 =  os.path.join("woagules",mods.get())
    ### target = os.path.join(os.getcwd(), os.path.basename(source1))
    if not os.path.isfile("data.win.orig"):
        os.rename("data.win","data.win.orig")
    os.system(f"copy woagules\{mods.get()} {currenta}")
    os.rename(mods.get(),"data.win")
    ### shutil.copyfile(currenta, target)

def CheckTowers():
    dir_path = '/path/to/directory'
    for item in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, item)):
            print(item)

# bg
bg = PhotoImage(file = "src\warbg.png") 
canvas1 = Canvas(win, width = 400,height = 400) 
canvas1.pack(fill = "both", expand = True) 
canvas1.create_image( 0, 0, image = bg,anchor = "nw") 
### label1 = Label(win, image = bg) 
### label1.place(x = 0, y = 0)


# buttons
startgame = ttk.Button(win,text="Launch",width=15,command=StartGame)
foldergame = ttk.Button(win,text="Open saves folder",width=20,command=OpenFolder)
folderwoagules = ttk.Button(win,text="Open mods folder",width=17,command=OpenWoagules)
replacemod = ttk.Button(win,text="Replace",width=7,command=UseWoagules)
canvas1.create_window( 690, 550,window = startgame)
canvas1.create_window( 110, 500,window = foldergame)
canvas1.create_window( 110, 530,window = folderwoagules)
canvas1.create_window( 199, 469,window = replacemod)
### startgame.place(x=690,y=550)

#inputs
params = ttk.Entry()
mods = ttk.Entry()
params.place(y=510,x=640)
mods.place(y=460,x=45)

#labels
canvas1.create_text(150, 70, text="WoagEdit", font=('Tiny5', 30, "bold"), fill="White")
canvas1.create_text(110, 103, text="Ver 0.1", font=('Tiny5', 8, "bold"), fill="White")
canvas1.create_text(695, 490, text="parameters (use with '-')", font=('Tiny5', 10, "bold"), fill="White")
canvas1.create_text(128, 445, text="enter mod name to import", font=('Tiny5', 10, "bold"), fill="White")
### title_lab = ttk.Label(text="WoagEdit",font= ('Tiny5',20,"bold"),foreground="White")
### title_lab.place(x=100,y=60)


win.mainloop()
