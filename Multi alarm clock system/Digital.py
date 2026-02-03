import time
from clear import clear

def clock():
        print(f"{time.strftime("%I:%M:%S %p")}")
        time.sleep(1)
        clear()

