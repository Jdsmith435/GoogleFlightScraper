from airport_selector import getSelectedAirport
from driverHandler import WebPageConductor
from greatingMessage import printGreeting
from colorama import Fore, Style
from generateDates import Dates

# Start of Call stack
printGreeting()
#selectedAirport = getSelectedAirport()
selectedAirport = "LAX"
dateObject = Dates("220719", "221012")
currentScraper = WebPageConductor(dateObject)
currentScraper.getPricesForAirport(selectedAirport, "slc")
print(Fore.YELLOW,"Testing with AAA")
print(Style.RESET_ALL)

#currentScraper = WebPageConductor('Abeid Amani Karume International Airport')
#currentScraper.getPricesForAirport(datesGenerated.getDays())