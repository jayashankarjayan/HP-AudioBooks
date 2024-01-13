from typing import Protocol
from ..entities.value_objects.chapter import VOChapter, VOChapters


class IChapterRepo(Protocol):

    def get_all(self, book_name: str) -> list[VOChapter]:
        ...

    def add_chapters(self, chapters: VOChapters) -> list[VOChapter]:
        ...
