import os
import requests
from requests.models import Response


from domain.entities.aggregates.agg_book import AggBook
from domain.entities.aggregates.agg_audio import AggAudio
from domain.repositories.repo_audio_source import IAudioSourceRepo
from domain.repositories.repo_book import IBookRepo
from domain.repositories.repo_chapter import IChapterRepo

from ..dto.download import BookDownloadInput


class DownloadBooks:

    def download_by_name(self, book_repo: IBookRepo,
                         chapter_repo: IChapterRepo,
                         audio_repo: IAudioSourceRepo,
                         payload: BookDownloadInput):
        book_aggregate = AggBook.get_book(book_repo, chapter_repo, payload.name)
        book = book_aggregate.book
        chapters = book_aggregate.chapters

        source = AggAudio.get_source(audio_repo, book)

        if not os.path.exists(payload.folder_path):
            os.mkdir(payload.folder_path)

        for chapter in chapters:
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
