from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *

class TestPersonalAreaToConstructor:
    def test_check_account_to_constructor(self, start_from_login_page):
        driver = start_from_login_page

        driver.find_element(*Locators.button_personal_area).click()

        driver.find_element(*Locators.button_constaction).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

    def test_check_logo_to_constructor(self, start_from_login_page):
        driver = start_from_login_page

        driver.find_element(*Locators.button_personal_area).click()

        driver.find_element(*Locators.logo).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site