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

imageBattery_Label = ttk.Label()

def change_photo_battery(label):
    label.cget("text")
    
    if label <= 0:
        twenty = ImageTk.PhotoImage(Image.open("res\\icons\\20%.png").resize((15,15)))
    elif label <= 20:
        fifty = ImageTk.PhotoImage(Image.open("res\\icons\\50%.png").resize((15,15)))
    elif label <= 50:
        eighty = ImageTk.PhotoImage(Image.open("res\\icons\\80%.png").resize((15,15)))
    elif label <= 80:
        one_hundred = ImageTk.PhotoImage(Image.open("res\\icons\\100%.png").resize((15,15)))
    
        
def update_all(label, root):
    while True:
        label.config(text=getLevelBattery())
        print(label.cget("text"))
        root.update()
        
loop = update_all(levelBattery_Label, root)