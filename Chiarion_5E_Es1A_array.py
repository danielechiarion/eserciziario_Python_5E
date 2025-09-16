import random

# function to generate a random number between a minimum and maximum value
def generateNumber(min, max):
    return random.randint(min, max)
    
# function to populate an array with random numbers
def generateArray(array, size, minNumber, maxNumber):
      for i in range(size):
          array.append(generateNumber(minNumber, maxNumber))

# function to sum the elements in an array
def sumArray(array):
    sum = 0;
    
    for i in range(len(array))
        sum += array[i]
        
# function to display the menu with all the choices
def displayMenu(options)
    choice = 1; # initialise the variable
    
    while choice < 1 || choice > len(options):
        for i in range(len(options)):
            print((i+1), " ", options[i])
        choice = int(input(""))
        
        if choice < 1 || choice > len(options)
