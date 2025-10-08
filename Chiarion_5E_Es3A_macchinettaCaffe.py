import random, math
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
MAXIMUMTANK = 10 # minimum quantity of pods in the tank
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
    global usedPodsCounter, MAXIMUMTANK

    if usedPodsCounter < 0:
        usedPodsCounter = random.randint(0, MAXIMUMTANK+1)
    
    return usedPodsCounter != MAXIMUMTANK

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
        window.after(1000, configureMenu)
        window.after(100, enableButtons)

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
                font=("Arial",20),
                command=lambda: pressNumber(value+1),
                state="disabled"
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
    global rightFrame
    frame_display = tk.Frame(rightFrame)
    frame_display.pack(pady=20)

    canva = tk.Canvas(frame_display, bg="blue", width=300, height=80, highlightthickness=0)
    canva.grid(row=0, column=0, columnspan=3, rowspan=2)

    textId = canva.create_text(150,40,text="", font=("Terminal", 16, "bold"), fill="white")

    return canva, textId

def createBeverageLabel(master, number, name):
    # canvas of the label
    canvas = tk.Canvas(master, bg="black", width=200, height=50, highlightthickness=0)

    # circle with number
    circle_d = 24
    circle_x = 10
    circle_y = 13
    canvas.create_oval(circle_x, circle_y, circle_x + circle_d, circle_y + circle_d,
                       fill="white", outline="orange", width=2)

    # centre the number
    canvas.create_text(circle_x + circle_d / 2, circle_y + circle_d / 2,
                       text=str(number), font=("Courier", 12, "bold"))

    # text of the beverage next to the number
    canvas.create_text(circle_x + circle_d + 15, circle_y + circle_d / 2,
                       text=name, anchor="w", font=("Courier", 14, "bold"), fill="white")

    return canvas

def createBeverageGrid(master, number):
    # create variables and lists
    beverageGrid = []
    index = 0

    for currentRow in range(math.ceil(number/2)):
        row = []
        for currentColumn in range(2):
            if index >= number:
                return beverageGrid
            
            currentLabel = createBeverageLabel(master, index+1, beverages[index].name)
            currentLabel.grid(row=currentRow, column=currentColumn, padx=10, pady=10)
            row.append(currentLabel)
            index += 1

        beverageGrid.append(row)

def updateDisplay():
    global changingValue, fixedMessage, display, textID

    currentText = fixedMessage + changingValue
    display.itemconfig(textID, text=currentText)

def pressNumber(num):
    global changingValue
    changingValue += str(num) # add the value
    updateDisplay() # update the display

def pressEnter():
    global changingValue
    number = int(changingValue)

    return 1 <= number <= len(beverages)
    
def enableButtons():
    global buttonGrid, enterButton

    for currentRow in buttonGrid: 
        for currentButton in currentRow: 
            currentButton.config(state="normal") # change the state of the button
    enterButton.config(state="normal")

def configureMenu():
    global display, textID
    global fixedMessage

    fixedMessage = "Seleziona una bevanda: "
    display.itemconfig(textID, text=fixedMessage)

def checkResult(value):
    global display, textID
    global changingValue

    # control if the value if enough to proceed
    if not value:
        changingValue = ""
        display.itemconfig(textID, text="Valore non valido, riprova")
        return
    
    indexBeverage = int(changingValue)-1
    preparationTime = math.ceil(float(beverages[indexBeverage].waterAmount / WATERRELEASESPEED)) # calculate time
    window.after(300, lambda: displayRemainingTime(preparationTime))
    

def displayRemainingTime(preparationTime):
    global fixedMessage, changingValue

    fixedMessage = "Tempo rimasto: "
    updateDisplay()

    if preparationTime > 0:
        changingValue = f"{preparationTime}s"
        updateDisplay()
        window.after(1000, lambda: displayRemainingTime(preparationTime - 1))
    else:
        fixedMessage = "Bevanda pronta!"
        changingValue = ""
        updateDisplay()
        window.after(1000, controlMachineCondition)
        window.after(2000, configureMenu)

def controlMachineCondition():
    global fixedMessage, changingValue
    global display, textID
    changingValue = ""
    status = True

    if not checkWaterLevel():
        fixedMessage = "Acqua non sufficiente"
        window.after(100, updateDisplay)
        return
    if not checkUsedPods():
        fixedMessage = "Serbatoio cialde usate pieno"
        window.after(1000, updateDisplay)
        return
    
    checkTemperatureHeater(display, textID)

# *** START OF MAIN PROGRAM ***
# create mainFrame for all the things
mainFrame = tk.Frame(window, bg="white")
mainFrame.pack(padx=20, pady=20)

# define the list of beverages to use
beverageFrame = tk.Frame(mainFrame, bg="white")
beverageFrame.pack(side="left", pady=20)
createBeverageGrid(beverageFrame, len(beverages))

# create frame for the right part of the machine, including display and numbers
rightFrame = tk.Frame(mainFrame, bg="white")
rightFrame.pack(side="right", pady=20, padx=60)

# insert the display of the machine
display, textID = createDisplay()

# create a frame for the buttons
buttonFrame = tk.Frame(rightFrame, bg="white")
buttonFrame.pack(pady=20)
buttonGrid = createRowButtons(buttonFrame, 9,3,3)
# add enter button
enterButton = tk.Button(buttonFrame, text="Invio",
                bg="lightgray",
                fg="black",
                activebackground="gray",
                activeforeground="white",
                relief="raised",
                bd=3,
                width=6,
                height=1,
                font=("Arial",20),
                command= lambda: checkResult(pressEnter()),
                state = "disabled"
        )
enterButton.grid(pady=20, columnspan=3)

# define the message for temperature heater
# and check the temperature
# check also the other condition
fixedMessage = "Avvio macchina..."
window.after(300, controlMachineCondition())

# CHOOSING THE BEVERAGE FROM THE LIST
changingValue = "" # use a global variable for the value to use

window.mainloop()