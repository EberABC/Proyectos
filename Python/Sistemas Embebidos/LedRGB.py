from machine import Pin
from time import sleep

R=Pin(9,Pin.OUT,value=0)
G=Pin(10,Pin.OUT,value=0)
B=Pin(11,Pin.OUT,value=0)
t=1

def Red():
    R.value(0)
    G.value(1)
    B.value(1)

def Yellow():
    R.value(0)
    G.value(1)
    B.value(0)
    
def Green():
    R.value(1)
    G.value(1)
    B.value(0)

def Blue():
    R.value(1)
    G.value(0)
    B.value(1)

def Cyan():
    R.value(1)
    G.value(0)
    B.value(0)

def Purple():
    R.value(0)
    G.value(0)
    B.value(1)

def White():
    R.value(0)
    G.value(0)
    B.value(0)

def Black():
    R.value(1)
    G.value(1)
    B.value(1)

while True:
    Red()
    sleep(t)
    Yellow()
    sleep(t)
    Green()
    sleep(t)
    Blue()
    sleep(t)
    Cyan()
    sleep(t)
    Purple()
    sleep(t)
    White()
    sleep(t)
    Black()
    sleep(t)
    print("Ejecutando.")