from selenium.webdriver.firefox.webdriver import WebDriver
from pages.grub_geeks_base_page import GrubGeeksBasePage
from selenium.webdriver.common.by import By


class RegisterPage(GrubGeeksBasePage):
    """
    Class representation of the Register Page /register
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.domain + "/register"

    def navigate(self):
        """

        :return:
        """
        self.driver.get(self.url)

    def register_new_user(self,
                          email:str,
                          username: str,
                          password: str):
        """

        :param email:
        :param username:
        :param password:
        :return:
        """
        email_input = self.driver.find_element(By.ID, "email_address")
        username_input = self.driver.find_element(By.ID, "user_name")
        password_input = self.driver.find_element(By.ID, "password")
        confirm_input = self.driver.find_element(By.ID, "pass_confirm")
        register_button = self.driver.find_element(By.ID, "submit")

        self.driver.implicitly_wait(5)
        email_input.send_keys(email)
        username_input.send_keys(username)
        password_input.send_keys(password)
        # send same password to the confirm input
        confirm_input.send_keys(password)

        register_button.click()
