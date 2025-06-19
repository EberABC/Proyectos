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

columnas=[I1,I2,I3,I4,I5]
filas=[T1,T2,T3,T4,T5]


t=1
def apagar_columnas():
    for columna in columnas:
        columna.value(0)
def apagar_filas():
    for fila in filas:
        fila.value(1)

def on_columnas():
    for fila in filas:
        fila.value(0)
    for i in range(0,len(columnas)):
        apagar_columnas()
        columnas[i].value(1)
        sleep(t)
    apagar_columnas()
    for i in range(len(columnas)-1,-1,-1):
        apagar_columnas()
        columnas[i].value(1)
        sleep(t)
    for columna in columnas:
        columna.value(1)
    for fila in filas:
        fila.value(1)
    for i in range(0,len(filas)):
        apagar_filas()
        filas[i].value(0)
        sleep(t)
    apagar_filas()
    for i in range(len(filas)-1,-1,-1):
        apagar_filas()
        filas[i].value(0)
        sleep(t)
    
on_columnas()