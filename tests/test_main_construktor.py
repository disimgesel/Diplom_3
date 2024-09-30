from pages.order_page import OrderPage
from data.data import ExpectedResult
from conftest import *
import allure


class TestMainConstruktor:

    @allure.title('Переход на страницу "Конструктор"')
    def test_transition_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_list_button()
        main_page.click_on_constructor_button()
        assert ExpectedResult.TITLE_PAGE_KONSTRUKTOR in main_page.text_from_title_main_page()

    @allure.title('Переход на страницу "Лента заказов"')
    def test_transition_orders_feed_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_list_button()
        assert order_page.title_text_feed_page() == "Лента заказов"

    @allure.title('Отображение окна "Детали ингредиента"')
    def test_details_modal_window_ingredient_is_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.ingr_modal_window_is_displaying()

    @allure.title('Закрытие окна "Детали ингредиента"')
    def test_closing_details_modal_window_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_close_button_ingr_modal()
        assert main_page.ingr_modal_window_is_not_displaying()

    @allure.title('Увеличение счетчика количества ингредиентов после добавления')
    def test_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_title_page()
        main_page.add_ingredient()
        assert main_page.get_count_of_ingredient() == '2'

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_authorized_user_can_create_order(self, driver, create_and_delite_user):
        main_page = MainPage(driver)
        main_page.wait_visibility_title_page()
        main_page.add_ingredient()
        main_page.click_create_order_button()
        assert main_page.check_modal_confirmation_order_is_displaying()
