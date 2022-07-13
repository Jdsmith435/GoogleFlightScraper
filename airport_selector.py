# Users will have the option to select an airport or provide start and end dates for all airports
from calendar import c
import csv
from getkey import getkey, keys
from colorama import Fore, Style
from matplotlib import style
from pynput.keyboard import Key, Listener

airports = []
keyListener = Listener()
current = 0 
selectedAirport = ''

# Gets airports from csv file 
def getAirportsFromCSV():
    # Get airports from csv file
    with open("largeAirports.csv") as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            airports.append(row[1])
            airports.sort()

def getSelectedAirport():
    if(len(airports) == 0):
        getAirportsFromCSV()
    print("Please select your destination airport:")
    print(Fore.MAGENTA, airports[0], end='\r')
    with Listener(on_press = airportConsoleSelection) as listener:   
        listener.join()
        listener.stop()
        return selectedAirport

def airportConsoleSelection(key):
    global current 
    global selectedAirport
    key = getkey()
    if key == keys.UP:
        if current < len(airports): 
            current+=1
            print("                                                                           ", end='\r')
            print(Fore.MAGENTA, airports[current], end='\r')
    elif key == keys.DOWN:
        if current > 0:
            current-=1
            print("                                                                           ", end='\r')
            print(Fore.MAGENTA, airports[current], end='\r')
    elif key == keys.ENTER:
        print(Fore.GREEN, "Selected: ", airports[current])
        print(Style.RESET_ALL)
        selectedAirport = airports[current]
        return False

  
