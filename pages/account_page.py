import allure
from pages.base_page import BasePage
from locators.locators import PersonalAccountPageLocators


class AccountPage(BasePage):

    @allure.step('Переход на вкладку История заказов')
    def go_to_order_history_tab(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step('Клик на кнопку Выход')
    def click_on_logout(self):
        self.click_on_element(PersonalAccountPageLocators.EXIT_ACCOUNT)

    @allure.step('Ожмдание отображения кнопки Сохранить')
    def wait_visibility_of_save_button(self):
        self.wait_visibility_element(PersonalAccountPageLocators.SAVE_BUTTON)

    @allure.step('Проверка, что кнопка Сохранить отображается')
    def check_save_button_is_displaying(self):
        return self.check_element_is_displaying(PersonalAccountPageLocators.SAVE_BUTTON)

    @allure.step('Проверка отображения заголовка Вход')
    def check_enter_header_is_displayed(self):
        return self.check_element_is_displaying(PersonalAccountPageLocators.ENTER_HEADER)
