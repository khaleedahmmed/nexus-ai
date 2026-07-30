from src.exceptions.user_exceptions import UserNotFoundException
from src.models.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface
from src.schemas.user import UserCreateRequest


class UserService:

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(
        self,
        request: UserCreateRequest,
    ) -> User:
        user_id = len(self.user_repository.get_all()) + 1

        user = User(
            id=user_id,
            name=request.name,
            email=request.email,
        )

        user = self.user_repository.add(user)

        return user

    def get_all_users(self) -> list[User]:
        return self.user_repository.get_all()

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User:

        user = self.user_repository.get_by_id(user_id)

        if user is None:
            raise UserNotFoundException(user_id)

        return user
