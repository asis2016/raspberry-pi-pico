from machine import Pin
import utime
           
       

sensor_pir = Pin(28, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, machine.Pin.OUT)
buzzer = Pin(13, Pin.OUT)

print('activating...')



def pir_handler(pin):
    """ Passive infrared sensor. """
    print('Alarm!')
    if pin.value():
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)


sensor_pir.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

while True:
  led.toggle()
  utime.sleep(1)

