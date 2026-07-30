# class User:

#     def __init__(self, id: int, name: str, email: str):
#             self.id = id
#             self.name = name
#             self.email = email


from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    email: str


# from pydantic import BaseModel


# class User(BaseModel):
#     id: int
#     name: str
#     email: str
