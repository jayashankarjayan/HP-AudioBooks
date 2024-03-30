from pydantic import BaseModel, RootModel


class VOChapter(BaseModel):
    name: str
    book_name: str


class VOChapters(RootModel[list[VOChapter]]):
    root: list[VOChapter]
