class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidFenError(Error):
    """Exception raised for invalid FEN strings.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class InvalidColorError(Error):
    """Exception raised for invalid color strings.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
