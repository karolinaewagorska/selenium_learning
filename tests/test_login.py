import time
import pytest
from selenium_demo_shop.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("anna@gmail.com", "annakurnikowa")
        time.sleep(3)

        assert my_account_page.is_logout_displayed()

    def test_login_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("anna@gmail.com", "annaannaanna")
        time.sleep(3)

        assert "Authentication failed." in my_account_page.get_error_message()



