import machine
import utime

potentiometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)



def voltage():
    """ Voltage measurement through potentiometer. """
    v = potentiometer.read_u16() * conversion_factor
    print(v)
    

while True:
    voltage()
    utime.sleep(2)
