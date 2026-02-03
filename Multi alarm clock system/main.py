# Multi alarms system;
import time
from clear import  clear
from Digital import clock
from audio import audio
# <!-- ---------------------------------------------->
print(time.strftime("%I:%M:%S %p"))
alarms = []
# <!-- ---------------------------------------------->
def user_input(nl):
    try:
        hour = int(input("Hour : ").strip())
        if hour not in range(1,13):
            return "Out of range !"
            
        minute = int(input("Minute : ").strip())
        if not minute in range(0,60):
            return "Out of range ~"
    except ValueError:
        return "Only Numbers allowed !"
    period = input("AM or PM : ").upper().strip()
    if period == "":
        return "Can't be empty !"
    if period not in ("AM","PM"):
        return "Out of Range --> Available values are (AM,PM)"
    
    format_ = f"{hour:02d}:{minute:02d}:{period}"

    if format_  in nl:
        return "Duplicate Entry Not Allowed !"

    nl.append(format_)
    clear()
    return f"Success !"
# <!-- ---------------------------------------------->
def mathcing_function(nl):
    current_time = time.strftime("%I:%M:%p") 
    for alarm in nl.copy():
        if alarm == current_time:
            nl.remove(current_time)
            audio()
            print(f"Alarmed ringed at {current_time}")
            time.sleep(2)
            continue
# <!-- ---------------------------------------------->
def main(nl):
    while True:
        choice  = input("Yes or no : ").lower()

        if choice == "":
            print("Choice can't be empty !")

        if choice not in ("yes","no","y","n") and choice != "":
            print("Choice value not defined \
                Available values are yes, no, y, n")

        if choice in ("yes","y"):
            print(user_input(alarms)) 

        if choice in ("no","n"):
            while len(alarms) != 0:
                print(f"Alarms : \
{nl}")
                mathcing_function(nl)
                clock()

            print("Thank You For Using the clock \
Program Ended")
            break

main(alarms)
