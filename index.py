# Start of flight scraper
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# XPaths change when selected
searchBarInitial = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input"
searchBarSecondary = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div/input"
def getAirportsFromCSV():
    # Get airports from csv file
    airports = []
    with open("largeAirports.csv") as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            airports.append(row)

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/travel/flights?hl=en-US")
    search_box = driver.find_element(By.XPATH, searchBarInitial)
    search_box.click()
    search_box = driver.find_element(By.XPATH, searchBarSecondary)
    search_box.click()
    search_box.send_keys("HONG KONG")
    #search_box = driver.find_element(By.XPATH,"//div[@aria-label='Enter your destination']//div//input[@aria-label='Where ``else?']")
    #search_box.send_keys("Hong kong")


#    search_text.send_keys(Keys.RETURN)
#    print(driver.title)
    #driver.close()
except Exception as error:
    print(bcolors.FAIL, "ERROR: ", error)

    

