from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base import Base


class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30))


class Spending(Base):
    id = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey(Category.id))
    name = Column(String(30))
