from machine import Pin
from utime import sleep


nums = {
    0: "abcdef",
    1: "bc",
    2: "abdeg",
    3: "abcdg",
    4: "bcfg",
    5: "acdfg",
    6: "acdefg",
    7: "abc",
    8: "abcdefg",
    9: "abcfg"
}

a = Pin(14, Pin.OUT)
b = Pin(13, Pin.OUT)
c = Pin(12, Pin.OUT)
d = Pin(11, Pin.OUT)
e = Pin(10, Pin.OUT)
f = Pin(9, Pin.OUT)
g = Pin(8, Pin.OUT)
p = Pin(20, Pin.OUT)

d1 = Pin(15, Pin.OUT,value=1)
d2 = Pin(16, Pin.OUT,value=1)
d3 = Pin(17, Pin.OUT,value=1)
d4 = Pin(18, Pin.OUT)

btn1 = Pin(4,Pin.IN)
btn2 = Pin(3,Pin.IN)
count = 0

segments = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f,
    'g': g
}

def apagar():
    for segment in segments.values():
        segment.value(0)

def encender(num):
    apagar()
    for seg in nums[num]:
        segments[seg].value(1)
        
apagar()

while True:
    encender(count)
    if (btn1.value() == 1) and (count<9):
        apagar()
        count+=1
        sleep(0.2)
    if (btn2.value() == 1) and (count>0):
        apagar()
        count-=1
        sleep(0.2)