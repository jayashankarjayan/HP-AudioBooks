from domain.entities.value_objects.book import VOBook, VOBooks


class BookRepo:

    def __init__(self) -> None:
        self.books = {"sorcerer's stone": VOBook(name="sorcerer's stone"),
                      "chamber of secrets": VOBook(name="chamber of secrets"),
                      "prisoner of azkaban": VOBook(name="prisoner of azkaban"),
                      "goblet of fire": VOBook(name="goblet of fire"),
                      "order of the pheonix": VOBook(name="order of the pheonix"),
                      "half blood prince": VOBook(name="half blood prince"),
                      "deathly hallows": VOBook(name="deathly hallows")}

    def get_by_name(self, name: str) -> VOBook:
        return self.books[name]

    def add_book(self, data: VOBook) -> VOBook:
        self.books[data.name] = VOBook(name=data.name)
        return self.books[data.name]

    def get_all(self) -> list[VOBook]:
        return VOBooks.model_validate(self.books.keys()).root
