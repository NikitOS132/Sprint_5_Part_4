import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential

@pytest.mark.usefixtures("start_from_register_page")
class TestCheckNewRegister:
    def test_something(self, driver, new_user):

        driver.find_element(*Locators.field_name).send_keys(new_user["name"])

        driver.find_element(*Locators.field_email).send_keys(new_user["email"])

        driver.find_element(*Locators.field_password).send_keys(new_user["password"])

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

@pytest.mark.usefixtures("start_from_register_page")
class TestCheckingErrorPassword:
    def test_something(self, driver):

        driver.find_element(*Locators.field_password).send_keys(Credential.incorrect_password)

        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))