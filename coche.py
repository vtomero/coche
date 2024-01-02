from machine import UART, Pin, PWM
from time import sleep

class Coche:
    '''Iniciamos las variable, comoprueba si son un entero o un Pin. También asignamos la variable dirección y la velocidad de los motores'''
    def __init__(self, IN1: int or Pin, IN2:int or Pin, IN3: int or Pin, IN4: int or Pin, PWM1: int or Pin, PWM2: int or Pin, direccion='STOP', velocidad=50000):
        
        if isinstance(IN1, int):
            self.IN1 = Pin(IN1, Pin.OUT)
        if isinstance(IN1, Pin):
            self.IN1 = IN1
        if isinstance(IN2, int):
            self.IN2 = Pin(IN2, Pin.OUT)
        if isinstance(IN2, Pin):
            self.IN2 = IN2
        if isinstance(IN3, int):
            self.IN3 = Pin(IN3, Pin.OUT)
        if isinstance(IN3, Pin):
            self.IN3 = IN3
        if isinstance(IN4, int):
            self.IN4 = Pin(IN4, Pin.OUT)
        if isinstance(IN4, Pin):
            self.IN4 = IN4
        if isinstance(PWM1, int):
            self.PWM1=PWM(Pin(PWM1))
            self.PWM1.freq(1000)
        if isinstance(PWM1, Pin):
            self.PWM1=PWM(PWM1)
            self.PWM1.freq(1000)
        if isinstance(PWM2, int):
            self.PWM2=PWM(Pin(PWM2))
            self.PWM2.freq(1000)
        if isinstance(PWM2, Pin):
            self.PWM2=PWM(PWM2)
            self.PWM2.freq(1000)
        self.velocidad = velocidad
        self.direccion = direccion
        
    def adelante(self):
        self.IN1.value(1)
        self.IN2.value(0)
        self.IN3.value(0)
        self.IN4.value(1)
        self.PWM1.duty_u16(self.velocidad)
        self.PWM2.duty_u16(self.velocidad)
        self.direccion = 'ADELANTE'
        
    def stop(self):
        self.IN1.value(0)
        self.IN2.value(0)
        self.IN3.value(0)
        self.IN4.value(0)
        self.direccion = 'STOP'
    
    def atras(self):
        self.IN1.value(0)
        self.IN2.value(1)
        self.IN3.value(1)
        self.IN4.value(0)
        self.PWM1.duty_u16(self.velocidad)
        self.PWM2.duty_u16(self.velocidad)
        self.direccion = 'ATRAS'
    
    def izquierda(self):
        self.IN1.value(0)
        self.IN2.value(0)
        self.IN3.value(0)
        self.IN4.value(1)
        self.PWM2.duty_u16(self.velocidad)
        self.direccion = 'IZQUIERDA'
    
    def derecha(self):
        self.IN1.value(1)
        self.IN2.value(0)
        self.IN3.value(0)
        self.IN4.value(0)
        self.PWM1.duty_u16(self.velocidad)
        self.direccion = 'DERECHA'
    
    def iralantepor(self, tiempo):
        self.IN1.value(1)
        self.IN2.value(0)
        self.IN3.value(0)
        self.IN4.value(1)
        self.PWM1.duty_u16(self.velocidad)
        self.PWM2.duty_u16(self.velocidad)
        self.direccion = 'ADELANTE'
        sleep(tiempo)
        self.stop()
    
    def iratraspor(self, tiempo):
        self.IN1.value(0)
        self.IN2.value(1)
        self.IN3.value(1)
        self.IN4.value(0)
        self.PWM1.duty_u16(self.velocidad)
        self.PWM2.duty_u16(self.velocidad)
        self.direccion = 'ATRAS'
        sleep(tiempo)
        self.stop()
    
    def getvelocidad(self):
        return self.velocidad
    
    def setvelocidad(self, velocidad):
        self.velocidad=velocidad
    
    def getdireccion(self):
        return self.direccion
    
    def ira(self, direccion):
        if direccion == 'ADELANTE':
            self.adelante()
        elif direccion == 'ATRAS':
            self.atras()
        elif direccion == 'IZQUIERDA':
            self.izquierda()
        elif direccion == 'DERECHA':
            self.derecha()
        else:
            self.stop()
    
    def irapor(self, direccion, tiempo):
        if direccion == 'ADELANTE':
            self.iralantepor(tiempo)
        elif direccion == 'ATRAS':
            self.iratraspor(tiempo)
        else:
            self.stop()
        
    