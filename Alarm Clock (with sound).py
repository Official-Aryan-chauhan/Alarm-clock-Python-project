# Alarm clcok ! For Singel Alarm System with digitl clock
import time 
from playsound3 import playsound
import os
import sys
import keyboard
from open import open_alarm_clock # Importing open_alarm_clock function to open the alarm clock script window
# Feature to add -- add multi alarm system
time_ = time.strftime("%I:%M:%S %p")
print(f"Current Time | {time_}")
# time.sleep(2)

temp_list  = []
alarm_H = (input("Enter Time of Alarm Hour : ")).strip()
alarm_M = (input("Enter Time of Alarm Minute : ")).strip()
alarm_AM_PM = input("Enter AM ro PM : ").upper().strip()
temp_list.append(alarm_H)
temp_list.append(alarm_M)
temp_list.append(alarm_AM_PM)

def clear_terminal():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _  = os.system("clear")  
        # ("Cleared Terminal")

def ring_alarm():
        print(time_)
        print("Ringing !")
        try:
            open_alarm_clock()  # Open the alarm clock script window
            playsound("E:\Git and Github\Alarm-clock-Python-project\sound.mp3")
        except KeyboardInterrupt:
            print("Alarm Stopped !")
            sys.exit(0)

while True:
        if temp_list[0] == time.strftime('%I') and temp_list[1] == time.strftime('%M') and temp_list[2] == time.strftime("%p"):
            ring_alarm()
            break
        else:
            print(time.strftime("%I:%M:%S %p"))
            time.sleep(1) 
            clear_terminal()
            continue
   
# End of the code

        
        