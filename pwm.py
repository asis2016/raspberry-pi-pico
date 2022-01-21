# Pulse-width modulation

import machine
import utime

potentiometer = machine.ADC(26)
led = machine.PWM(machine.Pin(15))

# freq = 1000 hertz, 1 thousand cycles / sec.
led.freq(1000)



def brightness_control():
    """ Duty cycle from PWM. """
    led.duty_u16(potentiometer.read_u16())
    

while True:
    brightness_control()
    

