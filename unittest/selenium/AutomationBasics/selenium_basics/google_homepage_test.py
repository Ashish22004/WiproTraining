from selenium import webdriver
from selenium.webdriver.ie.service import Service



class EdgeChromeiumDriverManager:
    def install(self):
        print("Google Homepage Loaded")
        pass


driver = webdriver.Edge(service = Service(EdgeChromeiumDriverManager().install()))

driver.get("https://www.google.com")


