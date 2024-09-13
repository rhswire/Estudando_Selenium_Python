from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class Etapa1Page(BasePage):
    NOME = (By.ID, "nome")
    EMAIL = (By.ID, "email")
    IDADE = (By.ID, "idade")
    WHATSAPP = (By.ID, "whatsapp")
    CIDADE = (By.ID, "cidade")
    BOTAO_PROSSEGUIR = (By.XPATH, "//button")

    def preencher_etapa1(self, nome, email, idade, whatsapp, cidade):
        self.wait_for_element(self.NOME).send_keys(nome)
        self.driver.find_element(*self.EMAIL).send_keys(email) # O asterístico é para pegar o segundo elemento da tupla
        self.driver.find_element(*self.IDADE).send_keys(idade)
        self.driver.find_element(*self.WHATSAPP).send_keys(whatsapp)
        self.driver.find_element(*self.CIDADE).send_keys(cidade)
        self.driver.find_element(*self.BOTAO_PROSSEGUIR).click()