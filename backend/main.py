# from src.config import settings
# from src.models.user import User

# def main():
#     print("Hello from backend!")
#     print("=== Testing Settings ===")
#     print(f"App Name: {settings.app.app_name}")
#     print(f"APP Environment: {settings.app.app_env}")
#     print(f"Debug Mode: {settings.app.debug} (Type: {type(settings.app.debug)})")
#     print(f"OpenAI Key: {settings.ai.openai_api_key}")

#     # user = User(id=1,name="Khaled",email="khaled@test.com")
#     user = User(1, "Khaled")
#     print(user.name)
# if __name__ == "__main__":
#     main()
    
from fastapi import FastAPI
from src.api.user_routes import router as user_router

app = FastAPI(title="Nexus AI")

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Nexus AI API is running"}

@app.get("/f")
def t():
    return {"message": "Nefff"}