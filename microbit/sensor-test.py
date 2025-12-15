# Imports go at the top
from microbit import *

# define the functionalities the microbit can do
options = (
    "Temperature",
    "Light",
    "Noise",
    "Acceleration",
    "Distance",
    "Gas"
)

def getTemperature():
    display.scroll("Temp: ")
    display.scroll(temperature())

def barra(valore, massimo):
    livelli = int((valore / massimo) * 5)
    display.clear()
    for y in range(5):
        if y >= 5 - livelli:
            for x in range(5):
                display.set_pixel(x, y, 9)

def getLight():
    barra(display.read_light_level(), 255)

def getNoise():
    barra(microphone.sound_level(), 255)

def getAcceleration():
    display.scroll("AccX: ")
    display.scroll(accelerometer.get_x())
    sleep(1000)

    display.scroll("AccY: ")
    display.scroll(accelerometer.get_y())
    sleep(1000)

    display.scroll("AccZ: ")
    display.scroll(accelerometer.get_z())
    sleep(1000)

def getDistance():
    

# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HEART)
    sleep(1000)
    display.scroll('Hello')
