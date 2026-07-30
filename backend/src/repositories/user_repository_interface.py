from abc import ABC, abstractmethod

from src.models.user import User

class UserRepositoryInterface(ABC):

    @abstractmethod
    def add(self, user: User) -> User:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        pass