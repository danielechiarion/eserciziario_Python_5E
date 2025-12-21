import socket
from datetime import datetime

"""Define constants for connection"""
PORT = 8080

class MeasureDay:
    """Class which define measures 
    for each day"""

    def __init__(self, date, firsTemperature, secondTemperature):
        """Constructor with the control on data conversion"""

        try:
            self.date = date
            self.firstTemperature = firsTemperature
            self.secondTemperature = secondTemperature
        except ValueError:
            raise ValueError("Conversion error")
        
    def __eq__(self, value):
        """Equals based on the date"""
        return value.date == self.date
    
    def __hash__(self):
        """Hash method to use set"""
        return hash(self.date)
    
    def __lt__(self, other):
        """Method to compare daily measurements"""
        return (max(self.firstTemperature, self.secondTemperature), self.date) < (max(other.firstTemperature, other.secondTemperature), other.date)
    

def readFromSocket(connection):
    """Read the message sent from the socket"""
    data = ""
    while True:
        chunk = connection.recv(1024)
        if not chunk:
            break
        data += chunk.decode()
    
    return data

def parseClientData(content):
    """Function to parse data sent from the client
    in order to be used"""
    try:
        arrayData = content.split(";")
        date = datetime.strptime(arrayData[0], "%d/%m/%Y")
        firstTemperature = float(arrayData[1])
        secondTemperature = float(arrayData[2])
    except ValueError as e:
        raise ValueError(e)
    
    return date, firstTemperature, secondTemperature

def returnStats(measures):
    try:
        # calculate the data
        analisedDays = len(measures)
        temperatureList = []
        
        # get the average of temperatures
        sum = 0
        for singleMeasures in measures:
            sum += singleMeasures.firstTemperature + singleMeasures.secondTemperature
            temperatureList.append(singleMeasures.firstTemperature)
            temperatureList.append(singleMeasures.secondTemperature)
        averageTemperature = sum / len(measures) / 2

        # calculate maximum and minimum
        maximumTemperature = max(temperatureList)
        minimumTemperature = min(temperatureList)
    except Exception as e:
        raise Exception(e)
    
    return analisedDays, analisedDays*2, maximumTemperature, minimumTemperature, averageTemperature

# create server connection
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', PORT))
serverSocket.listen()
print("Server started...")

while True:
    # establish a connection with the client
    connection, NULL = serverSocket.accept()
    print("Connection accepted")
    with connection:
        measures = set()
        # continue till it's interrupted
        while True:
            try:
                # if it's true it means there is a packet to add
                if bool(int(connection.recv(1).decode())):
                    clientData = connection.recv(1024).decode()
                    measures.add(MeasureDay(*parseClientData(clientData)))
                    print("Adding measure")
                    continue

                # otherwise it's time to end the connection and return the data
                response = returnStats(measures)
                connection.sendall(f"{response[0]};{response[1]};{response[2]};{response[3]};{response[4]}".encode())
                print("Send session result")
                break
            except Exception as e:
                print(e)

serverSocket.close() # close the socket