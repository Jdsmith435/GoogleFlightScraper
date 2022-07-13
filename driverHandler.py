# Gets search results based off provided information. 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from colorama import Fore, Style
from selenium.webdriver.common.keys import Keys
import time

class WebPageConductor: 
    
    def __init__(self, dateObject):
        self.dateObject = dateObject
    #            https://www.google.com/travel/flights?q=Flights%20to%20AAA%20from%20slc%20on%202022-10-01%20through%202022-10-12
    #            https://www.google.com/travel/flights?q=Flights%20to%20SFO%20from%20HNL%20on%202022-09-13%20through%202022-09-17
    def generateURLRequest(self, destCode, origCode, startDate, endDate): 
        return ("https://www.google.com/travel/flights?q=Flights%20to%20" + destCode + "%20from%20" + origCode + "%20on%20"+startDate+"%20through%20"+endDate)

    # Searches a single airport over a certain date range
    def getPricesForAirport(self, destCode, origCode):
        options = Options()
        # Doesn't open gui
        # options.add_argument('--headless')
        #for endDate in self.dateObject.getDays():
           #print(endDate)

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(self.generateURLRequest(destCode,origCode,self.dateObject.startDayGetter(),self.dateObject.endDayGetter()))

            time.sleep(12)

            #flightInput.send_keys(Keys.TAB)
         
            
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