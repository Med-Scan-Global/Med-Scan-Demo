from pydantic import BaseModel


class Model(BaseModel):
    model_name: str
    model_version: str


class UserQuery(BaseModel):
    query: str
