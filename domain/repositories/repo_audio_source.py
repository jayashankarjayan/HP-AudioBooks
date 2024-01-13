from typing import Protocol
from ..entities.value_objects.audio_source import VOAudioSource


class IAudioSourceRepo(Protocol):

    def get_by_book_name(self, book_name: str) -> VOAudioSource:
        ...

    def add_for_book(self, source: VOAudioSource) -> VOAudioSource:
        ...
