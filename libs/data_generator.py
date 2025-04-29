import random
import string
from faker import Faker

fake = Faker()

class Generators:

    def generate_string(self, length=10):
        """Генерирует случайную строку заданной длины"""
        letters = string.ascii_letters
        result = ""
        for _ in range(length):
            result += random.choice(letters)
        return result

    def generate_number(self, min_val=0, max_val=100):
        """Генерирует случайное число в заданном диапазоне"""
        return random.randint(min_val, max_val)

    def generate_email(self, domain="example.com"):
        """Генерирует случайный email"""
        username = fake.word()
        return f"{username}@{domain}"

    def generate_phone_number(self, country_code="+1"):
        """Генерирует случайный номер телефона"""
        return f"{country_code} {random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"