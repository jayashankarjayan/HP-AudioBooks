from pydantic import BaseModel


class VOAudioSource(BaseModel):
    name: str
    book_name: str
    book_alias: str

    @property
    def url(self) -> str:
        _url = "https://ipaudio4.com/wp-content/uploads"
        return f"{_url}/{self.book_alias}"
