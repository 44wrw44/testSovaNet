import json
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path, HTTPException
import os
from pydantic import BaseModel

port: int = int(os.getenv('SOVANET_PORT', "8080"))
hello: str = os.getenv('HELLO', "WORLD")

if not os.path.exists('data'):
    os.mkdir('data')

app = FastAPI()


class User(BaseModel):
    name: str = "Piter"
    age: int = 30
    comment: str = "Nigger"


@app.get("/")
async def root():
    return {"message": "Hello "+hello}


@app.post("/user/")
async def create_user(
        user: User,
):
    with open(f"data/{user.name}.txt", "w") as file:
        file.write(user.model_dump())
    return {"success": True}


@app.get("/user/{name}")
async def get_user(
        name: Annotated[str, Path()]
):
    try:
        with open(f"data/{name}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port)