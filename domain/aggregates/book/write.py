from core.exceptions import InvalidUserInputError, ResourceNotFoundError
from ...value_objects.audio_source import VOAudioSource
from ...value_objects.book import VOBook
from ...value_objects.chapter import VOChapters
from ...repositories.repo_book import IBookRepo
from ...repositories.repo_audio_source import IAudioSourceRepo
from ...repositories.repo_chapter import IChapterRepo


class AggBook:
    book: VOBook
    chapters: VOChapters = VOChapters.model_validate([])

    def __init__(
            self,
            book_repo: IBookRepo,
            chapter_repo: IChapterRepo,
            audio_repo: IAudioSourceRepo,
            book: VOBook | None = None,
            chapters: VOChapters | None = None,
            audio_source: VOAudioSource | None = None,
            book_name: str | None = None
            ) -> None:
        self.book_repo = book_repo
        self.chapter_repo = chapter_repo
        self.audio_repo = audio_repo

        self.book = book
        self.chapters = chapters
        self.audio_source = audio_source

        self.__book_name = book_name

    def __enter__(self) -> "AggBook":
        if self.__book_name:
            if self.book.name != self.__book_name:
                raise InvalidUserInputError(
                    "Provided book id or an object of VOBook are not identical. Provide only one of them"
                )

            return self.get_agg_by_book_name(
                self.book_repo,
                self.chapter_repo,
                self.audio_repo,
                book_name=self.__book_name
            )
        
        
        if not self.__book_name and not self.book:
            raise InvalidUserInputError(
                "Provide either a book name or an object of VOBook"
            )
        
        if self.__book_name:
            return self.get_agg_by_book_name(
                self.book_repo,
                self.chapter_repo,
                self.audio_repo,
                book_name=self.__book_name
            )
        return self

    def get_agg_by_book_name(
            self,
            book_repo: IBookRepo,
            chapter_repo: IChapterRepo,
            audio_repo: IAudioSourceRepo,
            book_name: str
    ) -> "AggBook":
        self.book = book_repo.get_by_name(book_name)
        if not self.book:
            raise ResourceNotFoundError(
                f"Requested book was not found: {book_name}"
            )
        
        self.chapters = chapter_repo.get_all(book_name)
        self.audio_source = audio_repo.get_source(self.book.name)

        return self

    def add_book(self) -> "AggBook":
        # book_repo.add_book(book)
        return self

    def add_source(self) -> "AggBook":
        # audio_repo.add_for_book(source)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """
        TODO: Exit logic to be added
        """
        pass
