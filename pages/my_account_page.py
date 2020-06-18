from selenium.webdriver.common.keys import Keys
from selenium_demo_shop.locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_input = locators.MyAccountPage.email_input
        self.pass_input = locators.MyAccountPage.pass_input
        self.error_msg_login = locators.MyAccountPage.error_msg_login
        self.logout_input = locators.MyAccountPage.logout_input

    def open_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")

    def log_in(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.pass_input).send_keys(password)
        self.driver.find_element(*self.pass_input).send_keys(Keys.ENTER)

    def is_logout_displayed(self):
        return self.driver.find_element(*self.logout_input).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg_login).text

