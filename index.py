# Gets search results based off provided information. 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from airport_selector import getSelectedAirport
from greatingMessage import printGreeting
from console_output import bcolors

# XPaths change when selected
searchBarInitial = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input"
searchBarSecondary = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div/input"
dateStart = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/input"
dateEnd = "/html/body/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input"

printGreeting()
getSelectedAirport()

# try:
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.google.com/travel/flights?hl=en-US")
#     search = driver.find_element(By.XPATH, searchBarInitial)
#     search.click()
#     search = driver.find_element(By.XPATH, searchBarSecondary)
#     search.click()
#     search.send_keys("HONG KONG")
#     search.send_keys(Keys.TAB)
#     search = driver.find_element(By.XPATH, dateStart)
#     # TODO Put date Here 
#     search.send_keys(Keys.TAB)
#     search = driver.find_element(By.XPATH, dateEnd)
#     # TODO Put date Here 
#     search.send_keys(Keys.TAB)
#     #driver.close()
# except Exception as error:
#     print(bcolors.FAIL, "ERROR: ", error)

    

