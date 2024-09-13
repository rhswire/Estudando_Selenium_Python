from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)
    #driver.implicity_wait(10)
    driver.get("https://paulocoliveira.github.io/mypages/waits/index.html")
    driver.maximize_window()

    yield driver

    driver.quit()

    # para rodar este teste com sucesso, descomente a linha da fixture qua ativa o implicity_wait (driver.implicity_wait(10))
    def test_implicity_wait(driver):
        button = driver.find_element(By.XPATH, "//section[@id='condicional-element-section']/button")
        button.click()
        hidden_button = driver.find_elements(By.ID, "hidden-button")
        hidden_button.click()
    
    def test_file_upload(driver):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "qrcode.png")

        WebDriverWait(driver, 10).until(
            EC.present_of_element_located((By.ID, "file-upload")) # Esperar que este elemento este presente 
        )

        driver.find_element(By.ID, "file-upload").send_keys(file_path)

        driver.find_element(By.XPATH, "//button[contain(text(), 'Enviar Arquivo')]").click()

        message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "file_upload-status"))
        )

        assert  message_element.text == "Arquivo enviado"

    def test_email_sending(driver):
        send_email_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Enviar Email')]"))
        )

        send_email_button.click()

        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "email-status"), "Email enviado com sucesso")
        )

        WebDriverWait(driver, 10).until(
            EC.title_contains("sucesso")
        )

        WebDriverWait(driver, 10).until(
            EC.title_is("Email enviado com sucesso")
        )

    def test_condicional_element(driver):
        toggle_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(driver.find_element(By.XPATH, "//section[@id='condicional-element-section']/button"))
        )
        
        toggle_button.click()

        sleep(5)

        hidden_button = WebDriverWait(driver, 3).until(
            EC.visibility_of(driver.find_element(By.ID, "hidden-button"))
        )

        hidden_button.click()

        message = driver.find_element(By.ID, "message").text

        assert message =="Você interagiu com o elemento oculto!"

        sleep(3)

    def text_url_change(driver):
        current_url = driver.current_url
        print(current_url)

        change_url_button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Mudar URL')]"))
        )

        change_url_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_changes(current_url)
        )

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://paulocoliveira.github.io/mypages/waits/index.html?language=python&framework=selenium")
        )

        WebDriverWait(driver, 10).until(
            EC.url_contains("language=python&framework=selenium")
        )     

    def test_terms_of_service(driver):
        agree_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located(By.ID, "agree-button")
        )

        agree_button.click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_selected(driver.find_element(By.ID, "agree-terms"))
        ) 

        driver.find_elements(By.ID, "confirm-button").click()

        message = driver.find_elements(By.ID, "terms-message").text
        assert message == "Você concordou com os termos com sucesso."
        

