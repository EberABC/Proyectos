from machine import Pin
from utime import sleep

I1=Pin(15,Pin.OUT)
I2=Pin(16,Pin.OUT)
I3=Pin(17,Pin.OUT)
I4=Pin(18,Pin.OUT)
I5=Pin(19,Pin.OUT)

T1=Pin(14,Pin.OUT,value=0)
T2=Pin(13,Pin.OUT,value=0)
T3=Pin(12,Pin.OUT,value=0)
T4=Pin(11,Pin.OUT,value=0)
T5=Pin(10,Pin.OUT,value=0)

t=1

def on():
    I1.value(1)
    I2.value(1)
    I3.value(1)
    I4.value(1)
    I5.value(1)
    T1.value(0)
    T2.value(0)
    T3.value(1)
    T4.value(1)
    T5.value(1)

def off():
    I1.value(0)
    I2.value(0)
    I3.value(0)
    I4.value(0)
    I5.value(0)
    
def probar():
    for i in range(0,4):
        on()
        sleep(t)
        off()
        sleep(t)
    
probar()