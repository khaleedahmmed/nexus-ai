from fastapi import Depends
from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService

user_repository = UserRepository()


def get_user_repository() -> UserRepository:

    return user_repository


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserService:

    return UserService(user_repository)
