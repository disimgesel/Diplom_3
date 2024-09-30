from pages.base_page import BasePage
from locators.locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step('Получение заголовка страницы заказов')
    def title_text_feed_page(self):
        return self.get_text_element(OrderPageLocators.TITLE_OF_ORDERS_FEED_PAGE)

    @allure.step('Отображение окна с заказом ')
    def modal_order_details_displayed(self):
        self.wait_visibility_element(OrderPageLocators.MODAL_ORDER)
        return self.check_element_is_displaying(OrderPageLocators.MODAL_ORDER)

    @allure.step('Клик карточки заказа')
    def click_order_card(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_CARD_IN_FEED)
        self.click_on_element(OrderPageLocators.ORDER_CARD_IN_FEED)

    @allure.step('Отображения номера заказа в ленте заказов')
    def id_order_displayed_feed(self, order_id):
        locator = (OrderPageLocators.ORDER_CARD_IN_FEED[0],
                   OrderPageLocators.ORDER_ID_FEED[1].format(order_id=order_id))
        wait = self.wait_visibility_element(locator)
        return self.check_element_is_displaying(locator)

    @allure.step('Заказы, выполненные за все время')
    def quantity_orders_all_time(self):
        self.wait_visibility_element(OrderPageLocators.COMPLETE_ORDERS_ALL_TIME)
        return self.get_text_element(OrderPageLocators.COMPLETE_ORDERS_ALL_TIME)

    @allure.step('Заказы, выполненные за сегодня')
    def get_quantity_orders_today(self):
        self.wait_visibility_element(OrderPageLocators.COMPLETE_ORDERS_TODAY)
        return self.get_text_element(OrderPageLocators.COMPLETE_ORDERS_TODAY)

    @allure.step('Последний заказ, взятый в работу')
    def number_order_in_progress_section(self):
        number_order = self.get_text_element(OrderPageLocators.NUMBER_ORDER_IN_PROGRESS_SECTION)
        if number_order is None:
            number_order = '0'
        return number_order

    @allure.step('Ожидание видимости секции с заказами')
    def wait_visibility_of_order_section(self):
        self.wait_visibility_element(OrderPageLocators.ORDER_LIST)

    @allure.step('Получение номера заказа в карточке заказа')
    def get_order_card_id(self):
        return self.get_text_element(OrderPageLocators.ID_ORDER_CARD)
