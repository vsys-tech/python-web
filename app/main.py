import uvicorn
import sys
from fastapi import FastAPI

from app.routes.admin import adminRouter
from app.routes.userroutes import userRouter

app = FastAPI()


@app.get("")
async def read_home():
    return "home page "


@app.get("/")
async def read_home():
    return "home page "


app.include_router(userRouter, prefix="/users", tags=["users"])
app.include_router(adminRouter, prefix="/admin", tags=["admins"])

if __name__ == '__main__':
    import argparse

    for value in sys.argv:
        print(value)

uvicorn.run('main:app', host='localhost', port=80, reload=True)
