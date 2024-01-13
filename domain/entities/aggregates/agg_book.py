from ..value_objects.book import VOBook
from ..value_objects.chapter import VOChapter
from ...repositories.repo_book import IBookRepo
from ...repositories.repo_chapter import IChapterRepo


class AggBook:
    book: VOBook
    chapters: list[VOChapter]

    @classmethod
    def get_book(cls, book_repo: IBookRepo, chapter_repo: IChapterRepo,
                 name: str) -> 'AggBook':
        cls.book = book_repo.get_by_name(name)
        cls.chapters = cls.get_chapters(chapter_repo, cls.book)
        return cls

    @classmethod
    def add_book(cls, book_repo: IBookRepo, book: VOBook) -> VOBook:
        return book_repo.add_book(book)

    @classmethod
    def get_chapters(cls, chapter_repo: IChapterRepo, book: VOBook) -> list[VOChapter]:
        return chapter_repo.get_all(book.name)

    @classmethod
    def get_all_books(cls, book_repo: IBookRepo) -> list[VOBook]:
        return book_repo.get_all()
