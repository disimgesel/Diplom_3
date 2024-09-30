from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание доступности клика элемента')
    def wait_element_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Ожидание смены текста элемента')
    def wait_change_text_element(self, locator, value):
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(locator, value))

    @allure.step('Ожидание закрытия элемента')
    def wait_close_element(self, locator):
        WebDriverWait(self.driver, 20).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Отображения элемента')
    def check_element_is_displaying(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Доступность элемента для клика')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    @allure.step('Клик элемента')
    def click_on_element(self, locator):
        element = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(element).click().perform()

    @allure.step('Ввод данных в поле ввода')
    def input_data_to_field(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получение текста элемента')
    def get_text_element(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text
