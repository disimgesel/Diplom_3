from pages.recovery_password_page import RecoveryPasswordPage
from pages.main_page import MainPage
from data.urls import Endpoints
import allure
from conftest import driver


class TestRecoveryPasswordPage:

    @allure.title('Переход на страницу восстановления пароля')
    def test_transition_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.overlay_drop(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.transition_recovery_password_page()
        assert Endpoints.FORGOT_PASSWORD == driver.current_url

    @allure.title('Переход к восстановлению пароля после ввода email и по клику на кнопку Восстановить')
    def test_click_on_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.overlay_drop(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.transition_recovery_password_page()
        recovery_password_page.send_email_input()
        recovery_password_page.click_on_recover_button()
        assert recovery_password_page.check_password_input_is_displaying()

    @allure.title('Подсвечивание поля "Пароль" при клике элемента "показать"')
    def test_activate_visibility_of_password(self, driver):
        main_page = MainPage(driver)
        main_page.overlay_drop(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.transition_recovery_password_page()
        recovery_password_page.send_email_input()
        recovery_password_page.click_on_recover_button()
        recovery_password_page.send_password_input()
        recovery_password_page.click_on_hide_password_element()
        assert recovery_password_page.password_field_visible()
