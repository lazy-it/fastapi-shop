from pydantic import EmailStr, BaseModel, Field
from typing import Annotated
from annotated_types import MinLen, MaxLen


class CreateUser(BaseModel):  # pydantic класс наследуемся от BaseModel
    # username: str = Field(..., min_length=3, max_length=20) старый подход через Field
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr