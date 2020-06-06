from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from pages.grub_geeks_base_page import GrubGeeksBasePage

class ForumPage(GrubGeeksBasePage):
    """

    """
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.domain + "/forum"
        self.navigate()
        self.driver.implicitly_wait(5)

    def navigate(self):
        self.driver.get(self.url)

    def add_post(self, subject: str, content: str) -> bool:
        """

        :param subject: title of the subject
        :param content: content which you wish to post
        :return: whether or not the post was successful
        """
        #element locators
        add_post_button = self.driver.find_element(By.LINK_TEXT,"Add Post")

        #initiate new forum post
        add_post_button.click()

        new_post_subject = self.driver.find_element(By.XPATH, "//input[@id='subject']")
        new_post_content = self.driver.find_element(By.XPATH, "//input[@id='main_post_content']")
        new_add_post_button = self.driver.find_element(By.ID, "submit")
        #fill in forum post form
        new_post_subject.send_keys(subject)
        new_post_content.send_keys(content)
        new_add_post_button.click()

        new_forum_post_subject_link = self.driver.find_element(By.LINK_TEXT, subject)
        if new_forum_post_subject_link.is_displayed() == True:
            return True