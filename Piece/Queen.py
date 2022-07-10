import Piece.Piece as Piece


class Queen(Piece.Piece):
    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_alpha(self):
        if self.color == "white":
            return "wQ"
        elif self.color == "black":
            return "bQ"
        else:
            raise error.InvalidColorError(defs.color_error)

    def print_info(self):
        super().print_info()
        print("Type of the piece is: Queen")
