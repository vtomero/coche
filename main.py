
from machine import Pin,UART, PWM
from time import sleep
from coche import Coche
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

led = Pin(25, Pin.OUT) 
coche = Coche(1,2,27,26,0,28)

while True:
    
    if uart.any(): #Devuelve 0 sino hay datos que mandar
        data = uart.read() #devuleve el objeto con la lectura de los datos        
        if data== b'f\r\n' or data ==b'f':                      
            led.high() 
            print("Coche Adelante")
            uart.write("LED encendido")
            coche.adelante()
        elif data== b'a\r\n' or data ==b'a':
            led.high()
            print("Coche Atrás")
            uart.write("LED encendido")
            coche.atras()              
        elif data== b'i\r\n' or data ==b'i':
            led.high()
            print("Coche a la Izquierda")
            uart.write("LED encendido")
            coche.izquierda()
        elif data== b'd\r\n' or data ==b'd':
            led.high()
            print("Coche a la Derecha")
            uart.write("LED encendido")
            coche.derecha() 
        elif data== b's\r\n' or data ==b's':
            led.low()
            print("Coche Parado")
            uart.write("LED apagado")
            coche.stop()
          

