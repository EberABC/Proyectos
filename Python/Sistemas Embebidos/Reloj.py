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

displays = [d1,d2,d3,d4]

btn1 = Pin(4,Pin.IN)
btn2 = Pin(3,Pin.IN)

d_minutos, u_minutos, d_horas, u_horas = 0, 0, 0, 0
segundos = 42900
t = 1/100

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
    for display in displays:
        display.value(1)

def encender_unidades_minutos(u_minutos):
    apagar()
    for seg in nums[u_minutos]:
        segments[seg].value(1)
    d4.value(0)

def encender_decenas_minutos(d_minutos):
    apagar()
    for seg in nums[d_minutos]:
        segments[seg].value(1)
    d3.value(0)

def encender_unidades_horas(u_horas):
    apagar()
    for seg in nums[u_horas]:
        segments[seg].value(1)
    d2.value(0)

def encender_decenas_horas(d_horas):
    apagar()
    for seg in nums[d_horas]:
        segments[seg].value(1)
    d1.value(0)

while True:
    horas = int(segundos/3600)
    minutos = int((segundos - (horas*3600))/60)
    
    d_horas = int(horas/10)
    u_horas = horas - (d_horas*10)
    d_minutos = int(minutos/10)
    u_minutos = minutos - (d_minutos*10)
    
    for i in range(10):
        encender_decenas_horas(d_horas)
        sleep(1/400)
        encender_unidades_horas(u_horas)
        sleep(1/400)
        encender_decenas_minutos(d_minutos)
        sleep(1/400)
        encender_unidades_minutos(u_minutos)
        sleep(1/400)
    if segundos<86399:
        segundos += 1
    else:
        segundos = 0