from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello, world!"
    }


@app.get("/hello")  # query стринг
def hello(name):
    return {"message": f"Hello {name}"}


@app.post("/calc/add/")  # калькулятор
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }