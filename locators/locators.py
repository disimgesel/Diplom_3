from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:

    PROFILE = (By.XPATH, '//a[contains(text(),"Профиль")]')
    ORDER_HISTORY = (By.XPATH, '//a[contains(text(),"История заказов")]')
    EXIT_ACCOUNT = (By.XPATH, '//button[contains(text(),"Выход")]')
    DESCRIPTION_SECTION = (By.XPATH, '//p[contains(text(),"В этом разделе вы можете изменить свои персональные данные")]')
    ENTER_HEADER = (By.XPATH, '//h2[contains(text(),"Вход")]')
    SAVE_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]')


class OrderPageLocators:

    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
    TITLE_ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')
    ID_ORDER_CARD = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')
    ORDER_LIST = (By.XPATH, '//div[contains(@class, "OrderHistory_orderHistory__")]')
    TITLE_OF_ORDERS_FEED_PAGE = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')
    ORDER_CARD_IN_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                        '//div[contains(@class, "Modal_orderBox")]')
    TITLE_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]'
                                              '//div[contains(@class, "Modal_orderBox")]//h2')
    NUMBER_ORDER_IN_PROGRESS_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]'
                                                     '/li[contains(@class, "text_type_digits-default")]')
    ORDER_ID_FEED = (By.XPATH, './/*[text()="{order_id}"]')
    COMPLETE_ORDERS_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    COMPLETE_ORDERS_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    IN_PROGRESS_SECTION = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]')


class LoginPageLocators:

    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    ENTER_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    RECOVERY_BUTTON = (By.XPATH, '//a[text()="Восстановить пароль"]')
    REGISTRATION_BUTTON = (By.XPATH, '//a[contains(text(),"Зарегистрироваться")]')
    ENTER_TITLE = (By.XPATH, '//h2[contains(text(),"Вход")]')


class MainPageLocators:

    TITLE_MAIN_PAGE = (By.XPATH, '//h1')
    LK_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    AUTH_BUTTON_LK = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
    CONSTUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]')
    ORDERS_LIST = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    MODAL_INGREDIENT_WINDOW = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    MODAL_INGREDIENT_HEADER = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')
    MODAL_INGREDIENT_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, '
                                             '"Modal_modal_opened")]//button[contains(@class, "close")]')
    OVERLAY = (By.XPATH, "//section[@class='Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")
    SAUCE_SECTION = (By.XPATH, '//span[contains(text(),"Соусы")]')
    FILLINGS_SECTION = (By.XPATH, '//span[contains(text(),"Начинки")]')
    BUNS_SECTION = (By.XPATH, '//span[contains(text(),"Булки")]')
    ACTIVE_SECTION = (By.XPATH, '//div[contains(@class, "tab_tab__") and contains(@class, "tab_tab_type_current__")]')
    INGREDIENT_BUN = (By.XPATH, './/*[@alt="Краторная булка N-200i"]')
    INGREDIENT_FILLING = (By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa70")]')
    INGREDIENT_SAUCE = (By.XPATH, '//a[contains(@href, "/ingredient/61c0c5a71d1f82001bdaaa75")]')
    HISTORY_ORDER = (By.XPATH, '//a[contains(text(),"История заказов")]')
    INGREDIENT_CONSTRUCTION = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    INGREDIENT_COUNTER = (By.XPATH, '//a[contains(@href, "ingredient/61c0c5a71d1f82001bdaaa6c")]'
                                    '//p[@class="counter_counter__num__3nue1"][1]')
    MODAL_CONFIRM_ORDER = (By.XPATH, '//div[contains(@class, "Modal_modal__container")]')
    NUMBER_ORDER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]')
    MODAL_ORDER_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]' 
                                          '//button[contains(@class, "close")]')


class RecoveryPasswordPageLocators:
    
    RECOVERY_PASSWORD = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')
    EMAIL_INPUT = (By.XPATH, '//input[contains(@class, "input__textfield")]')
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    PASSWORD_INPUT = (By.XPATH, '//input[contains(@type, "password")]')
    HIDE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    PASSWORD_VISABILITY_ACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                                '"input_status_active")]')
    PASSWORD_VISABILITY_INACTIVE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                                    '"input_type_password")]')
