from pydantic import BaseModel, RootModel


class VOBook(BaseModel):
    name: str

class VOBooks(RootModel[list[VOBook]]):
    root: list[VOBook]
