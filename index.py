# Gets search results based off provided information. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from airport_selector import getSelectedAirport
from greatingMessage import printGreeting
from colorama import Fore, Style
import time
# XPaths change when selected
searchBarInitial = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input"
searchBarSecondary = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div/input"
dateStart = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input"
dateEnd = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input"

printGreeting()
selectedAirport = getSelectedAirport()

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/travel/flights?hl=en-US")
    search = driver.find_element(By.XPATH, searchBarInitial)
    search.click()
    search = driver.find_element(By.XPATH, searchBarSecondary)
    search.click()
    search.send_keys(selectedAirport)
    search.send_keys(Keys.TAB)
    time.sleep(1)
    search = driver.find_element(By.XPATH, dateStart)
    # TODO Put date Here 
    search.send_keys(Keys.TAB)
    time.sleep(1)
    search = driver.find_element(By.XPATH, dateEnd)
    # TODO Put date Here 
    search.send_keys(Keys.TAB)
    time.sleep(1)    
    destination = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/div[2]/div[2]/ul[1]/li[1]/div/div[2]/div/div[2]/div[3]/span/span[2]/span/span")
    price = driver.find_element(By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/div[2]/div[2]/ul[1]/li[1]/div/div[2]/div/div[2]/div[6]/div[1]/div[2]/span")
    print("SLC => ",destination.text, "   PRICE: ", Fore.GREEN, price.text)
    print(Style.RESET_ALL)
    #driver.close()
except Exception as error:
    print(Fore.RED, "ERROR: ", error)

    

