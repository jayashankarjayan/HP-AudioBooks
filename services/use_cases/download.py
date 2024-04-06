import os
import requests
from requests.models import Response


from domain.aggregates.book.read import BookQueryManager
from domain.repositories.repo_audio_source import IAudioSourceRepo
from domain.repositories.repo_book import IBookRepo
from domain.repositories.repo_chapter import IChapterRepo

from ..dto.download import BookDownloadInput


class DownloadBooks:

    
    def __init__(
            self,
            book_repo: IBookRepo,
            chapter_repo: IChapterRepo,
            audio_repo: IAudioSourceRepo
            ) -> None:
        self.book_repo = book_repo
        self.chapter_repo = chapter_repo
        self.audio_repo = audio_repo

    def download_by_name(self, payload: BookDownloadInput):
        book = BookQueryManager.get_book(
            self.book_repo, payload.name
            )

        chapters = BookQueryManager.get_all_chapters(
            self.chapter_repo, book.name
        )

        source = BookQueryManager.get_audio_source(self.audio_repo, book)

        if not os.path.exists(payload.folder_path):
            os.mkdir(payload.folder_path)

        for chapter in chapters.root:
            print(f"Downloading: {chapter.name}")
            chapter_url = f"{source.url}/{chapter.name}.mp3"
            file = os.path.join(payload.folder_path, f"{chapter.name}.mp3")

            if not os.path.exists(file):
                response: Response = requests.get(chapter_url)

                if response.status_code != requests.codes.ok:
                    print(f"Failed to download: {chapter.name}")
                else:
                    with open(file, "wb") as wf:
                        wf.write(response.content)
