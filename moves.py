from Piece import King, Queen, Bishop, Knight, Rook, Pawn, WhiteSpace
from defs import pos_to_index, index_to_pos


def legal_moves(piece):
    moves = []
    if isinstance(piece, King.King):
        rank = piece.get_rank()
        file = piece.get_file()

        moves = [[rank + 1, file], [rank - 1, file], [rank + 8, file], [rank - 8, file], [rank + 9, file], [rank - 9, file], [rank + 7, file], [rank - 7]]
    elif isinstance(piece, Queen.Queen):
        pass
    elif isinstance(piece, Pawn.Pawn):
        rank = piece.get_rank()
        file = piece.get_file()

        index = pos_to_index([rank, file])

        if piece.get_color() == "white":
            if rank == 6:
                moves = [index + 8, index + 16]
            else:
                moves = [index + 8]
        else:
            if rank == 1:
                moves = [index - 8, index - 16]
            else:
                moves = [index - 8]

        for i in range(len(moves)):
            if moves[i] in range(64):
                moves[i] = index_to_pos(moves[i])
            else:
                moves[i] = None

    # Return the moves list with the elements flipped. For example, [[5,3],[4,5]] will return [[3,5],[5,4]]
    return [[moves[i][1], moves[i][0]] for i in range(len(moves)) if moves[i] is not None]


if __name__ == "__main__":
    king = King.King(4, 4, "white")
    print(legal_moves(king))
