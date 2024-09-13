from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Firefox()

browser.get("https://www.uol.com.br")

browser.maximize_window()

title = browser.title
print(title)

sleep(10)

browser.quit
