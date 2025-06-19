from machine import Pin
from utime import sleep

I1 = Pin(15, Pin.OUT)
I2 = Pin(16, Pin.OUT)
I3 = Pin(17, Pin.OUT)
I4 = Pin(18, Pin.OUT)
I5 = Pin(19, Pin.OUT)

T1 = Pin(14, Pin.OUT, value=1)
T2 = Pin(13, Pin.OUT, value=1)
T3 = Pin(12, Pin.OUT, value=1)
T4 = Pin(11, Pin.OUT, value=1)
T5 = Pin(10, Pin.OUT, value=1)

columnas = [I1, I2, I3, I4, I5]
filas = [T1, T2, T3, T4, T5]

t = 0.001
iteraciones=10000/3

def barrido_leds():
    while True:
        for columna in columnas:
            columna.value(1)
            for fila in filas:
                fila.value(0)
                sleep(t)
                fila.value(1)
            columna.value(0)
        for fila in filas:
            fila.value(0)
            for columna in columnas:
                columna.value(1)
                sleep(t)
                columna.value(0)
            fila.value(1)

def M_off():
    for i in range(5):
        columnas[i].value(0)
        filas[i].value(1)

def diagonal():
    M_off()
    while True:
        for i in range(5):
            columnas[i].value(1)
            filas[i].value(0)
            sleep(t/100)
            columnas[i].value(0)
            filas[i].value(1)
        for i in range(4,-1,-1):
            columnas[4-i].value(1)
            filas[i].value(0)
            sleep(t/100)
            columnas[4-i].value(0)
            filas[i].value(1)

def explosion():
    while True:
        M_off()
        for x in range(iteraciones):
            columnas[2].value(1)
            filas[2].value(0)
            sleep(t/1000)
            columnas[2].value(0)
            filas[2].value(1)
        for x in range(iteraciones/8):
            for j in range(1,4):
                filas[j].value(0)
                for i in range(1,4):
                    if ((j==2) and (i==2)):
                        sleep(t/1000000)
                    else:
                        columnas[i].value(1)
                        sleep(t/1000)
                        columnas[i].value(0)
                filas[j].value(1)
        for x in range(iteraciones/16):
            for j in range(5):
                filas[j].value(0)
                for i in range(5):
                    if (((j==1 or j==2 or j==3) and (i==1 or i==2 or i==3))):
                        sleep(t/1000000)
                    else:
                        columnas[i].value(1)
                        sleep(t/1000)
                        columnas[i].value(0)
                filas[j].value(1)
    
explosion()




