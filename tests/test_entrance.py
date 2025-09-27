from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import Credential
from curl import *

class TestEntrance:
    def test_check_entrance_main_site(self, start_from_site_not_login):
        driver = start_from_site_not_login

        driver.find_element(*Locators.BIG_LOGIN_BTN).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_check_entrance_profile_button(self, start_from_site_not_login):
        driver = start_from_site_not_login

        driver.find_element(*Locators.button_personal_area).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_check_entrance_register_site(self, start_from_register_page):
        driver = start_from_register_page

        driver.find_element(*Locators.inscription_login).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_check_entrance_forgot(self, start_from_register_page):
        driver = start_from_register_page

        driver.find_element(*Locators.inscription_login).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site