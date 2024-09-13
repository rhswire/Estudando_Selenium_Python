from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

my_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=my_service, options=chrome_options)

# browser = webdriver.Firefox()

browser.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

browser.maximize_window()
title = browser.title

full_name = browser.find_element(By.XPATH, "//imput[@id='fullName']")
full_name.send_keys("Aline Pereira")

email = browser.find_element(By.NAME, "email")
email.send_keys("aline.pereira@aline.pt")

phone = browser.find_element(By.ID, "phoneNumber")
phone.send_keys("922448758")

Select(browser.find_element(By.ID, "desiredPosition")).select_by_visible_text("QA")

remote = browser.find_element(By.ID, "location1")
remote.click()

years = browser.find_element(By.NAME, "experienceYears")
years.send_keys("3")

html = browser.find_element(By.ID, "skills1")
html.click()

js = browser.find_element(By.ID, "skills3")
js.click()

# skills = browser.find_elements(By.NAME, "skill")
# # print(len("skill"))
# skills[0].click()
# skills[2].click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()

message = browser.find_element(By.ID, "successMessage").text

assert message == "Submission successful!"


sleep(20)

#browser.quit