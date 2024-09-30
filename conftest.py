import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data.urls import Endpoints
import requests
import helpers
from helpers import RegisterDataUser
faker = Faker()


@pytest.fixture(params=['firefox', 'chrome'], scope="function")
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.get(Endpoints.BASE_URL)
    yield browser
    browser.quit()


@pytest.fixture
def create_and_delite_user(driver):
    user_registration = RegisterDataUser()
    user_data = user_registration.create_user_data()
    response = requests.post(Endpoints.CREATE_USER, json=user_data)
    response = response.json()
    access_token = response.get('accessToken')
    if access_token:
        user_data['accessToken'] = access_token
    else:
        raise ValueError("AccessToken отсутствует в ответе")
    main_page = MainPage(driver)
    main_page.click_on_auth_button_main_page()
    login_page = LoginPage(driver)
    login_page.wait_visibility_of_enter_title()
    login_page.send_email(user_data['email'])
    login_page.send_password(user_data['password'])
    login_page.click_on_enter_button()
    yield {'driver': driver, 'user_data': user_data, 'accessToken': response['accessToken']}
    access_token = response['accessToken']
    requests.delete(Endpoints.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture(scope='function')
def create_order(create_and_delite_user):
    order_data_ingr = {'ingredients': helpers.get_order_data()}
    access_token = create_and_delite_user['accessToken']
    response = requests.post(Endpoints.CREATE_ORDER, json=order_data_ingr, headers={'Authorization': access_token})
    order_number = response.json()['order']['number']
    order_data = {'order_number': order_number,
             'user_email': create_and_delite_user['user_data']['email'],
             'user_password': create_and_delite_user['user_data']['password']}
    return order_data
