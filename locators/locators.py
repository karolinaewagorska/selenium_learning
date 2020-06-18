from selenium.webdriver.common.by import By


class MyAccountPage:

    email_input = (By.ID, "email")
    pass_input = (By.ID, "passwd")
    error_msg_login = (By.XPATH, "//div[@class='alert alert-danger']//li")
    logout_input = (By.CLASS_NAME, "logout")


class AccountDescriptionPage:

    email_create_input = (By.ID, "email_create")
    first_name_input = (By.ID, "customer_firstname")
    last_name_input = (By.ID, "customer_lastname")
    password_input = (By.ID, "passwd")
    address_input = (By.ID, "address1")
    city_input = (By.ID, "city")
    state_select = (By.ID, "id_state")
    postcode_input = (By.ID, "postcode")
    country_select = (By.ID, "id_country")
    phone_input = (By.ID, "phone_mobile")
    error_msg_create_account = (By.XPATH, "//div[@class='alert alert-danger']//li")
    save_description = (By.XPATH, "//button[@id='submitAccount']")


