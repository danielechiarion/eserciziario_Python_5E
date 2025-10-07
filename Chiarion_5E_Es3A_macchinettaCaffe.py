import random
import os
import time

import tkinter as tk

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
    global currentWaterLevel, MINIMUMWATER

    # if the variable is not set
    # I generate it randomly
    if currentWaterLevel < 0:
        currentWaterLevel = random.randint(900,3001)

    return currentWaterLevel >= MINIMUMWATER

# function to check the used pods
def checkUsedPods():
    global usedPodsCounter, MINIMUMTANK

    if usedPodsCounter < 0:
        usedPodsCounter = random.randint(0, MINIMUMTANK+1)
    
    return usedPodsCounter != MINIMUMTANK

# def function to check temperature heater
def checkTemperatureHeater(canva, textID):
    DEGREESPERSECOND = 5 # define constant to increase the degrees
    global currentTemperatureHeater, HEATERTEMPERATURE

    # if there's no temperature available I generate it
    if currentTemperatureHeater < 0:
        currentTemperatureHeater = random.randint(0,HEATERTEMPERATURE+1)

    # repeat the message until the heater reaches the level
    if currentTemperatureHeater < HEATERTEMPERATURE:
        currentTemperatureHeater += DEGREESPERSECOND
        window.after(1000, lambda: checkTemperatureHeater(canva, textID)) # repeat the message with heater temperature
        canva.itemconfig(textID, text=f"Temperatura attuale: {currentTemperatureHeater}°C")
    else:
        canva.itemconfig(textID, text="Temperatura raggiunta")

# *** FUNCTIONS WITH ELEMENTS OF Tkinter ***
# define tkinter environment
window = tk.Tk()
window.geometry("600x600")
window.title("Macchinetta caffè")
window.resizable(True, True)
window.configure(background="white")

def createButton(master, string, value):
    btn = tk.Button(master, text=string,
                bg="lightgray",
                fg="black",
                activebackground="gray",
                activeforeground="white",
                relief="raised",
                bd=3,
                width=2,
                height=1,
                font=("Arial",20)
        )

    return btn

def createRowButtons(master, numberButtons, rows, columns):
    # variable declaration
    buttonGrid = []
    index = 0 

    # create a cicle to create the buttons
    for currentRow in range(rows):
        row = []

        for currentColumn in range(columns):
            if index >= numberButtons:
                return buttonGrid

            
            currentButton = createButton(master, str(index+1), index)
            currentButton.grid(row=currentRow, column=currentColumn, padx=10, pady=10)
            row.append(currentButton)

            index += 1

        buttonGrid.append(row)

    return buttonGrid

def createDisplay():
    global window
    frame_display = tk.Frame(window)
    frame_display.pack(pady=20)

    canva = tk.Canvas(frame_display, bg="blue", width=300, height=80, highlightthickness=0)
    canva.grid(row=0, column=0, columnspan=3, rowspan=2)

    textId = canva.create_text(150,40,text="", font=("Terminal", 16), fill="white")

    return canva, textId

# *** START OF MAIN PROGRAM ***
# insert the display of the machine
display, textID = createDisplay()

# create a frame for the buttons
buttonFrame = tk.Frame(window, bg="white")
buttonFrame.pack(pady=20)
createRowButtons(buttonFrame, 9,3,3)

# define the message for temperature heater
# and check the temperature
messageTemperature = tk.Label(text="")
messageTemperature.pack(pady=20)
checkTemperatureHeater(display,textID)

window.mainloop()