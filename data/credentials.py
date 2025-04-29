import os

from dotenv import load_dotenv
load_dotenv()
class Credentials:
    LOGIN_ADMIN = os.getenv("LoginAdmin")
    PASSWORD_ADMIN = os.getenv("PasswordAdmin")

    LOGIN_USER = os.getenv("LoginUser")
    PASSWORD_USER = os.getenv("PasswordUser")
