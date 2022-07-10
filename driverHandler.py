# Gets search results based off provided information. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from colorama import Fore, Style
import time

class WebPageConductor: 
    googleFlightsURL    = "https://www.google.com/travel/flights?hl=en-US"

    def __init__(self, airport:str):
        self.destAirport = airport

    # Searches a single airport over a certain date range
    def getPricesForAirport(self):

        options = Options()
        # Doesn't open gui
        # options.add_argument('--headless')

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(self.googleFlightsURL)
            flightDestination = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Where to?']")
            printState("Selected placeholder Where to?", "\r")
            flightDestination.click()
            flightDestination = driver.find_element(By.CSS_SELECTOR, "input[aria-describedby='i22']")
            printState("Selected placeholder Where else?","\r")
            flightDestination.click()
            flightDestination.clear()
            flightDestination.send_keys(self.destAirport)
            printState("Sending Keys Destination Airport pt 2","\r")
            
            time.sleep(12)

            #flightDestination.send_keys(Keys.TAB)
         
            
            #startDate = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Departure']")
            #startDate.send_keys("Mon, Jul 18")
            # search.click()
            # time.sleep(15)
            # search = driver.find_element(By.XPATH, searchBarSecondary)
            # search.click()
            # search.send_keys(selectedAirport)
            # search.send_keys(Keys.TAB)
            # time.sleep(1)
            # search = driver.find_element(By.XPATH, dateStart)
            # # TODO Put date Here 
            # search.send_keys(Keys.TAB)
            # time.sleep(1)
            # search = driver.find_element(By.XPATH, dateEnd)
            # # TODO Put date Here 
            # search.send_keys(Keys.TAB)
            # time.sleep(1)    
            # destination = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/div[2]/div[2]/ul[1]/li[1]/div/div[2]/div/div[2]/div[3]/span/span[2]/span/span")
            # price = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/div[2]/div[2]/ul[1]/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span")
            # print("SLC => ",destination.text, "   PRICE: ", Fore.GREEN, price.text)
            # print(Style.RESET_ALL)
            #driver.close()
        except Exception as error:
            print(Fore.RED, "ERROR: ", error)

def printState(state, end):
    print("                                                                           ", end=end)
    print(Fore.BLUE, state, end=end)