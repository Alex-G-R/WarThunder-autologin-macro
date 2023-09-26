import time
import subprocess
import pyautogui
import os

#
# / Type pip install pyautogui / in terminal or CMD
#

# dfine the path to the executable
exe_path = r'C:\Program Files (x86)\Steam\steamapps\common\War Thunder\launcher.exe'

try:
    # use subprocess to run the .exe
    subprocess.Popen(exe_path)
    print(f'Started {exe_path}')
except FileNotFoundError:
    print(f'File not found: {exe_path}')
except Exception as e:
    print(f'An error occurred: {e}')

# wait for the luncher
time.sleep(10);
# start the luncher
pyautogui.press('enter')

# wait for the game to open up 
time.sleep(40)

# get the daily present
pyautogui.press('esc')
time.sleep(3)
pyautogui.press('esc')
time.sleep(3)
pyautogui.press('esc')
time.sleep(3)

# Force shutdown the computer
time.sleep(10)
os.system("shutdown /s /f /t 0")