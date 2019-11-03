import sys
import time
from datetime import datetime
from turtle import *

class time_zone_clock ():
    def set_default_time(self):
        obj_turtle = Turtle()
        current_time = ""
        detail_time = str(datetime.now())
        current_time = detail_time[11:19]
        hours,min,sec = int(current_time[0:2]),int(current_time[3:5]),int(current_time[6:8])
        while True:
            #obj_turtle.clear()
            obj_turtle.clear()
            obj_turtle.write(str(hours).zfill(2) +":"+str(min).zfill(2) +":"+ str(sec).zfill(2), font=("arial",50,"normal"))
            obj_turtle.write("India Time +5 GMT")
            sec = sec + 1
            time.sleep(1)
            if sec == 60:
                sec=0
                min = min + 1
            if min == 60:
                min=0
                hours = hours + 1
            if hours == 24:
                hours = 0







if __name__ == "__main__":
    basetime1 = time_zone_clock
    basetime1.set_default_time(time_zone_clock)
