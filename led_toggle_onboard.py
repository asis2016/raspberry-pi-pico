import machine
import utime



def toggle_onboard_led():
    """ Toggle onboard led (Pin 25). """
    led = machine.Pin(25, machine.Pin.OUT)

    while True:
        led.toggle()
        utime.sleep(1)


toggle_onboard_led()