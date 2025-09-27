from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential

class TestCheckRegister:
    def test_new_register(self, start_from_register_page, new_user):
        driver = start_from_register_page

        driver.find_element(*Locators.field_name).send_keys(new_user["name"])

        driver.find_element(*Locators.field_email).send_keys(new_user["email"])

        driver.find_element(*Locators.field_password).send_keys(new_user["password"])

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

    def test_err_password_in_register(self, start_from_register_page):
        driver = start_from_register_page

        driver.find_element(*Locators.field_password).send_keys(Credential.incorrect_password)

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))