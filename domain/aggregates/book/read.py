from ...repositories.repo_audio_source import IAudioSourceRepo
from ...value_objects.audio_source import VOAudioSource
from ...value_objects.chapter import VOChapters
from ...value_objects.book import VOBook, VOBooks
from ...repositories.repo_book import IBookRepo
from ...repositories.repo_chapter import IChapterRepo


class BookQueryManager:

    @staticmethod
    def get_book(book_repo: IBookRepo, name: str) -> VOBook:
        return book_repo.get_by_name(name)

    @staticmethod
    def get_all_books(book_repo: IBookRepo) -> VOBooks:
        return book_repo.get_all()

    @staticmethod
    def get_all_chapters(chapter_repo: IChapterRepo, book_name: str) -> VOChapters:
        return chapter_repo.get_all(book_name)

    @staticmethod
    def get_audio_source(audio_repo: IAudioSourceRepo, book: VOBook) -> VOAudioSource:
        return audio_repo.get_source(book.name)
