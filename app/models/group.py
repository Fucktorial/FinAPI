from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.relations import UserGroupRelation


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    user_group = relationship(
        "User",
        secondary=UserGroupRelation,
        back_populates="group",
        cascade="all, delete",
    )
