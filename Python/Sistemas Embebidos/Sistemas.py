from machine import Pin
from utime import sleep

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
i = 5000

def off():
    for col in Columns:
        col.value(0)
    for row in Rows:
        row.value(1)

def sistemas():
    off()
    # 1-15
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 2-16
    for x in range(i/10):
        C1.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 3-17
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 4-18
    for x in range(i/10):
        C1.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 5-19
    for x in range(i/10):
        C1.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 6-20
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 7-21
    for x in range(i/10):
        C1.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 8-22
    for x in range(i/10):
        C1.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 9-23
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 10-24
    for x in range(i/10):
        C1.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 11-25
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 12-26
    for x in range(i/10):
        C1.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 13-27
    for x in range(i/10):
        C1.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 14-28
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0,5,+3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 15-29
    for x in range(i/10):
        C1.value(1)
        for j in range(1):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0,5,+3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 16-30
    for x in range(i/10):
        C1.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0,5,+3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 17-31
    for x in range(i/10):
        C1.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0,5,+3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C15.value(0)
    # 18-32
    for x in range(i/10):
        C1.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(0,5,+3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C15.value(0)
    # 19-33
    for x in range(i/10):
        C1.value(1)
        for j in range(0,5,+4):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C1.value(0)
        C2.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C2.value(0)
        C3.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C3.value(0)
        C4.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C4.value(0)
        C5.value(1)
        for j in range(2,3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C5.value(0)
        C6.value(1)
        for j in range(1,2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C6.value(0)
        C7.value(1)
        for j in range(5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C7.value(0)
        C8.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C8.value(0)
        C9.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C9.value(0)
        C10.value(1)
        for j in range(0,5,+3):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C10.value(0)
        C11.value(1)
        for j in range(1,5):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C11.value(0)
        C12.value(1)
        for j in range(0):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C12.value(0)
        C13.value(1)
        for j in range(5):
            if j != 3:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C13.value(0)
        C14.value(1)
        for j in range(0,5,+2):
            Rows[j].value(0)
            sleep(t/5)
            Rows[j].value(1)
        C14.value(0)
        C15.value(1)
        for j in range(5):
            if j != 1:
                Rows[j].value(0)
                sleep(t/5)
                Rows[j].value(1)
        C15.value(0)
    

sistemas()
off()
