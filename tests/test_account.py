from conftest import driver, create_and_delite_user
from pages.account_page import AccountPage
from pages.main_page import MainPage
from data.urls import Endpoints
import allure

class TestPersonalAccountPage:

    @allure.title('Переход в профиль аккаунта по кнопке "Личный кабинет"')
    def test_transition_personal_acc_page(self, driver, create_and_delite_user):
        main_page = MainPage(driver)
        main_page.wait_visibility_title_page()
        main_page.click_on_personal_acc_button()
        account_page = AccountPage(driver)
        account_page.wait_visibility_of_save_button()
        account_page.check_save_button_is_displaying()
        assert Endpoints.ACCOUNT == driver.current_url

    @allure.title('Переход на вкладку "История заказов"')
    def test_transition_order_history_page(self, driver, create_and_delite_user):
        main_page = MainPage(driver)
        main_page.wait_visibility_title_page()
        main_page.click_on_personal_acc_button()
        account_page = AccountPage(driver)
        account_page.wait_visibility_of_save_button()
        account_page.check_save_button_is_displaying()
        account_page.go_to_order_history_tab()
        assert Endpoints.ORDER_HISTORY == driver.current_url

    @allure.title('Выход из аккаунта по кнопке "Выход" в ЛК')
    def test_out_from_account(self, driver, create_and_delite_user):
        main_page = MainPage(driver)
        main_page.wait_visibility_title_page()
        main_page.click_on_personal_acc_button()
        account_page = AccountPage(driver)
        account_page.wait_visibility_of_save_button()
        account_page.check_save_button_is_displaying()
        account_page.click_on_logout()
        assert account_page.check_enter_header_is_displayed()
