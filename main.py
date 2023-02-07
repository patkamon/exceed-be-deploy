from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"msg": "welcome to root page"}


@app.get("/items/{item_id}/{item_bool}")
def read_item(item_id: int, item_bool: bool = 0 , q: Union[str, None] = None ):
    return {"item_id": item_id, "q": q, "item_bool": item_bool}
