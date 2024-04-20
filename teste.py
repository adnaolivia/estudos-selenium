from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver() # instancia o driver
browser = Firefox() # instancia o firefox

class teste_selenium():

    barra_pesquisa_locator = driver.find_element(By.CSS_SELECTOR,"#APjFqb") # retornou NoSuchElement ://

    def abrir_firefox(self):
        url = 'https://google.com/'
        browser.get(url)
    
    def fazer_pesquisa(self):
        fazer_pesquisa = driver.find_element(*self.barra_pesquisa_locator)
        fazer_pesquisa.send_keys("youtube" + Keys.ENTER)