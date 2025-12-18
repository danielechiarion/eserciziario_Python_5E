import tkinter
from tkinter import messagebox
import socket

""" Define constants for the execution of the 
client socket """
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8080

def connectToServer(follower, content):
    """Function to connect to the server with
    the socket"""
    global SERVER_ADDRESS, SERVER_PORT

    try:
        socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketClient.connect((SERVER_ADDRESS, SERVER_PORT))
        socketClient.sendall(follower.encode()) # send if the message will have any followers
        if content:
            socketClient.sendall(content.encode()) # send the possible content
    except ConnectionRefusedError as e:
        messagebox.showerror("Errore", str(e))

def sendMeasurement():
    """Function to send measurement 
    from server to client"""



# define tkinter structure
root = tkinter.Tk()
root.title("Invio Temperature Giornaliere - Stazione meteo")
frame = tkinter.Frame(root, padx=20, pady=20)

# define calendar entry
labelDate = tkinter.Label(frame, text="Inserisci la data (YYYY-MM-DD):")
labelDate.pack()
entryDate = tkinter.Entry(frame, width=30)
entryDate.pack()

# define temperature entries
labelTemperatureFirst = tkinter.Label(frame, text="Inserisci la temperatura alle ore 12: ")
labelTemperatureFirst.pack()
entryTemperatureFirst = tkinter.Entry(frame, width=30)
entryTemperatureFirst.pack()

labelTemperatureSecond = tkinter.Label(frame, text="Inserisci la temperatura alle ore 24: ")
labelTemperatureSecond.pack()
entryTemperatureSecond = tkinter.Entry(frame, width=30)
entryTemperatureSecond.pack()

# define send buttons
buttonSend = tkinter.Button(frame, text="Invia misurazione")
buttonSend.pack()
buttonFinish = tkinter.Button(frame, text="Termina invio")
buttonFinish.pack()

root.mainloop()