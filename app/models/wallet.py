from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.relations import UserWalletRelation


class Wallet_types(Base):
    __tablename__ = "wallet_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    id_type = Column(Integer, ForeignKey(Wallet_types.id))
    name = Column(String(30))
    user_wallet = relationship(
        "User",
        secondary=UserWalletRelation,
        back_populates="wallet",
        cascade="all, delete",
    )
