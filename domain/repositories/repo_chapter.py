from typing import Protocol
from ..value_objects.chapter import VOChapters


class IChapterRepo(Protocol):

    def get_all(self, book_name: str) -> VOChapters:
        ...

    def bulk_add_chapters(self, chapters: VOChapters) -> VOChapters:
        ...
