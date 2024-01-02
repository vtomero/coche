
from machine import Pin,UART, PWM
from time import sleep
from coche import Coche
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

led = Pin(25, Pin.OUT) 
coche = Coche(1,2,27,26,0,28)

while True:
    
    if uart.any(): #Devulve cero si no hay nada que transmitir
        data = uart.read() #devuelve el objeto leido
        if data== b'F\r\n':                      
            led.high() 
            print("Coche Adelante")
            uart.write("LED encendido")
            for n in range(3,10):
                coche.setvelocidad(n*10000)           
                coche.irapor('ATRAS',2)               
                
           
        elif data==b'b\r\n':
            led.low()
            print("Coche Parado")
            uart.write("LED apagado")
            coche.stop()
          
