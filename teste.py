from selenium.webdriver import Firefox
from selenium import webdriver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

url = 'https://duckduckgo.com/'
browser = Firefox()
browser.get(url)