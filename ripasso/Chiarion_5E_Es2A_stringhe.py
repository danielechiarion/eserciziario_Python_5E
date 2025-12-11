# function to separate characters in
# even and odd positions
def separateEvenOddCharacters(string):
    evenString = ""
    oddString = ""

    for i in range(len(string)):
        if i % 2 == 0:
            evenString += string[i]
        else:
            oddString += string[i]

    return evenString, oddString

# check if the string has doubles
def hasDoubles(string):
    doubleCharacters = set()

    for i in range (len(string)-1):
        if string[i] == string[i+1]:
            doubleCharacters.add(string[i])
    
    return doubleCharacters

# function to check which letters share
# the two strings
def commonCharacters(firstString, secondString):
    commonChars = set() # define set

    for char in firstString:
        if secondString.__contains__(char):
            commonChars.add(char)

    return commonChars

# function to compare the number of vowels between two strings
# the function will return:
# - 1 if the first string has more vowels
# - 2 if the second string has more vowels
# - 0 if the string has the same amount of vowels
def compareVowels(firstString, secondString):
    firstCount = 0
    secondCount = 0
    vowels = "aeiouAEIOU" # make a string with the vowels

    # use a single cycle to check the two strings
    for i in range(max(len(firstString), len(secondString))):
        if i < len(firstString) and vowels.__contains__(firstString[i]):
            firstCount += 1
        if i < len(secondString) and vowels.__contains__(secondString[i]):
            secondCount += 1

    if firstCount > secondCount:
        return 1
    elif firstCount < secondCount:
        return 2
    else:
        return 0 

# function to compare the number of consonants between two strings
# the function will return:
# - 1 if the first string has more consonants
# - 2 if the second string has more consonants
# - 0 if the string has the same amount of consonants
def compareConsonants(firstString, secondString):
    firstCount = 0
    secondCount = 0
    vowels = "aeiouAEIOU" # make a string with the consonants

    # use a single cycle to check the two strings
    for i in range(max(len(firstString), len(secondString))):
        if i < len(firstString) and not vowels.__contains__(firstString[i]):
            firstCount += 1
        if i < len(secondString) and not vowels.__contains__(secondString[i]):
            secondCount += 1

    if firstCount > secondCount:
        return 1
    elif firstCount < secondCount:
        return 2
    else:
        return 0       

# *** STARTING POINT OF MAIN ***
# ask to enter the first string
while True:
    firstString = input("Inserisci la prima stringa (solo lettere): ")
    # check if the string has only letters
    if not firstString.isalpha():
        print("La stringa deve contenere solo lettere\n")
    else:
        break

# ask the character to search
while True:
    charSearch = input("Inserisci la lettera da cercare nella stringa: ")
    if len(charSearch) == 0 or not charSearch.isalpha():
        print("Non hai inserito una lettera\n")
    else:
        break

# check how many times the letter is in the string
print(f"Il carattere {charSearch} è presente nella stringa {firstString} {firstString.count(charSearch)} volte\n")
# get even and odd letters and print them
evenString, oddString = separateEvenOddCharacters(firstString)
print(f"I caratteri in posizione pari sono: {evenString}\nI caratteri in posizione dispari sono: {oddString}\n")
# check if the string contains double letters
doubleCharacters = hasDoubles(firstString)
if doubleCharacters.__len__() > 0:
    print("La stringa contiene le seguenti doppie: \n")
    for char in doubleCharacters: print(char, end="\t")
    print()
else:
    print("La stringa non contiene doppie\n")

# ask for a second string
while True:
    secondString = input("Inserisci la seconda stringa (solo lettere): ")
    # check if the string has only letters
    if not secondString.isalpha():
        print("La stringa deve contenere solo lettere\n")
    else:
        break

# check which of the two strings is longer
if len(firstString) > len(secondString):
    print(f"La stringa {firstString} è più lunga di {secondString}\n")
elif len(firstString) < len(secondString):
    print(f"La stringa {secondString} è più lunga di {firstString}\n")
else:
    print("Le due stringhe hanno la stessa lunghezza\n")
# check which letters are common in the two strings
commonChars = commonCharacters(firstString, secondString)
if commonChars.__len__() > 0:
    print("Le lettere comuni alle due strighe sono:")
    for char in commonChars: print(char, end="\t")
    print()
else:
    print("Le due stringhe non hanno lettere in comune\n")

# compare the number of vowels and consonants between the two strings
vowelComparison = compareVowels(firstString, secondString)
consonantComparison = compareConsonants(firstString, secondString)

if vowelComparison == 1:
    print(f"La stringa {firstString} ha più vocali di {secondString}\n")
elif vowelComparison == 2:
    print(f"La stringa {secondString} ha più vocali di {firstString}\n")
else:
    print("Le due stringhe hanno lo stesso numero di vocali\n")

if consonantComparison == 1:
    print(f"La stringa {firstString} ha più consonanti di {secondString}\n")
elif consonantComparison == 2:
    print(f"La stringa {secondString} ha più consonanti di {firstString}\n")
else:
    print("Le due stringhe hanno lo stesso numero di consonanti\n")