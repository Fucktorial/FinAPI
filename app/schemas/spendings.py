from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str(max_lenght=30)


class Spending(BaseModel):
    id: int
    id_category: int
    name: str(max_lenght=30)
