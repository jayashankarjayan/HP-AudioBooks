from ...repositories.repo_audio_source import IAudioSourceRepo
from ..value_objects.audio_source import VOAudioSource
from ..value_objects.book import VOBook


class AggAudio:

    @classmethod
    def get_source(cls, audio_repo: IAudioSourceRepo, book: VOBook) -> VOAudioSource:
        return audio_repo.get_by_book_name(book.name)

    @classmethod    
    def add_source(cls, audio_repo: IAudioSourceRepo, source: VOAudioSource) -> VOAudioSource:
        return audio_repo.add_for_book(source)
