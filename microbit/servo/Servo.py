from machine import Pin, PWM

def map_valore(x, in_min, in_max, out_min, out_max):
    """Funzione per eseguire il map di un valore da una scala
    di grandezza ad un altra"""
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

class Sensore(object):
    def __init__(self, pin:int, frequency:int):
        self.__pwm= PWM(Pin(pin))
        self.__pwm.frequency = frequency

    def move(self, angle:int):
        """Function to move the servo to a specific angle"""

        angle = max(0, min(180, angle)) # limit the angle to range 0-180
        self.__pwm.duty(map_valore(angle, 0, 180, 500000, 2500000))