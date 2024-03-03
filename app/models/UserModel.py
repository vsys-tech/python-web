from . import BaseModel


class UserModel(BaseModel):
    id: int | None = None
    email: str
    role: str
    password: str
    pass


def __init__(self, **kwargs):
    self.id = kwargs.get('id')
    self.email = kwargs.get('email')
    self.role = kwargs.get('role')
    self.password = kwargs.get('password')
    pass


def __del__(self):
    pass
