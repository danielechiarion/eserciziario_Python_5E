# Imports go at the top
from microbit import *

# define the functionalities the microbit can do
options = (
    "Temperature",
    "Light",
    "Noise",
    "Acceleration",
    "Orienteering"
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

def getOrienteering():
    display.scroll(compass.heading())

# start the counter for the option
counter = 0
display.scroll(options[counter]) # display the option
while True:
    # restart counter
    if counter == len(options):
        counter = 0

    # select option by the button pressed
    if button_a.was_pressed():
        counter += 1
        display.scroll(options[counter]) # display the option
        continue
    elif button_b.was_pressed():
        display.clear()
        # if button B is pressed do the action
        if options[counter] == "Temperature":
            getTemperature()
        elif options[counter] == "Light":
            getLight()
        elif options[counter] == "Noise":
            getNoise()
        elif options[counter] == "Acceleration":
            getAcceleration()
        else:
            getOrienteering()
