from machine import Pin
import utime
      

        
def traffic_light():
    """ Simple traffic light. """
    red = Pin(15, Pin.OUT)
    yellow = Pin(14, Pin.OUT)
    green = Pin(13, Pin.OUT)
    
    while True:
        red.toggle()
        utime.sleep(300)
        yellow.toggle()
        utime.sleep(300)
        green.toggle()
        utime.sleep(300)


traffic_light()