#this file is for open the main alarm window and can run the audio !
import playsound3
import subprocess #to open the current window
import keyboard # to control the audio 
from clear import clear
def openthewindow():
    url = ("E:\Git and Github\Alarm-clock-Python-project\Multi alarm clock system\main.py")
    subprocess.run(url,shell=True)

def audio():
    openthewindow()
    if keyboard.is_pressed('q') == True:
        return "Exited" #audio is not controlable yet use the different module in future to make it more advanced !
    else:
        playsound3.playsound("E:\Git and Github\Alarm-clock-Python-project\Multi alarm clock system\sound.mp3")
        return "#stop"

