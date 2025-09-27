from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *

class TestExit:
    def test_check_exit_account(self, start_from_login_page):
        driver = start_from_login_page

        driver.find_element(*Locators.button_personal_area).click()

        driver.find_element(*Locators.PROFILE_EXIT_BTN).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site