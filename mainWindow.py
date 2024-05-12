# from scr import *

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from PIL import Image, ImageTk

from src.AndroidDebugger.debugger_commads import getLevelBattery
from src.AndroidDebugger.functions import update_battery

root = tk.Tk()

statusBattery_Frame = ttk.Frame(root)
statusBattery_Frame.pack()

levelBattery_Label = ttk.Label(statusBattery_Frame, text=0)
levelBattery_Label.grid(row=0, column=0)


imageBattery_Label = ttk.Label(statusBattery_Frame)
imageBattery_Label.grid(row=0, column=1)

update_battery(levelBattery_Label)

mainloop()