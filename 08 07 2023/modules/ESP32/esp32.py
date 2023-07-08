from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class EspMethods:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        time.sleep(3)
        self.driver.get("your IP")
        time.sleep(3)
        self.on = self.driver.find_element(By.ID,'botonEncender')
        time.sleep(3)
        self.off = self.driver.find_element(By.ID,'botonApagar')

    def on_led(self):
        self.on.click()
        # time.sleep(2)
        # driver.quit()
    
    def off_led(self):
        self.off.click()