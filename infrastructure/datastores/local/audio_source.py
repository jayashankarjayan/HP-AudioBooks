from domain.entities.value_objects.audio_source import VOAudioSource


class AudioSourceRepo:

    def get_by_book_name(self, book_name: str) -> VOAudioSource:

        sources = {"sorcerer's stone":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="sorcerer's stone",
                                 book_alias="HARR/1 fry HARRY POTTER AND THE PHILOSOPHER'S STONE"),
                   "chamber of secrets":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="chamber of secrets",
                                 book_alias="HARR/2 fry HARRY POTTER AND THE CHAMBER OF SECRETS"),
                   "prisoner of azkaban":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="prisoner of azkaban",
                                 book_alias="HARR/3 fry HARRY POTTER AND THE PRISONER OF AZKABAN"),
                   "goblet of fire":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="goblet of fire",
                                 book_alias="HARR/4 fry HARRY POTTER AND THE GOBLET OF FIRE"),
                   "order of the pheonix":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="order of the pheonix",
                                 book_alias="HARR/5 fry HARRY POTTER ANND THE ORDER OF THE PHOENIX"),
                   "half blood prince":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="half blood prince",
                                 book_alias="HARR/6 fry HARRY POTTER AND THE HALF-BLOOD PRINCE"),
                   "deathly hallows":
                   VOAudioSource(name="http://harryaudiobooks.net", book_name="deathly hallows",
                                 book_alias="HARR/7 fry HARRY POTTER AND THE DEATHLY HALLOWS")}
        return sources[book_name]

    def add_for_book(self, source: VOAudioSource) -> VOAudioSource:
        ...
