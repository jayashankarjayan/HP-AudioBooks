import typer

from ..datastores.local.audio_source import AudioSourceRepo
from ..datastores.local.book import BookRepo
from ..datastores.local.chapter import ChapterRepo

from services.dto.download import BookDownloadInput
from services.use_cases.download import DownloadBooks


downloader = typer.Typer()

audio_source_repo = AudioSourceRepo()
book_repo = BookRepo()
chapter_repo = ChapterRepo()
download_books = DownloadBooks(book_repo, chapter_repo, audio_source_repo)


@downloader.command()
def download_book(book_name: str):
    user_input = BookDownloadInput(name=book_name)
    download_books.download_by_name(user_input)
