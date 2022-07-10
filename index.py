from airport_selector import getSelectedAirport
from driverHandler import WebPageConductor
from greatingMessage import printGreeting
from colorama import Fore, Style
from generateDates import Dates
# Start of Call stack
printGreeting()
#selectedAirport = getSelectedAirport()
#currentScraper = WebPageConductor(selectedAirport)
print(Fore.YELLOW,"Testing with Abeid Airport")
print(Style.RESET_ALL)
#currentScraper = WebPageConductor('Abeid Amani Karume International Airport')
#currentScraper.getPricesForAirport()
datesGenerated = Dates("07122022", "09122022",7)
datesGenerated.getDays()