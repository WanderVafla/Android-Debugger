from src.AndroidDebugger.debugger_commads import getLevelBattery
from src.AndroidDebugger.interface.config.icons_PIL import *

def update_battery(label, imageLabel):
    level_battery = getLevelBattery()
    label.after(1000, lambda: update_battery(label))
    label.config(text=level_battery)
    
    imageLabel.config(image="")