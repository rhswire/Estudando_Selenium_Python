from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):                  # Método construtor
        self.driver = driver
        self.base_url = "https://paulocoliveira.github.io/mypages/patterns/index.html"
    
    def open_site(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def wait_for_element(self, locator, timeout=10):
       return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((locator))
       )

    