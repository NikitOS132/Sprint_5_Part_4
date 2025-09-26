from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *

class TestPersonalArea:
    def test_check_personal_area(self, start_from_login_page):
        driver = start_from_login_page

        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 60).until(EC.url_to_be(profile_site))

        assert driver.current_url == profile_site