import tkinter
from tkinter import messagebox
import socket
from datetime import datetime

""" Define constants for the execution of the 
client socket """
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8080

# create socket to start communication with the server
try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((SERVER_ADDRESS, SERVER_PORT))
    connectionActive = True
except ConnectionRefusedError:
    messagebox.showerror("Errore", "Connessione con il server non accettata")

def readFromSocket(connection):
    """Read the message sent from the socket"""
    data = ""
    while True:
        chunk = connection.recv(1024)
        if not chunk:
            break
        data += chunk.decode()
    
    return data

def sendMeasurement():
    """Function to send measurement 
    from server to client"""
    global entryTemperatureFirst, entryTemperatureSecond, entryDate
    global SERVER_PORT, SERVER_ADDRESS, clientSocket, connectionActive

    # if the socket has not started restart it
    if not connectionActive:
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect((SERVER_ADDRESS, SERVER_PORT))
            connectionActive = True
        except ConnectionRefusedError:
            messagebox.showerror("Errore", "Connessione con il server non accettata")

    # get the date and check it
    date = entryDate.get()
    try:
        datetime.strptime(date, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Errore", "Formato data non valido")
        return
    
    # get the temperatures and try to convert them
    try:
        firstTemperature = float(entryTemperatureFirst.get())
        secondTemperature = float(entryTemperatureSecond.get())
    except ValueError:
        messagebox.showerror("Errore", "Formato numerico temperature non valido")
        return
    
    # finally send measurement with
    # the standard of communication specified
    clientSocket.sendall(str(int(True)).encode())
    clientSocket.sendall(f"{date};{firstTemperature};{secondTemperature}".encode())

def stopMeasurementSequence():
    """Function to stop measurement sequence
    from the client and send it to the server"""
    global clientSocket, connectionActive
    global textbox

    # if the connection is not active stop the function
    if not connectionActive:
        return
    
    clientSocket.sendall(str(int(False)).encode())
    # otherwise read data from server
    response = clientSocket.recv(2048).decode()
    arraystring = response.split(";")
    try:
        dayMasured = int(arraystring[0])
        measureTaken = int(arraystring[1])
        maximumTemperature = float(arraystring[2])
        minimumTemperature = float(arraystring[3])
        averageTemperature = float(arraystring[4])
    except ValueError:
        messagebox.showerror("Errore", "Errore nell'invio del formato dei dati")
        return
    
    # report the result
    textbox.insert(tkinter.END, f"Messaggio ricevuto {datetime.now()}\n")
    textbox.insert(tkinter.END, f"Giorni inseriti: {dayMasured}\tMisurazioni effettuate: {measureTaken}\tTemperatura massima: {maximumTemperature}°C\tTemperatura minima: {minimumTemperature}°C\tTemperatura media: {averageTemperature}°C\n")
    textbox.see(tkinter.END)
    # close the connection
    clientSocket.close()
    connectionActive = False

# define tkinter structure
root = tkinter.Tk()
root.title("Invio Temperature Giornaliere - Stazione meteo")
frame = tkinter.Frame(root, padx=20, pady=20)
frame.pack()

# define calendar entry
labelDate = tkinter.Label(frame, text="Inserisci la data (DD/MM/YYYY):")
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
buttonSend = tkinter.Button(frame, text="Invia misurazione", command=sendMeasurement)
buttonSend.pack()
buttonFinish = tkinter.Button(frame, text="Termina invio", command=stopMeasurementSequence)
buttonFinish.pack()

# create textbox for text and make it read-only
responseFrame = tkinter.Frame(root)
responseFrame.pack()

textbox = tkinter.Text(responseFrame, width=50, height=10)
textbox.pack()
textbox.config(state=tkinter.NORMAL)

root.mainloop()