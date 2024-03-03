from fastapi import APIRouter
import random
import app.services.users as userService
from app.models.UserModel import UserModel

userRouter = APIRouter()


@userRouter.get("/")
async def root_main():
    return " users works"


@userRouter.get("/first")
async def users_first():
    return userService.one_user()


@userRouter.get("/all")
async def all_users():
    return userService.all_users()


@userRouter.put("/add")
async def add_user(user: UserModel):
    random.seed(999)
    user.id = random.randint(1, 999)
    userService.users.append(user)
    return "Added user"
    pass
