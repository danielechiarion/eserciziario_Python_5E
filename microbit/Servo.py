# Imports go at the top
from microbit import *

class Sensore(object):
    def __init__(self, pin:int, period:int):
        self.__pin = pin
        self.__period = period

    def move(self, angle:int):
        