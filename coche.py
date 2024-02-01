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


'''Clase sonido para el coche mediante un buzzer pasivo.
duty_u16 para el Volumen, y la frequencia para el tono'''

class Sonido:
    tiempo = 0.3
    def __init__(self, buz: int or PWM, duty = 0, freq = 500):
        if isinstance(buz, int):
            self.buz = PWM(Pin(buz))
        if isinstance(buz, PWM):
            self.buz = buz
        self.buz.freq(freq)
        self.buz.duty_u16(duty)
        
    
    def tocar(self, freq):
        self.buz.duty_u16(2000)
        self.buz.freq(freq)
    
    tones = {
        "P": "P",
        "B0": 31,
        "C1": 33,
        "CS1": 35,
        "D1": 37,
        "DS1": 39,
        "E1": 41,
        "F1": 44,
        "FS1": 46,
        "G1": 49,
        "GS1": 52,
        "A1": 55,
        "AS1": 58,
        "B1": 62,
        "C2": 65,
        "CS2": 69,
        "D2": 73,
        "DS2": 78,
        "E2": 82,
        "F2": 87,
        "FS2": 93,
        "G2": 98,
        "GS2": 104,
        "A2": 110,
        "AS2": 117,
        "B2": 123,
        "C3": 131,
        "CS3": 139,
        "D3": 147,
        "DS3": 156,
        "E3": 165,
        "F3": 175,
        "FS3": 185,
        "G3": 196,
        "GS3": 208,
        "A3": 220,
        "AS3": 233,
        "B3": 247,
        "C4": 262,
        "CS4": 277,
        "D4": 294,
        "DS4": 311,
        "E4": 330,
        "F4": 349,
        "FS4": 370,
        "G4": 392,
        "GS4": 415,
        "A4": 440,
        "AS4": 466,
        "B4": 494,
        "C5": 523,
        "CS5": 554,
        "D5": 587,
        "DS5": 622,
        "E5": 659,
        "F5": 698,
        "FS5": 740,
        "G5": 784,
        "GS5": 831,
        "A5": 880,
        "AS5": 932,
        "B5": 988,
        "C6": 1047,
        "CS6": 1109,
        "D6": 1175,
        "DS6": 1245,
        "E6": 1319,
        "F6": 1397,
        "FS6": 1480,
        "G6": 1568,
        "GS6": 1661,
        "A6": 1760,
        "AS6": 1865,
        "B6": 1976,
        "C7": 2093,
        "CS7": 2217,
        "D7": 2349,
        "DS7": 2489,
        "E7": 2637,
        "F7": 2794,
        "FS7": 2960,
        "G7": 3136,
        "GS7": 3322,
        "A7": 3520,
        "AS7": 3729,
        "B7": 3951,
        "C8": 4186,
        "CS8": 4435,
        "D8": 4699,
        "DS8": 4978,
    }
    
    cancion = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]
    
    def silencio(self):
         self.buz.duty_u16(0)
    
    def tocar_cancion(self, sonidos, tiempo):
        for nota in range(len(sonidos)):
            if self.tones[sonidos[nota]] == "P":
                self.silencio()
            else: self.tocar(self.tones[sonidos[nota]])
            sleep(tiempo)
        self.silencio()
    
    def iniciar(self, cancion):
        self.tocar_cancion(cancion)
    
    def tocar_la_cancion(self,cancion=cancion, tiempo = tiempo):
        self.tocar_cancion(cancion, tiempo)
    
    
