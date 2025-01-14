""" User models """
from sqlmodel import Field
from .base import SQLModel

# Shared properties
class UserBase(SQLModel):
    name: str = Field(unique=False, index=True)
    surname: str | None = None
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id_user: int | None = Field(default=None, primary_key=True)
    hashed_password: str

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserCreateOpen(SQLModel):
    email: str
    password: str
    full_name: str | None = None


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None

class UpdatePassword(SQLModel):
    current_password: str
    new_password: str

# Properties to return via API, id_user is always required
class UserOut(UserBase):
    id_user: int

class UsersOut(SQLModel):
    data: list[UserOut]
    count: int

# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str
