from app.models import UserModel

user1 = UserModel.UserModel(id=100, email="some name", role='admin', password="password1")
user2 = UserModel.UserModel(id=101, email="some name", role='manager', password="password2")

users = [user1, user2]


def one_user():
    return user1
    pass


def all_users():
    return users
    pass
