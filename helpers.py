import requests
import random
from data.urls import Endpoints
from faker import Faker
faker = Faker()
fakeRU = Faker(locale='ru_RU')


class RegisterDataUser:

    @staticmethod
    def create_user_data():
        name = faker.first_name()
        email = faker.free_email()
        password = faker.password(length=10, special_chars=False, digits=False, upper_case=False, lower_case=True)
        user_data = {
            "email": email,
            "password": password,
            "name": name
        }
        return user_data


def get_order_data():
    response = requests.get(Endpoints.INGREDIENTS)
    data_ingredients = response.json().get('data', [])
    variety = {'bun': [], 'main': [], 'sauce': []}
    for ingredient in data_ingredients:
        category = ingredient.get('type')
        if category in variety:
            variety[category].append(ingredient['_id'])
    get_ingredients = [
        random.choice(variety['bun']),
        random.choice(variety['main']),
        random.choice(variety['sauce'])
    ]
    return get_ingredients
