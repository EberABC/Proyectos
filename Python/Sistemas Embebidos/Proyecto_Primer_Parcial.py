from machine import Pin
from utime import sleep
from Sistemas import sistemas
from Efectos import efectos
from Nombres import nombres

C1  = Pin(15,Pin.OUT)
C2  = Pin(16,Pin.OUT)
C3  = Pin(17,Pin.OUT)
C4  = Pin(18,Pin.OUT)
C5  = Pin(19,Pin.OUT)
C6  = Pin(20,Pin.OUT)
C7  = Pin(21,Pin.OUT)
C8  = Pin(22,Pin.OUT)
C9  = Pin(26,Pin.OUT)
C10 = Pin(27,Pin.OUT)
C11 = Pin(28,Pin.OUT)
C12 = Pin(4,Pin.OUT)
C13 = Pin(3,Pin.OUT)
C14 = Pin(2,Pin.OUT)
C15 = Pin(1,Pin.OUT)

T1 = Pin(10,Pin.OUT)
T2 = Pin(11,Pin.OUT)
T3 = Pin(12,Pin.OUT)
T4 = Pin(13,Pin.OUT)
T5 = Pin(14,Pin.OUT)

Columns = [C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15]
Rows = [T1,T2,T3,T4,T5]

t = (1/50000)
i = 2000
def off():
    for col in Columns:
        col.value(0)
    for row in Rows:
        row.value(1)

while True:
    sistemas()
    nombres()
    efectos()
off()
