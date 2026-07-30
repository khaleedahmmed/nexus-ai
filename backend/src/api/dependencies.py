from src.repositories.user_repository import UserRepository
from src.services.user_service import UserService


def get_user_repository() -> UserRepository:
    return UserRepository()


def get_user_service() -> UserService:
    user_repository = get_user_repository()

    return UserService(user_repository)
