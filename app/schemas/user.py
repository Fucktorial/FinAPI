import re
from datetime import datetime

from pydantic import BaseModel, EmailStr, validator

from app.models.user import Gender


def normalize(name: str) -> str:
    return " ".join(word.strip().capitalize() for word in name.split(" "))


class UserBase(BaseModel):
    username: str(max_lenght=30)
    secondname: str(max_lenght=30)
    lastname: str(max_lenght=30)
    gender: Gender
    registration_date: datetime
    phone_number: str(max_lenght=12)
    email: EmailStr
    wallet: int
    group: int

    # Validators
    @validator("phone_number")
    def phone_validator(cls, value):
        re_expr = r"/^(\+7|8)(9{1})(\d{9})/"
        if not re.match(re_expr, value):
            raise ValueError("wrong phone number format")
        return value

    _normalize_name = validator("name", allow_reuse=True)(normalize)
    _normalize_secondname = validator("secondname", allow_reuse=True)(
        normalize
    )
    _normalize_lastname = validator("lastname", allow_reuse=True)(normalize)


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
