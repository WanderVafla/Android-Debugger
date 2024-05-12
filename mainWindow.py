# from scr import *

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from PIL import Image, ImageTk

from src.AndroidDebugger.debugger_commads import getLevelBattery

root = tk.Tk()

statusBattery_Frame = ttk.Frame(root)
statusBattery_Frame.pack()

levelBattery_Label = ttk.Label(statusBattery_Frame, text=0)
levelBattery_Label.grid(row=0, column=0)

imageBattery_Label = ttk.Label(statusBattery_Frame)
imageBattery_Label.grid(row=0, column=1)


def update_battery():
    
    level_battery = imageBattery_Label.cget("text")
    print(level_battery)
    if level_battery <= "0":
        twenty = ImageTk.PhotoImage(Image.open("res\\icons\\20%.png").resize((15,15)))
        imageBattery_Label.config(image=twenty)
    elif level_battery <= "20":
        fifty = ImageTk.PhotoImage(Image.open("res\\icons\\50%.png").resize((15,15)))
        imageBattery_Label.config(image=fifty)
    elif level_battery <= "50":
        eighty = ImageTk.PhotoImage(Image.open("res\\icons\\80%.png").resize((15,15)))
        imageBattery_Label.config(image=eighty)
    elif level_battery <= "80":
        one_hundred = ImageTk.PhotoImage(Image.open("res\\icons\\100%.png").resize((15,15)))
        imageBattery_Label.config(image=one_hundred)



        
def loop_update():
    while True:
        levelBattery_Label.config(text=getLevelBattery())
        update_battery()
        root.update()
        
loop = loop_update()