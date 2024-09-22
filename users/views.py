from fastapi import APIRouter
from users.schemas import CreateUser  # импортируем pydantic схему и schemas.py
from users import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")  # пост запрос с боди и валидацией pydantic
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)