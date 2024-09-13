from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    driver.get("https://paulocoliveira.github.io/mypages/validation/index.html")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_get_attibute(driver):
    page_title = driver.find_element(By.ID, "title")
    value = page_title.get_attribute("data-test")
    assert value == "testValue"

def test_is_displayed(driver):
    driver.find_element(By.ID, "toggleButton").click()
    hidden_message = driver.find_element(By.ID, "hiddenMessage")
    assert hidden_message.is_displayed()

def test_is_enabled(driver):
    input_field = driver.find_element(By.ID, "inputField")
    assert input_field.is_enabled()

def test_get_property(driver):
    checkbox = driver.find_element(By.ID, "testCheckbox")
    assert checkbox.get_property("checked") == True 
    checkbox.click()
    assert checkbox.get_property("checked") == False 

def test_is_selected(driver):
    checkbox = driver.find_element(By.ID, "testCheckbox")
    assert checkbox.test_is_selected() == True
    checkbox.click()
    assert checkbox.test_is_selected() == False

def test_value_of_css_property(driver):
    button = driver.find_element(By.ID, "toggleButton")
    print(button.value_of_ccs_property("color"))

def test_value_of_css_property_2(driver):
    button = driver.find_element(By.ID, "toggleButton")
    assert button.value_of_ccs_property("background_color") == "rgba(98, 0, 238, 1)"

# Estes testes provavelmente vai falhar na máquina de vocês, pois o tamanho de tela influencia

def test_size(driver):
    button = driver.find_element(By.ID, "testButton")
    size = button.size
    print(button.size)
    assert size["width"] == 2504 and size["height"] == 38 

def test_location(driver):
    button = driver.find_element(By.ID, "testButton")
    print(button.location)
    location = button.location
    assert location["x"] == 28 and location["y"] == 286

def test_tag_name(driver):
    button = driver.find_element(By.ID, "testButton")
    assert button.tag_name == "button"
    page_tittle = driver.find_element(By.ID, "title")
    assert page_title.tag_name == "h1"


