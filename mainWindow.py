# from scr import *

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from PIL import Image, ImageTk

from src.AndroidDebugger.debugger_commads import getLevelBattery
from src.AndroidDebugger.functions import update_battery
from src.AndroidDebugger.interface.config.icons_PIL import *

root = tk.Tk()

statusBattery_Frame = ttk.Frame(root)
statusBattery_Frame.pack()

levelBattery_Label = ttk.Label(statusBattery_Frame, text=0)
levelBattery_Label.grid(row=0, column=0)

imageTK_battery_None = ImageTk.PhotoImage(battery_None)
imageBattery_Label = ttk.Label(statusBattery_Frame, image=imageTK_battery_None)
imageBattery_Label.grid(row=0, column=1)

update_battery(levelBattery_Label)

mainloop()