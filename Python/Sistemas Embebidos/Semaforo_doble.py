from machine import Pin
from utime import sleep

LedV1=Pin(10,Pin.OUT)
LedA1=Pin(11,Pin.OUT)
LedR1=Pin(12,Pin.OUT)

LedV2=Pin(8,Pin.OUT)
LedA2=Pin(7,Pin.OUT)
LedR2=Pin(6,Pin.OUT)

count=0
t=2

while True:
    LedR1.value(0)
    LedA2.value(0)
    LedV1.value(1)
    LedR2.value(1)
    sleep(t)
    print("1:Verde\n2:Rojo",end="\n\n")
    
    LedV1.value(0)
    LedA1.value(1)
    sleep(t)
    print("1:Amarillo\n2:Rojo",end="\n\n")
    
    LedA1.value(0)
    LedR2.value(0)
    LedR1.value(1)
    LedV2.value(1)
    sleep(t)
    print("1:Rojo\n2:Verde",end="\n\n")
    
    LedV2.value(0)
    LedA2.value(1)
    sleep(t)
    print("1:Rojo\n2:Amarillo",end="\n\n")
    
    count+=1
    print(count)
    
    
    
    
    
    