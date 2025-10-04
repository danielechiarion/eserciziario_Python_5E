import random
import os
import time

import tkinter as tk

# define tkinter environment
window = tk.Tk()
window.geometry("600x600")
window.title("Macchinetta caffè")
window.resizable(True, True)
window.configure(background="black")


# define the class for beverages
class Beverage:
    # constructor
    def __init__(self, name, waterAmount):
        # control if the attributes have the right value
        if not isinstance(name, str):
            raise TypeError("Name is expected as a string")
        if not isinstance(waterAmount, int):
            raise TypeError("Water amount is expected as an integer")

        # assign the attributes
        self.name = name
        self.waterAmount = waterAmount
        
    # equals method
    def __eq__(self, another):
        # check if the object is instance of Beverage
        if not isinstance(another, Beverage):
            raise TypeError("The compared object in the equals of a Beverage must be a beverage")
        
        # return the condition
        return self.name == another.name
    
# define the different beverages for the machine
beverages = (
    Beverage("Caffe", 30),
    Beverage("Cappuccino", 120),
    Beverage("Tè", 150),
    Beverage("Cioccolata", 120),
    Beverage("Orzo", 80)
)

# define the constants for the machine
HEATERTEMPERATURE = 60 # expressed in °C
MINIMUMWATER = 1000 # expressed in mL
MINIMUMTANK = 10 # minimum quantity of pods in the tank
WATERRELEASESPEED = 5 # mL of water released per second

# define global variables
currentTemperatureHeater = -1
currentWaterLevel = -1
usedPodsCounter = -1

# method to clear screen
def clrScr():
    for widget in window.winfo_children():
        widget.destroy()

# check the level of the water
def checkWaterLevel():
    # if the variable is not set
    # I generate it randomly
    if currentWaterLevel < 0:
        currentWaterLevel = random.randint(900,3001)

    return currentWaterLevel >= MINIMUMWATER

# function to check the used pods
def checkUsedPods():
    if usedPodsCounter < 0:
        usedPodsCounter = random.randint(0, MINIMUMTANK+1)
    
    return usedPodsCounter != MINIMUMTANK

# def function to check temperature heater
def checkTemperatureHeater():
    DEGREESPERSECOND = 5 # define constant to increase the degrees

    # if there's no temperature available I generate it
    if currentTemperatureHeater < HEATERTEMPERATURE:
        currentTemperatureHeater = random.randint(0,HEATERTEMPERATURE+1)

    # repeat the messag

# *** START OF MAIN PROGRAM ***
window.mainloop()