from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium_demo_shop.locators import locators


class AccountDescription:

    def __init__(self, driver):
        self.driver = driver
        self.email_create_input = locators.AccountDescriptionPage.email_create_input
        self.first_name_input = locators.AccountDescriptionPage.first_name_input
        self.last_name_input = locators.AccountDescriptionPage.last_name_input
        self.password_input = locators.AccountDescriptionPage.password_input
        self.address_input = locators.AccountDescriptionPage.address_input
        self.city_input = locators.AccountDescriptionPage.city_input
        self.state_select = locators.AccountDescriptionPage.state_select
        self.postcode_input = locators.AccountDescriptionPage.postcode_input
        self.country_select = locators.AccountDescriptionPage.country_select
        self.phone_input = locators.AccountDescriptionPage.phone_input
        self.logout_input = locators.MyAccountPage.logout_input

    def create_account(self, new_email):
        self.driver.find_element(*self.email_create_input).send_keys(new_email)
        self.driver.find_element(*self.email_create_input).send_keys(Keys.ENTER)

    def set_personal_data(self, first_name, last_name, new_password):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.password_input).send_keys(new_password)

    def set_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def set_postcode(self, city, postcode):
        self.driver.find_element(*self.city_input).send_keys(city)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)

    def select_state(self, state):
        select = Select(self.driver.find_element(*self.state_select))
        select.select_by_visible_text(state)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_phone_number(self, phone):
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.phone_input).send_keys(Keys.ENTER)








