import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


with open ("config.json", "r") as f:
    config = json.load(f)

email = config["email"]
password = config["password"]
keywords = config["keywords"]
location = config["location"]

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/login")
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3856977850&keywords=austin%20texas%20software&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")

try:
    login_email = driver.find_element(By.NAME, "session_key")
    login_email.send_keys(email)
    
    login_pass = driver.find_element(By.NAME, "session_password")
    login_pass.send_keys(password)
    login_pass.send_keys(Keys.RETURN)

    # time.sleep(15)
    # go to jobs tab
    wait = WebDriverWait(driver, 10)

# Wait until the Jobs link is clickable
    jobs_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Jobs")))    
    jobs_link.click()
    time.sleep(2)

    search_keywords = driver.find_element(By. CLASS_NAME, "jobs-search-box__text-input")
    search_keywords.send_keys(keywords)
    search_keywords.send_keys(Keys.SPACE)

    search_location = driver.find_element(By.CLASS_NAME, "jobs-search-box__ghost-text-input")
    search_keywords.send_keys(location)
    time.sleep(2)
    search_keywords.send_keys(Keys.ENTER)
    time.sleep(3)

   
    autoapplybutton = driver.find_element(By.XPATH, "//*[text()='Easy Apply']")
    autoapplybutton.click()
    time.sleep(50)


#     number = 1
#     while True:
#         try:
#             element_id = "ember{number}"
#             element = driver.find_element(By.ID, element_id)
#             print(f"Found element with ID: {element_id}")
#             number += 1
#         except NoSuchElementException:
#             print(f"Element with ID: {element_id} not found, stopping the loop.")
#             number +=1

#     time.sleep(90)
#     driver.close

except Exception as e:
    print (e)
    driver.close