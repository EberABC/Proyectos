from machine import Pin, PWM
from utime import sleep

R=PWM(Pin(9),freq=1000)
G=PWM(Pin(10),freq=1000)
B=PWM(Pin(11),freq=1000)
t=1

def Color1():
    R.duty_u16(63479)#F7FF01 Amarillo #0-65535   Para ESP32 se usa .duty(4096) 0-4096
    G.duty_u16(65535)
    B.duty_u16(257)

def Color2():
    R.duty_u16(7967)#1FDFFF Cyan
    G.duty_u16(57311)
    B.duty_u16(65535)
    
def Color3():
    R.duty_u16(65535)#FF2585 Rosa
    G.duty_u16(9509)
    B.duty_u16(34181)

def Color4():
    R.duty_u16(48059)#BBFFC1 Verde pastel
    G.duty_u16(65535)
    B.duty_u16(49601)

def Color5():
    R.duty_u16(65535)#FFCBD6 Rosa pastel
    G.duty_u16(52171)
    B.duty_u16(54998)

def Color6():
    R.duty_u16(65535)#FF5959 Rojo claro
    G.duty_u16(22873)
    B.duty_u16(22873)

def Color7():
    R.duty_u16(51143)#C798FF Morado pastel
    G.duty_u16(39064)
    B.duty_u16(65535)

def Color8():
    R.duty_u16(65535)#FFF556 Amarillo claro
    G.duty_u16(62965)
    B.duty_u16(22102)

def Color9():
    R.duty_u16(65535)#FFD9BD Crema
    G.duty_u16(55769)
    B.duty_u16(48573)

def Color10():
    R.duty_u16(65535)#FFB1B6 Rosa claro
    G.duty_u16(45489)
    B.duty_u16(46774)
    
def apagar():
    R.duty_u16(0)
    G.duty_u16(0)
    B.duty_u16(0)
    
while True:
    apagar()
    sleep(t)
    Color1()
    sleep(t)
    Color2()
    sleep(t)
    Color3()
    sleep(t)
    Color4()
    sleep(t)
    Color5()
    sleep(t)
    Color6()
    sleep(t)
    Color7()
    sleep(t)
    Color8()
    sleep(t)
    Color9()
    sleep(t)
    Color10()
    sleep(t)