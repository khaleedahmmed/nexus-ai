from src.models.user import User
from src.schemas.user import UserCreateRequest

class UserService:

    def __init__(self):
        self.users: list[User] = []

    def create_user(self,  request: UserCreateRequest,) -> User: 
        user_id = len(self.users) + 1

        user = User(
            id=user_id,
            name=request.name,
            email=request.email,
        )
        self.users.append(user)
        
        return user
    
    def get_all_users(self) -> list[User]:
        return self.users
    
    def get_user_by_id(self, user_id: int) -> User | None:
        for user in self.users:
            if user.id == user_id:
                return user
        return None