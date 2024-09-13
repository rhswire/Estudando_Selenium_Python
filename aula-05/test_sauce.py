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
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_mandatory_scenario(driver):
    
    # Login
    title = driver.title
    assert title == "Swag Labs"

    assert driver.current_url == "https://www.saucedemo.com/"

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
   
    driver.find_element(By.XPATH, "//input[@name='login-button']").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


    product_title_element = driver.find_element(By.XPATH, "//span[@data-test='title']").text
    assert product_title_element == "Products"

    products = driver.find_elements(By.XPATH, "//button[contains(@id,'add-to-cart')]")

    for product in products:
        product.click()

    # Verificar se os 6 Itens estão no carrinho

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "6"

    # Ir para o carrinho

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Remover um produto

    driver.find_element(By.XPATH, "//*[@id='remove-test.allthethings()-t-shirt-(red)']").click()
   
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "5"

    #Ir para o Checkout

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    # Preencher os campos

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Carla")

    last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
    last_name.send_keys("Silva")

    postal_code = driver.find_element(By.NAME, "postalCode")
    postal_code.send_keys("2090-255")

    #Continuar para o Checkout Overview

    continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
    continue_button.click()

    # Fizalizar a compra

    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()

    # confirmation_ message = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").text
    # assert confirmation_ message == "Thank you for your order!"

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation_message == "Thank you for your order!"

    sleep(3)

def test_price_sorting(driver):

    # Login

    title = driver.title
    assert title == "Swag Labs"

    assert driver.current_url == "https://www.saucedemo.com/"

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
   
    driver.find_element(By.XPATH, "//input[@name='login-button']").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


    product_title_element = driver.find_element(By.XPATH, "//span[@data-test='title']").text
    assert product_title_element == "Products"

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_visible_text("Price(low to high)")

    sleep(3)

    products_price = driver.find_elements(By.CLASS_NAME, "inventory_itens_price")

    prices = []

    for product in products_price:
        price = product.text
        print(price)
        price = price.replace("$", "")
        price = float(price) # transformar texto em 
        prices.append(price) # criar uma lista

        print(prices)

        sorted_prices = sorted(prices)

        print(sorted_prices)

        assert prices == sorted_prices


def test_locker_user(driver):

     # Login
    title = driver.title
    assert title == "Swag Labs"

    assert driver.current_url == "https://www.saucedemo.com/"

    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.send_keys("locked_out_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.XPATH, "//input[@name='login-button']")
    button.click()

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert error_message =="Epic sadface: Sorry, this user has been locked out."

def test_total_price(driver):
  
    # Login
    title = driver.title
    assert title == "Swag Labs"

    assert driver.current_url == "https://www.saucedemo.com/"

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
   
    driver.find_element(By.XPATH, "//input[@name='login-button']").click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


    product_title_element = driver.find_element(By.XPATH, "//span[@data-test='title']").text
    assert product_title_element == "Products"

    products = driver.find_elements(By.XPATH, "//button[contains(@id,'add-to-cart')]")

    for product in products:
        product.click()

    products_price = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    total = 0

    for product in products_price:
        price = product.text
        price = price.replace("$","")
        price = float(price) 
        total = total + price 


     # Ir para o carrinho

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    #Ir para o Checkout

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    # Preencher os campos

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Carla")

    last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
    last_name.send_keys("Silva")

    postal_code = driver.find_element(By.NAME, "postalCode")
    postal_code.send_keys("2090-255")

    #Continuar para o Checkout Overview

    continue_button = driver.find_element(By.XPATH, "//input[@data-test='continue']")
    continue_button.click()
    
    total_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
 
    total_list = total_price.split('$')
    total_value = total_list[1]
    total_value_float = float(total_value)
  

    assert total == total_value_float
