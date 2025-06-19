from machine import Pin
from utime import sleep

LedV=Pin(10,Pin.OUT)
LedA=Pin(11,Pin.OUT)
LedR=Pin(12,Pin.OUT)
count=0
t=1

while True:
    LedR.value(0)
    LedV.value(1)
    sleep(t)
    LedV.value(0)
    LedA.value(1)
    sleep(t)
    LedA.value(0)
    LedR.value(1)
    sleep(t)
    count+=1
    print(count)