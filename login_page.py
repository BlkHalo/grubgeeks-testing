from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from pages.grub_geeks_base_page import GrubGeeksBasePage

class LoginPage(GrubGeeksBasePage):


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.domain + "/login"
        self.navigate()
        self.driver.implicitly_wait(5)

    def navigate(self):
        self.driver.get(self.url)

    def login(self, email:str, password:str):
        self.email_address_field = self.driver.find_element(By.XPATH, "//input[@id='email_address']")
        self.password_field = self.driver.find_element(By.ID, "password")
        self.submit_button = self.driver.find_element(By.ID, "submit")

        self.driver.implicitly_wait(5)
        self.email_address_field.click()
        self.email_address_field.send_keys(email)
        self.password_field.send_keys(password)
        self.submit_button.click()