import socket
import random
import time

"""Define constants for the execution of
the client socket"""
DEVICE_ID = "Sensor_01"
TIME_WAIT = 10
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 1234

def getMeasures():
    """Simulate getting some measurement 
    from the sensor"""
    TEMPERATUREMINRANGE = -10
    TEMPERATUREMAXRANGE = 50
    HUMIDITYMINRANGE = 0
    HUMIDITYMAXRANGE = 100

    temperature = random.randint(TEMPERATUREMINRANGE, TEMPERATUREMAXRANGE)
    humidity = random.randint(HUMIDITYMINRANGE, HUMIDITYMAXRANGE)

    return temperature, humidity

def formatMessage(temperature, humidity):
    """Format the message so as to send
    it to the server"""
    global DEVICE_ID 

    return f"{DEVICE_ID};{temperature};{humidity}"

def testConnection(clientSocket):
    """Test the connection to the server for
    a maximum of five tries"""
    for i in range(5):
        try:
            clientSocket.connect((SERVER_ADDRESS, SERVER_PORT))
            print("Connection to server successful\n")
            return True
        except ConnectionRefusedError:
            print("Connection refused, retrying...")
            time.sleep(1)
    
    return False

def readFromSocket(connection):
    """Read the message sent from the socket"""
    data = ""
    while True:
        chunk = connection.recv(1024)
        if not chunk:
            break
        data += chunk.decode()
    
    return data

def main():
    """Main function for the client socket execution"""
    global TIME_WAIT

    # create an infinite loop
    while True:
        # create a tcp/ip socket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # make a cycle for five maximum tries of connection to the client server
        if(not testConnection(clientSocket)):
            print("Could not connect to server, send operation aborted\n")

        # get measures and send to the server
        temperature, humidity = getMeasures()
        clientSocket.sendall(formatMessage(temperature, humidity).encode())
        clientSocket.shutdown(socket.SHUT_WR) 

        # print confirmation and close the socket
        print(f"Sent data to server: Temperature={temperature}, Humidity={humidity}\n")

        # read data from the server
        response = readFromSocket(clientSocket)
        if response == "OK":
            print("Data sent correctly\n")
        elif response == "FORMATO_NON_VALIDO":
            print("Error in the format\n")
        else:
            print("Unknown return code\n")

        clientSocket.close()

        time.sleep(TIME_WAIT) # sleep for the TIME_WAIT given

if __name__ == "__main__":
    main()