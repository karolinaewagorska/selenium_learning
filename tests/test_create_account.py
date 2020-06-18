from selenium_demo_shop.pages.my_account_page import MyAccountPage
import selenium_demo_shop.pages.account_description_page
import pytest
import random
import time


@pytest.mark.usefixtures("setup")
class TestAccountDescription:

    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        account_description = selenium_demo_shop.pages.account_description_page.AccountDescription(self.driver)
        account_description.create_account("anna@gmail.com")
        msg_account_failed = "An account using this email address has already been registered. Please enter a valid password or request a new one."
        time.sleep(3)

        assert msg_account_failed in my_account_page.get_error_message()

    def test_create_account_passed(self):
        random_email = str(random.randint(0, 10000)) + "anna@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        account_description = selenium_demo_shop.pages.account_description_page.AccountDescription(self.driver)
        account_description.create_account(random_email)
        account_description.set_personal_data("Anna", "Kowalczyk", "annakowalczyk")
        account_description.set_address("11")
        account_description.set_postcode("Poznan", "12345")
        account_description.select_state("Louisiana")
        account_description.select_country("United States")
        account_description.set_phone_number("+45456789123")
        time.sleep(3)

        assert my_account_page.is_logout_displayed()










