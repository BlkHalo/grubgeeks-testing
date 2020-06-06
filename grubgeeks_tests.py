from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

from pages.forum_page import ForumPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestRegistration:
    """

    """
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Any common test setups that are needed for all tests.
        """
        self.driver = WebDriver()
        self.registration_page = RegisterPage(driver=self.driver)
        self.login_page = LoginPage(driver=self.driver)
        self.forum_page = ForumPage(driver=self.driver)
        yield self.registration_page
        self.driver.quit()

    @pytest.fixture(autouse=False)
    def random_email(self) -> str:
        unique_int = datetime.today().now().strftime("%Y%m%d%H%M%S")
        return "lexie"+ unique_int +"@cats.com"

    @pytest.fixture(autouse=False)
    def unique_post(self):
        unique_string = datetime.today().now().strftime("%Y%m%d%H%M%S")
        return "post title: " + unique_string

    @pytest.fixture(autouse=False)
    def new_user(self, random_email) -> tuple:
        """
        creates a new user. insert randomness if this to be used on a consistent basis by a test.
        """
        new_user_email = random_email
        new_user_password = "123fish"

        self.registration_page.navigate()
        self.registration_page.register_new_user(email=new_user_email,
                                                 username=new_user_email,
                                                 password=new_user_password)

        return (new_user_email, new_user_password)

    @pytest.fixture(autouse=False)
    def existing_user(self) -> tuple:
        return ("lexie5@cats.com", "123fish")

    @pytest.fixture()
    def login_as_new_user(self, new_user) -> str:
        """

        :param new_user: a fixture to generate a new user
        :return:
        """
        new_user_email = new_user[0]
        new_user_password = new_user[1]

        self.login_page.navigate()
        self.login_page.login(email=new_user_email,
                              password=new_user_password)

        if self.driver.find_element(By.XPATH, "//*[@class='display-4']").text is not None:
            return new_user_email


    def test_navigate_register_page(self):
        """

        """
        self.registration_page.navigate()

        assert True

    def test_navigate_login_page(self):
        """

        :return:
        """
        self.login_page.navigate()

        assert True

    def test_fill_out_register_new_user_form(self, random_email):
        """
        New user can be registered through the form.

        :param random_email: fixture to generate a random email for form filling
        """
        self.registration_page.navigate()
        self.registration_page.register_new_user(email=random_email,
                                                 username=random_email,
                                                 password="123fish")

        assert self.driver.current_url == self.login_page.url

    def test_user_login(self, new_user):
        '''

        :param new_user: fixture that creates
        :return:
        '''

        new_user_email = new_user[0]
        new_user_password = new_user[1]

        self.login_page.navigate()
        self.login_page.login(email=new_user_email,
                              password=new_user_password)
        welcome_page_message = self.driver.find_element(By.XPATH, "//*[@class='display-4']")
        assert welcome_page_message.text == "Welcome to Grub Geeks, %s!" % new_user_email

    def test_new_user_can_add_forum_posts(self, login_as_new_user, unique_post):
        """

        :param new_user:
        :return:
        """
        self.forum_page.navigate()
        assert self.forum_page.add_post(subject=unique_post,
                                 content="blah") == True
