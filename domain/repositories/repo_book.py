from typing import Protocol
from ..value_objects.book import VOBook, VOBooks


class IBookRepo(Protocol):

    def get_by_name(self, name: str) -> VOBook:
        ...

    def add_book(self, data: VOBook) -> VOBook:
        ...
    
    def get_all(self) -> list[VOBook]:
        ...
