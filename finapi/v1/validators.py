import re

from pydantic import BaseModel, EmailStr, validator


class NameValidator(BaseModel):
    name: str(max_length=30)


class Group(NameValidator):
    pass


class Wallet_types(NameValidator):
    pass


class Wallet(NameValidator):
    pass


class Categories(NameValidator):
    pass


class Spending(NameValidator):
    pass


class User(BaseModel):
    username: str(max_length=30)
    second_name: str(max_length=30)
    lastname: str(max_length=30)
    phone_number: str(max_length=12)
    email: EmailStr

    @validator("phone_number")
    def phone_validator(cls, value):
        re_expression = r"/^(\+7|8)(9{1})(\d{9})/"
        if not re.match(re_expression, value):
            raise ValueError("Неверных формат номера телефона")
        return value
