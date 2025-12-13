import socket
import time
import logging

"""Define constants for the execution
of the program"""
ADDRESS = 'localhost'
PORT = 1234
LOGFILE = 'server.log'

logging.basicConfig(filename=LOGFILE, level=logging.DEBUG, format='%(levelname)s - %(message)s')

def readFromSocket(connection):
    """Read the message sent from the socket"""
    data = ""
    while True:
        chunk = connection.recv(1024)
        if not chunk:
            break
        data += chunk.decode()
    
    return data

def decodeString(data):
    try:
        # get the data and parse them
        dataList = data.split(';')
        deviceID = dataList[0]
        temperature = int(dataList[1])
        humidity = int(dataList[2])
        return True, deviceID, temperature, humidity
    except Exception as e:
        return False, None, None, None

def main():
    """Main function to execute the server"""
    global ADDRESS, PORT, LOGFILE

    # create the socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((ADDRESS, PORT))
    serverSocket.listen(5)

    while True:
        connection = serverSocket.accept()[0] # accept the connection
        print("Connection extablished with client\n")

        # read message from the socket and parse it
        data = readFromSocket(connection)
        result = decodeString(data)
        
        if not result[0]:
            logging.error(f"{time.time()}\tMalformed data received")
            connection.sendall("FORMATO_NON_VALIDO".encode())
            continue

        connection.sendall("OK".encode()) # send acknowledgement to the client
        logging.info(f"{time.time()}\tDevice: {result[1]}\tTemperature: {result[2]}\tHumidity: {result[3]}") # write it into the log
        print(f"{time.time()}\tDevice: {result[1]}\tTemperature: {result[2]}\tHumidity: {result[3]}\n")

        connection.close()

    serverSocket.close()


if __name__ == "__main__":
    main()