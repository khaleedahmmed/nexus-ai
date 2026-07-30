from src.models.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users: list[User] = []

    def add(self, user: User) -> User:
        self.users.append(user)

        return user

    def get_all(self) -> list[User]:
        return self.users

    def get_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user

        return None
