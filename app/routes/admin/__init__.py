from fastapi import APIRouter

adminRouter = APIRouter()


@adminRouter.get("/")
def get_admin():
    return {"message": "admin works"}
