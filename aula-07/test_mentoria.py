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
from pages.base_page import BasePage
from pages.etapa1_page import Etapa1Page

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    my_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=my_service, options=chrome_options)

    BasePage(driver).open_site()

    yield driver

    driver.quit()

def test_complete_registration1(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("Zélia Silva", "zelia@silva.pt", "15", "+351998754255", "Gondomar")

    sleep(5)

def test_complete_registration2(driver):
    etapa1 = Etapa1Page(driver)
    etapa1.preencher_etapa1("Diana Neves", "diana@neves.pt", "12", "+351998758877", "Porto")