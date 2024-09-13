from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

my_service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=my_service, options=chrome_options)

# browser = webdriver.Firefox()

browser.get("https://www.google.com")

browser.maximize_window()

title = browser.title

assert title == "Google"


print(title)

sleep(3)

browser.quit
