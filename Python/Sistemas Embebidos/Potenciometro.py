from machine import Pin, ADC
from utime import sleep

pot=ADC(Pin(28))
FC=3.3/65535
while True:
    v=pot.read_u16()*FC
    print(v)
    sleep(0.2)