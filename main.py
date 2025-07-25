import uvicorn
from fastapi import FastAPI
import os

port: int = int(os.getenv('SOVANET_PORT', "8080"))

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=port)