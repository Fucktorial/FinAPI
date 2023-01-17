from sqlalchemy import Integer, String, Column, Boolean, Time
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.models import (
    Gender,
    Wallet
)

class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    second_name = Column(String(30))
    lastname = Column(String(30))
    gender = Column(Enum(Gender), default=Gender.MALE.value)
    registration_date = Column(TIMESTAMP, default=datetime.now(timezone="UTC"))
    phone_number = Column(String(12))
    email = Column(TEXT)
    wallet = relationship("Wallet", secondary="User_wallet", back_populates="user_wallet")
    group = relationship("Group", secondary="Group_user", back_populates="user_group")
