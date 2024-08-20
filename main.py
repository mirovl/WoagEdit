# hello everyone!

import os #for cmd functions
from tkinter import * #tkinter
from tkinter import ttk #tkinter ttk
import subprocess #open processes
import shutil #idk just was for copy
import configparser  #config
#from configparser import SafeConfigParser
### import tkinter.font 
#some for setup
win = Tk()
win.geometry("800x600")
win.resizable(False,False)
win.title("WoagEdit")
list_colors = ["#c44725",""]
debug1 = "-debug"
appdata1 = os.getenv('APPDATA')
currenta = os.getcwd()
img = PhotoImage(file='src/icon.png')
parser = configparser.ConfigParser()
if os.path.isfile('settings.ini'):
    parser.read('settings.ini')
else:
    fp = open('settings.ini', 'x')
    fp.close()
    parser.read('settings.ini')
    parser.add_section("PARAMS")
    parser.set('PARAMS','param','')
win.tk.call('wm', 'iconphoto', win._w, img)

print(currenta)
# functions
def st():
    StartGame()
def StartGame():
    if params.get() == "":
        subprocess.call("PizzaTower2.exe")
    else:
        subprocess.call(f"PizzaTower2.exe {params.get()}")
    parser.set('PARAMS','param',f'{params.get()}')
    with open('settings.ini', 'w') as configfile:
        parser.write(configfile)

def OpenFolder():
    os.startfile(f"{appdata1}/PizzaTower_GM2")

def OpenWoagules():
    os.startfile("woagules")

def UseWoagules():
    if not os.path.isfile("data.win.orig"):
        os.rename("data.win","data.win.orig")
    os.system(f"copy woagules\{mods.get()} {currenta}")
    os.rename(mods.get(),"data.win")

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


# buttons
startgame = ttk.Button(win,text="Launch",width=15,command=StartGame)
foldergame = ttk.Button(win,text="Open saves folder",width=20,command=OpenFolder)
folderwoagules = ttk.Button(win,text="Open mods folder",width=17,command=OpenWoagules)
replacemod = ttk.Button(win,text="Replace",width=7,command=UseWoagules)
canvas1.create_window( 690, 550,window = startgame)
canvas1.create_window( 110, 500,window = foldergame)
canvas1.create_window( 110, 530,window = folderwoagules)
canvas1.create_window( 199, 469,window = replacemod)

#inputs
params = ttk.Entry()
mods = ttk.Entry()
params.place(y=510,x=640)
mods.place(y=460,x=45)
params.delete(0,END)
params.insert(0,parser.get('PARAMS','param'))

#labels
canvas1.create_text(150, 70, text="WoagEdit", font=('Tiny5', 30, "bold"), fill="White")
canvas1.create_text(110, 103, text="Ver 0.2", font=('Tiny5', 8, "bold"), fill="White")
canvas1.create_text(695, 490, text="parameters (use with '-')", font=('Tiny5', 10, "bold"), fill="White")
canvas1.create_text(128, 445, text="enter mod name to import", font=('Tiny5', 10, "bold"), fill="White")


win.mainloop()
