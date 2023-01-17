from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    Integer,
    VARCHAR,
    TIMESTAMP,
    TEXT,
    FLOAT,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, relationship

from enum import Enum
from datetime import datetime

class Gender(Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"


class Group(Base):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(30))
    user_group = relationship("User", secondary="Group_user", back_populates="group")


class Wallet_types(Base):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(30))


class Wallet(Base):
    id = Column(Integer, primary_key=True)
    id_type = Column(Integer, ForeignKey(Wallet_types.id))
    name = Column(VARCHAR(30))
    user_wallet = relationship("User", secondary="User_wallet", back_populates="wallet")


class Categories(Base):
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(30))


class Spending(Base):
    id = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey(Categories.id))
    name = Column(VARCHAR(30))


class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(30))
    second_name = Column(VARCHAR(30))
    lastname = Column(VARCHAR(30))
    gender = Column(Enum(Gender), default=Gender.MALE.value)
    registration_date = Column(TIMESTAMP, default=datetime.now(timezone="UTC"))
    phone_number = Column(VARCHAR(12))
    email = Column(TEXT)
    wallet = relationship(Wallet, secondary="User_wallet", back_populates="user_wallet")
    group = relationship(Wallet, secondary="Group_user", back_populates="user_group")


class User_wallet(Base):
    id_user = Column(Integer, ForeignKey(User.id))
    id_wallet = Column(Integer, ForeignKey(Wallet.id))


class Group_user(Base):
    id_group = Column(Integer, ForeignKey(Group.id))
    id_user = Column(Integer, ForeignKey(User.id))


class Transaction(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    id_user = Column(Integer, ForeignKey(User.id))
    id_wallet = Column(Integer, ForeignKey(Wallet.id))
    id_spending = Column(Integer, ForeignKey(Spending.id))
    value = Column(FLOAT)