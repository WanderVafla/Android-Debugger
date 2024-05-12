from src.AndroidDebugger.debugger_commads import getLevelBattery


def update_battery(label):
    level_battery = getLevelBattery()
    label.after(1000, lambda: update_battery(label))
    label.config(text=level_battery)