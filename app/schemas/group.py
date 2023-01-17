from pydantic import BaseModel


class Group(BaseModel):
    id: int
    name: str(max_lenght=30)
    user_group: int
