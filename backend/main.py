from fastapi import FastAPI
from src.api.user_routes import router as user_router
from src.exceptions.handlers import user_not_found_exception_handler
from src.exceptions.user_exceptions import UserNotFoundException

app = FastAPI(title="Nexus AI")

app.add_exception_handler(
    UserNotFoundException,
    user_not_found_exception_handler,
)
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Nexus AI API is running"}
