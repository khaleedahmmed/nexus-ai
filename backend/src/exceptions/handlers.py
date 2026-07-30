from fastapi import Request
from fastapi.responses import JSONResponse
from src.exceptions.user_exceptions import UserNotFoundException


async def user_not_found_exception_handler(
    request: Request,
    exception: UserNotFoundException,
):
    return JSONResponse(
        status_code=404,
        content={
            "type": "UserNotFoundException",
            "title": "Resource Not Found",
            "status": 404,
            "detail": str(exception),
            "path": str(request.url.path),
        },
    )
