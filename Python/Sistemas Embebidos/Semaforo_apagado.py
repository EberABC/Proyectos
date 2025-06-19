from machine import Pin
from utime import sleep

LedV1=Pin(10,Pin.OUT)
LedA1=Pin(11,Pin.OUT)
LedR1=Pin(12,Pin.OUT)

LedV2=Pin(8,Pin.OUT)
LedA2=Pin(7,Pin.OUT)
LedR2=Pin(6,Pin.OUT)

LedV3=Pin(20,Pin.OUT)
LedA3=Pin(19,Pin.OUT)
LedR3=Pin(18,Pin.OUT)

LedV4=Pin(28,Pin.OUT)
LedA4=Pin(27,Pin.OUT)
LedR4=Pin(26,Pin.OUT)

LedV1.value(0)
LedA1.value(0)
LedR1.value(0)

LedV2.value(0)
LedA2.value(0)
LedR2.value(0)

LedV3.value(0)
LedA3.value(0)
LedR3.value(0)

LedV4.value(0)
LedA4.value(0)
LedR4.value(0)
