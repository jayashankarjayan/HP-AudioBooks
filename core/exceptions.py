class ResourceNotFoundError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidUserInputError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
