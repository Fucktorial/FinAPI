from enum import Enum

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base
from app.models.relations import UserGroupRelation, UserWalletRelation


class Gender(str, Enum):
    __tablename__ = "genders"

    FEMALE = "FEMALE"
    MALE = "MALE"
    OTHER = "OTHER"
    UNDEFINED = "UNDEFINED"
    

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    secondname = Column(String(30), nullable=True)
    lastname = Column(String(30), nullable=True)
    gender = Column(Enum(Gender), default=Gender.UNDEFINED.value)
    registration_date = Column(DateTime, default=func.now(), nullable=False)
    phone_number = Column(String(12), nullable=False)
    email = Column(String)
    wallet = relationship(
        "Wallet",
        secondary=UserWalletRelation,
        back_populates="user_wallets",
        cascade="all, delete",
    )
    group = relationship(
        "Group",
        secondary=UserGroupRelation,
        back_populates="user_groups",
        cascade="all, delete",
    )