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
    sum = 0
    
    for i in range(len(array)):
        sum += array[i]
    return sum
        
# function to display the menu with all the choices
def displayMenu(options):
    while True:
        for i in range(len(options)):
            print((i+1), ") ", options[i], "\n")
        try:   
        	choice = int(input(""))
        
        	if choice < 1 or choice > len(options):
            	print("\nCodice non disponibile") # report the error
        	else:
            	return choice
        except ValueError:
        	print("\nVALORE NON SUPPORTATO. Hai inserito una stringa")

# *** START OF THE MAIN PROGRAM ***

array = [] # create an empty list
MINSIZEARRAY = 3 # constant for the minimum size of the array

# define all the possible options
options = (
            "Visualizza i numeri",
            "Visualizza l'array invertito",
            "Visualizza somma e media",
            "Visualizza numeri pari",
            "Visualizza numeri dispari",
            "Ricerca numero",
            "Elimina numero",
            "Alterna posizioni del vettore",
            "Ordina il vettore",
            "Esci"
    )

# ask for the size of the array checking the value
while True:
    try:
    	sizeArray = int(input("Inserisci quanti numeri vuoi generare: "))
    	if sizeArray < MINSIZEARRAY:
     	   print("Devi inserire almeno", MINSIZEARRAY, "numeri")
    	else:
    	    break
    except ValueError:
        print("\nVALORE NON SUPPORTATO. Hai inserito una stringa")

# ask for minimum and maximum numbers in the array checking them
while True:
    try:
    	minArrayNumber = int(input("Inserisci il numero minimo dell'array: "))
        break
    except ValueError:
        print("\nVALORE NON SUPPORTATO. Hai inserito una stringa")
        
while True:
    try:
    	maxArrayNumber = int(input("Inserisci il numero massimo dell'array: "))
    	if maxArrayNumber <= minArrayNumber:
        	print("Il numero massimo deve essere strettamente maggiore")
    	else:
        	break
    except ValueError:
        print("\nVALORE NON SUPPORTATO. Hai inserito una stringa")

# populate the array with the numbers and make the choice
generateArray(array, sizeArray, minArrayNumber, maxArrayNumber)

choice = 0
while choice != len(options):
    choice = displayMenu(options)

    match choice:
        # print array values
        case 1:
            print("I numeri dell'array sono:\n")
            for number in array: print(number, end="\t")
            print()
        # print reversed array
        case 2:
            print("L'array invertito è: \n")
            for number in reversed(array): print(number, end="\t")
            print()
        # print sum and average of the array
        case 3:
            sum = sumArray(array)
            print("La somma dei numeri è %d mentre la media è %.2f\n" % (sum, float(sum/len(array))))
        # print even numbers in the array
        case 4:
            print("I numeri in posizione pari sono: \n")
            for i in range(0, len(array), 2):
                print(array[i], end="\t")
            print()
        # print odd numbers in the array
        case 5:
            print("I numeri in posizione dispari sono: \n")
            for i in range(1, len(array), 2):
                print(array[i], end="\t")
            print()
        # search for a number in the array
        case 6:
            numberSearch = int(input("Inserisci il numero da cercare: "))
            try:
                print("Il numero è stato trovato in posizione", array.index(numberSearch))
            except ValueError:
                print("Il numero non è stato trovato")
        # delete a number from the array
        case 7:
            numberDelete = int(input("Inserisci il numero da eliminare: "))
            try:
                array.pop(array.index(numberDelete))
            except ValueError:
                pass # it does nothing, just to fill the tab
        # swap adjacent elements in the array
        case 8:
            for i in range(0, len(array)-1, 2):
                array[i], array[i+1] = array[i+1], array[i] # swap elements
        # sort the array
        case 9:
            array.sort()
        # exit the program
        case _:
            print("Uscita dal programma: ")