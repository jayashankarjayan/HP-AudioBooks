import os
from pydantic import BaseModel, computed_field


class BookDownloadInput(BaseModel):
    name: str

    @computed_field
    @property
    def folder_path(self) -> str:
        return os.path.join(os.getcwd(), self.name)
