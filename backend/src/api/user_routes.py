from fastapi import APIRouter, HTTPException
from src.repositories.user_repository import UserRepository
from src.schemas.user import UserCreateRequest, UserResponse
from src.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])
user_repository = UserRepository()
user_service = UserService(user_repository)


@router.get("/")
def get_users():
    users = user_service.get_all_users()
    return [
        UserResponse(id=user.id, name=user.name, email=user.email) for user in users
    ]


@router.get("/{id}")
def get_user(id: int):
    user = user_service.get_user_by_id(id)
    if user:
        return UserResponse(id=user.id, name=user.name, email=user.email)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/")
def create_user(request: UserCreateRequest):

    created_user = user_service.create_user(request)
    return UserResponse(
        id=created_user.id,
        name=created_user.name,
        email=created_user.email,
    )
