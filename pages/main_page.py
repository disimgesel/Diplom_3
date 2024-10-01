import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException


class MainPage(BasePage):

    @allure.step('Загрузка заголовка главной страницы')
    def wait_visibility_title_page(self):
        self.wait_visibility_element(MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step('Получение текста заголовка главной страницы')
    def text_from_title_main_page(self):
        return self.get_text_element(MainPageLocators.TITLE_MAIN_PAGE)

    @allure.step('Клик кнопки "Конструктор"')
    def click_on_constructor_button(self):
        self.wait_visibility_element(MainPageLocators.CONSTUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTUCTOR_BUTTON)

    @allure.step('Клик кнопки "Лента заказов"')
    def click_on_order_list_button(self):
        self.wait_visibility_element(MainPageLocators.ORDERS_LIST)
        self.click_on_element(MainPageLocators.ORDERS_LIST)

    @allure.step('Клик кнопки "Личный кабинет"')
    def click_on_personal_acc_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainPageLocators.LK_BUTTON))
        self.click_on_element(MainPageLocators.LK_BUTTON)

    @allure.step('Клик кнопки "Войти в аккаунт" на домашней странице')
    def click_on_auth_button_main_page(self):
        self.click_on_element(MainPageLocators.AUTH_BUTTON_LK)

    @allure.step('Клик ингредиена')
    def click_on_ingredient(self):
        self.wait_visibility_element(MainPageLocators.INGREDIENT_BUN)
        self.click_on_element(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Отображение модального окна с ингредиентами')
    def ingr_modal_window_is_displaying(self):
        self.wait_visibility_element(MainPageLocators.MODAL_INGREDIENT_HEADER)
        return self.check_element_is_displaying(MainPageLocators.MODAL_INGREDIENT_HEADER)

    @allure.step('Клик кнопки закрытия модального окна с ингредиентами')
    def click_close_button_ingr_modal(self):
        close_modal = self.check_element_is_clickable(MainPageLocators.MODAL_INGREDIENT_CLOSE_BUTTON)
        self.click_on_element(close_modal)

    @allure.step('Отображение модального окна ингредиента')
    def ingr_modal_window_is_not_displaying(self):
        self.wait_close_element(MainPageLocators.MODAL_INGREDIENT_HEADER)
        return not self.check_element_is_displaying(MainPageLocators.MODAL_INGREDIENT_HEADER)

    @allure.step('Добавление ингредиента')
    def add_ingredient(self):
        from_move_element = self.check_element_is_clickable(MainPageLocators.INGREDIENT_BUN)
        to_move_element = self.check_element_is_clickable(MainPageLocators.INGREDIENT_CONSTRUCTION)
        click = ActionChains(self.driver)
        click.click_and_hold(from_move_element).move_to_element(to_move_element).release().perform()

    @allure.step('Количество ингредиентов')
    def get_count_of_ingredient(self):
        return self.get_text_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Клик кнопки создания заказа')
    def click_create_order_button(self):
        self.check_element_is_clickable(MainPageLocators.CREATE_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Отображение модального окна, подтверждаюзего заказ')
    def check_modal_confirmation_order_is_displaying(self):
        self.wait_visibility_element(MainPageLocators.MODAL_CONFIRM_ORDER)
        return self.check_element_is_displaying(MainPageLocators.MODAL_CONFIRM_ORDER)

    @allure.step('Номер заказа, в подтверждающем модальном окне')
    def get_number_of_order_modal(self):
        try:
            self.wait_change_text_element(MainPageLocators.NUMBER_ORDER, '9999')
            return self.get_text_element(MainPageLocators.NUMBER_ORDER)
        except TimeoutException:
            print("TimeoutException: Номер заказа небыл прогружен")
            return '0'

    @allure.step('Клик кнопки закрытия модального окна подтверждения заказа')
    def click_on_close_button_order_modal(self):
        button = self.wait_element_clickable(MainPageLocators.MODAL_ORDER_CLOSE_BUTTON)
        try:
            button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Не отображение окна подтверждения заказа')
    def check_modal_of_order_not_displaying(self):
        self.wait_close_element(MainPageLocators.MODAL_CONFIRM_ORDER)
        return not self.check_element_is_displaying(MainPageLocators.MODAL_CONFIRM_ORDER)

    # Клик элемента с ожиданием исчезновения overlay и исключением
    @staticmethod
    def overlay_drop(driver, repetition=7):
        wait = WebDriverWait(driver, 20)
        attempt_count = 0
        while attempt_count < repetition:
            try:
                if MainPageLocators.OVERLAY:
                    wait.until(EC.invisibility_of_element_located(MainPageLocators.OVERLAY))
                element = wait.until(EC.element_to_be_clickable(MainPageLocators.AUTH_BUTTON_LK))
                element.click()
                return
            except ElementClickInterceptedException:
                attempt_count += 1
                try:
                    if MainPageLocators.OVERLAY:
                        wait.until(EC.invisibility_of_element_located(MainPageLocators.OVERLAY))
                except TimeoutException:
                    print("Overlay остался за установленное время")
                    raise
        raise Exception(f"Не осуществлен клик элемента")
