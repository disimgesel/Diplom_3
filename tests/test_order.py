from pages.order_page import OrderPage
from pages.account_page import AccountPage
from conftest import *
import allure


class TestOrderPage:

    @allure.title('Открытие модального окна с деталями заказа')
    def test_open_modal_order_details(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_list_button()
        order_page.click_order_card()
        assert order_page.modal_order_details_displayed()

    @allure.title('Отображение созданного заказа в ленте заказов')
    def test_order_history_is_displaying_in_order(self, driver, create_and_delite_user, create_order):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_page = OrderPage(driver)
        order_page_history = OrderPage(driver)
        main_page.wait_visibility_title_page()
        main_page.add_ingredient()
        main_page.click_create_order_button()
        main_page.check_modal_confirmation_order_is_displaying()
        main_page.click_on_close_button_order_modal()
        main_page.check_modal_of_order_not_displaying()
        main_page.click_on_personal_acc_button()
        account_page.go_to_order_history_tab()
        order_page_history.wait_visibility_of_order_section()
        id_order = order_page_history.get_order_card_id()
        main_page.click_on_order_list_button()
        assert order_page.id_order_displayed_feed(id_order)

    @allure.title('Увеличение счетчика общего количества выполненных заказов при выполнении заказа')
    def test_change_count_of_quantity_orders_all_time_success(self, driver, create_and_delite_user, create_order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_list_button()
        order_count_1 = order_page.quantity_orders_all_time()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_title_page()
        main_page.add_ingredient()
        main_page.click_create_order_button()
        main_page.check_modal_confirmation_order_is_displaying()
        main_page.click_on_close_button_order_modal()
        main_page.check_modal_of_order_not_displaying()
        main_page.click_on_order_list_button()
        order_count_2 = order_page.quantity_orders_all_time()
        assert order_count_2 > order_count_1

    @allure.title('Увеличение счетчика выполненных заказов за день при выполнении заказа')
    def test_change_counter_orders_for_today(self, driver, create_and_delite_user, create_order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_on_order_list_button()
        order_count_1 = order_page.get_quantity_orders_today()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_title_page()
        main_page.add_ingredient()
        main_page.click_create_order_button()
        main_page.check_modal_confirmation_order_is_displaying()
        main_page.click_on_close_button_order_modal()
        main_page.check_modal_of_order_not_displaying()
        main_page.click_on_order_list_button()
        order_count_2 = order_page.get_quantity_orders_today()
        assert order_count_1 < order_count_2

    @allure.title('Отображение созданного заказа в разделе "В работе" ')
    def test_number_new_order_is_displaying_in_progress(self, driver, create_and_delite_user, create_order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_visibility_title_page()
        main_page.add_ingredient()
        main_page.click_create_order_button()
        main_page.check_modal_confirmation_order_is_displaying()
        number_order = main_page.get_number_of_order_modal()
        main_page.click_on_close_button_order_modal()
        main_page.check_modal_of_order_not_displaying()
        main_page.click_on_order_list_button()
        assert order_page.number_order_in_progress_section() == '0'+number_order
