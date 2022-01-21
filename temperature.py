import machine
import utime


sensor_temp = machine.ADC(4)
conversion = 3.3 / (65535)



def temperature():
    """
    Read temperature from internal ADC.
    ADC 4 is the number channel that is connected with temperature sensor.    
    """
    reading = sensor_temp.read_u16() * conversion
    t = 27 - (reading - 0.706)/0.001721
    print(t)
    utime.sleep(2)
    
    
while True:
    temperature()