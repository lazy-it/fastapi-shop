from typing import Annotated

from fastapi import Path, APIRouter  # Подключаем АПИ роутер


'''
Создаем отдельное пространство имен с именем роутер, в prefix все запросы будут идти на /items
'''
router = APIRouter(prefix="/items", tags=['Items'])


@router.get("/")
def list_items():
    return [
        "Item1",
        "Item2"
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/{item_id}")
def get_item_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):  # Задаем число от 1 до 10000000
    return {
        "item": {
            "id": item_id,
        },
    }