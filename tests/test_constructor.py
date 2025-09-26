from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestCheckChapter:
    def test_check_chapter(self, start_from_site_not_login):
        driver = start_from_site_not_login

        fillings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.TAB_FILLINGS))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", fillings)
        fillings.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Начинки"))

        sauces = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.TAB_SAUCES))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sauces)
        sauces.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Соусы"))

        buns = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.TAB_BUNS))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buns)
        buns.click()

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Булки"))

        new_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_TAB))
        assert new_element.is_displayed()