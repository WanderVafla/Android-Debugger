import subprocess

__all__ = ['getLevelBattery()']

def getLevelBattery():
    result = subprocess.run(["adb", "shell", "dumpsys", "battery"], capture_output=True, text=True)
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        if 'level' in line:
            battery_level = line.split(':')[-1].strip()
            return battery_level