from machine import Pin, PWM
from utime import sleep

Servo = PWM(Pin(15))
Servo.freq(50)
t=1

def convertir(grados):
    return grados*65535/180

while True:
    Servo.duty_u16(convertir(180))
    sleep(t)
    Servo.duty_u16(convertir(90))
    sleep(t)
    Servo.duty_u16(convertir(0))
    sleep(t)