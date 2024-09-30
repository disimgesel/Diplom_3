import allure
from pages.base_page import BasePage
from locators.locators import RecoveryPasswordPageLocators
from data.data import UserData


class RecoveryPasswordPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def transition_recovery_password_page(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.RECOVERY_PASSWORD)
        self.click_on_element(RecoveryPasswordPageLocators.RECOVERY_PASSWORD)

    @allure.step('Ввод email')
    def send_email_input(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.EMAIL_INPUT)
        email = UserData.EMAIL
        self.input_data_to_field(RecoveryPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик ссылки восстановления пароля')
    def click_on_recover_button(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON)
        self.click_on_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON)

    @allure.step('Отображение поля для ввода пароля')
    def check_password_input_is_displaying(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.PASSWORD_INPUT)
        return self.check_element_is_displaying(RecoveryPasswordPageLocators.PASSWORD_INPUT)

    @allure.step('Ввод пароля')
    def send_password_input(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.PASSWORD_INPUT)
        password = UserData.PASSWORD
        self.input_data_to_field(RecoveryPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Клик элемента скрытия/отображения пароля')
    def click_on_hide_password_element(self):
        self.wait_visibility_element(RecoveryPasswordPageLocators.HIDE_PASSWORD)
        self.click_on_element(RecoveryPasswordPageLocators.HIDE_PASSWORD)

    @allure.step('Активность поля ввода пароля')
    def password_field_visible(self):
        return self.check_element_is_displaying(RecoveryPasswordPageLocators.PASSWORD_VISABILITY_ACTIVE)
