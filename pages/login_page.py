from locators.locators import LoginPageLocators
from pages.base_page import BasePage
from data.data import UserData
import allure


class LoginPage(BasePage):

    email = UserData.EMAIL
    password = UserData.PASSWORD

    @allure.step('Ввод email при авторизации')
    def send_email(self, email):
        email_input = self.check_element_is_clickable(LoginPageLocators.EMAIL_FIELD)
        email_input.click()
        email_input.send_keys(email)

    @allure.step('Ввод пароля при авторизации')
    def send_password(self, password):
        password_input = self.check_element_is_clickable(LoginPageLocators.PASSWORD_FIELD)
        password_input.click()
        password_input.send_keys(password)

    @allure.step('Клик кнопки "Войти"')
    def click_on_enter_button(self):
        enter_button = self.check_element_is_clickable(LoginPageLocators.ENTER_BUTTON)
        enter_button.click()

    @allure.step('Ожидание отображения титла "Вход" страницы авторизации')
    def wait_visibility_of_enter_title(self):
        self.wait_visibility_element(LoginPageLocators.ENTER_TITLE)
