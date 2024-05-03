from typing import Literal

from pydantic import BaseModel, ConfigDict


class UserLoginIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    login: str
    password: str


class UserLoginOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    token: str


class UserRegisterIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str | None = None
    login: str
    password: str
    role: Literal['user', 'admin', 'editor']


class UserRegisterOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    token: str


class UserChangeNameIn(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str
    last_name: str
