from sqlalchemy import Column, ForeignKey, Integer, Table

from app.db.base import Base

UserWalletRelation = Table(
    "user_wallet",
    Base.metadata,
    Column("id_user", Integer, ForeignKey("users.id")),
    Column("id_wallet", Integer, ForeignKey("wallets.id")),
)

UserGroupRelation = Table(
    "user_group",
    Base.metadata,
    Column("id_user", Integer, ForeignKey("users.id")),
    Column("id_group", Integer, ForeignKey("groups.id")),
)
