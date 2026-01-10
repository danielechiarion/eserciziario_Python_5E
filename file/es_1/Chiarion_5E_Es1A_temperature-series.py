import random
import json
import time

# define constants for the execution of the file
MINTEMPERATURE = -20.0
MAXTEMPEATURE = 60.0
MEASUREFREQUENCY = 3 # seconds

# productor constants
PRODUCER = "ildenielcorporation"
DEVICE = "DHT11"
MODEL = "Premium"


def get_temperature():
    """Function to get the temperature from the device.
    In this case we will use a random generated number"""

    global MINTEMPERATURE, MAXTEMPEATURE # importing global variables
    
    return round(random.uniform(MINTEMPERATURE, MAXTEMPEATURE), 1)

def main():
    """Main function to execute the temperature series"""
    global PRODUCER, DEVICE, MODEL, MEASUREFREQUENCY

    file = open("data.dbt", "w")
    
    try:
        while True:
            data = {
                "producer" : PRODUCER,
                "device" : DEVICE,
                "model": MODEL,
                "temperature": get_temperature(),
                "timestamp": int(time.time())
            }

            file.write(json.dumps(data)+"\n") # append data to file
            file.flush()

            time.sleep(MEASUREFREQUENCY) # wait for next time to measure
    except KeyboardInterrupt:
        print("Measurement interrupted by user")
        file.close()

if __name__ == "__main__":
    main()