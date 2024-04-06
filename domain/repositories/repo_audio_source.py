from typing import Protocol
from ..value_objects.audio_source import VOAudioSource


class IAudioSourceRepo(Protocol):

    def get_source(self, book_name: str) -> VOAudioSource:
        ...

    def add_source(self, source: VOAudioSource) -> VOAudioSource:
        ...
