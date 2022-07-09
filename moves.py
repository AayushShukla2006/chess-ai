from Piece import King, Queen, Bishop, Knight, Rook, Pawn, WhiteSpace


def diagonal_moves(rank, file, m_arg_board):
    moves = []

    for i in range(rank + 1, 8):
        if file + (i - rank) <= 7:
            if isinstance(m_arg_board[i][file + (i - rank)], WhiteSpace.WhiteSpace):
                moves.append((i, file + (i - rank)))
            elif m_arg_board[i][file + (i - rank)].get_color() != m_arg_board[rank][file].get_color():
                moves.append((i, file + (i - rank)))
                break
            else:
                break

    for i in range(rank + 1, 8):
        if file - (i - rank) >= 0:
            if isinstance(m_arg_board[i][file - (i - rank)], WhiteSpace.WhiteSpace):
                moves.append((i, file - (i - rank)))
            elif m_arg_board[i][file - (i - rank)].get_color() != m_arg_board[rank][file].get_color():
                moves.append((i, file - (i - rank)))
                break
            else:
                break

    for i in range(rank - 1, -1, -1):
        if file + (rank - i) <= 7:
            if isinstance(m_arg_board[i][file + (rank - i)], WhiteSpace.WhiteSpace):
                moves.append((i, file + (rank - i)))
            elif m_arg_board[i][file + (rank - i)].get_color() != m_arg_board[rank][file].get_color():
                moves.append((i, file + (rank - i)))
                break
            else:
                break

    for i in range(rank - 1, -1, -1):
        if file - (rank - i) >= 0:
            if isinstance(m_arg_board[i][file - (rank - i)], WhiteSpace.WhiteSpace):
                moves.append((i, file - (rank - i)))
            elif m_arg_board[i][file - (rank - i)].get_color() != m_arg_board[rank][file].get_color():
                moves.append((i, file - (rank - i)))
                break
            else:
                break

    return moves


def straight_moves(rank, file, m_arg_board):
    moves = []

    for i in range(rank + 1, 8):
        if isinstance(m_arg_board[i][file], WhiteSpace.WhiteSpace):
            moves.append((i, file))
        elif m_arg_board[i][file].get_color() != m_arg_board[rank][file].get_color():
            moves.append((i, file))
            break
        else:
            break

    for i in range(rank - 1, -1, -1):
        if isinstance(m_arg_board[i][file], WhiteSpace.WhiteSpace):
            moves.append((i, file))
        elif m_arg_board[i][file].get_color() != m_arg_board[rank][file].get_color():
            moves.append((i, file))
            break
        else:
            break

    for i in range(file + 1, 8):
        if isinstance(m_arg_board[rank][i], WhiteSpace.WhiteSpace):
            moves.append((rank, i))
        elif m_arg_board[rank][i].get_color() != m_arg_board[rank][file].get_color():
            moves.append((rank, i))
            break
        else:
            break

    for i in range(file - 1, -1, -1):
        if isinstance(m_arg_board[rank][i], WhiteSpace.WhiteSpace):
            moves.append((rank, i))
        elif m_arg_board[rank][i].get_color() != m_arg_board[rank][file].get_color():
            moves.append((rank, i))
            break
        else:
            break

    return moves


def pawn_moves(rank, file, m_arg_board):
    moves = []

    if m_arg_board[rank][file].get_color() == "white":
        for i in range(rank - 1, rank - 3, -1):
            if isinstance(m_arg_board[i][file], WhiteSpace.WhiteSpace):
                moves.append((i, file))
            else:
                break
        if m_arg_board[rank - 1][file - 1].get_color() == "black":
            moves.append((rank - 1, file - 1))
        if m_arg_board[rank - 1][file + 1].get_color() == "black":
            moves.append((rank - 1, file + 1))
    else:
        for i in range(rank + 1, rank + 3):
            if isinstance(m_arg_board[i][file], WhiteSpace.WhiteSpace):
                moves.append((i, file))
            else:
                break
        if m_arg_board[rank + 1][file - 1].get_color() == "white":
            moves.append((rank + 1, file - 1))
        if m_arg_board[rank + 1][file + 1].get_color() == "white":
            moves.append((rank + 1, file + 1))

    return moves


def knight_moves(rank, file, m_arg_board):
    moves = []

    if file + 2 <= 7:
        if rank + 1 <= 7:
            if isinstance(m_arg_board[rank + 1][file + 2], WhiteSpace.WhiteSpace):
                moves.append((rank + 1, file + 2))
            elif m_arg_board[rank + 1][file + 2].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank + 1, file + 2))
        if rank - 1 >= 0:
            if isinstance(m_arg_board[rank - 1][file + 2], WhiteSpace.WhiteSpace):
                moves.append((rank - 1, file + 2))
            elif m_arg_board[rank - 1][file + 2].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank - 1, file + 2))
    if file - 2 >= 0:
        if rank + 1 <= 7:
            if isinstance(m_arg_board[rank + 1][file - 2], WhiteSpace.WhiteSpace):
                moves.append((rank + 1, file - 2))
            elif m_arg_board[rank + 1][file - 2].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank + 1, file - 2))
        if rank - 1 >= 0:
            if isinstance(m_arg_board[rank - 1][file - 2], WhiteSpace.WhiteSpace):
                moves.append((rank - 1, file - 2))
            elif m_arg_board[rank - 1][file - 2].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank - 1, file - 2))
    if rank + 2 <= 7:
        if file + 1 <= 7:
            if isinstance(m_arg_board[rank + 2][file + 1], WhiteSpace.WhiteSpace):
                moves.append((rank + 2, file + 1))
            elif m_arg_board[rank + 2][file + 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank + 2, file + 1))
        if file - 1 >= 0:
            if isinstance(m_arg_board[rank + 2][file - 1], WhiteSpace.WhiteSpace):
                moves.append((rank + 2, file - 1))
            elif m_arg_board[rank + 2][file - 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank + 2, file - 1))
    if rank - 2 >= 0:
        if file + 1 <= 7:
            if isinstance(m_arg_board[rank - 2][file + 1], WhiteSpace.WhiteSpace):
                moves.append((rank - 2, file + 1))
            elif m_arg_board[rank - 2][file + 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank - 2, file + 1))
        if file - 1 >= 0:
            if isinstance(m_arg_board[rank - 2][file - 1], WhiteSpace.WhiteSpace):
                moves.append((rank - 2, file - 1))
            elif m_arg_board[rank - 2][file - 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank - 2, file - 1))

    return moves


def king_moves(rank, file, m_arg_board):
    moves = []

    if file + 1 <= 7:
        if rank + 1 <= 7:
            if isinstance(m_arg_board[rank + 1][file + 1], WhiteSpace.WhiteSpace):
                moves.append((rank + 1, file + 1))
            elif m_arg_board[rank + 1][file + 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank + 1, file + 1))
        if rank - 1 >= 0:
            if isinstance(m_arg_board[rank - 1][file + 1], WhiteSpace.WhiteSpace):
                moves.append((rank - 1, file + 1))
            elif m_arg_board[rank - 1][file + 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank - 1, file + 1))
    if file - 1 >= 0:
        if rank + 1 <= 7:
            if isinstance(m_arg_board[rank + 1][file - 1], WhiteSpace.WhiteSpace):
                moves.append((rank + 1, file - 1))
            elif m_arg_board[rank + 1][file - 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank + 1, file - 1))
        if rank - 1 >= 0:
            if isinstance(m_arg_board[rank - 1][file - 1], WhiteSpace.WhiteSpace):
                moves.append((rank - 1, file - 1))
            elif m_arg_board[rank - 1][file - 1].get_color() != m_arg_board[rank][file].get_color():
                moves.append((rank - 1, file - 1))
    if rank + 1 <= 7:
        if isinstance(m_arg_board[rank + 1][file], WhiteSpace.WhiteSpace):
            moves.append((rank + 1, file))
        elif m_arg_board[rank + 1][file].get_color() != m_arg_board[rank][file].get_color():
            moves.append((rank + 1, file))
    if rank - 1 >= 0:
        if isinstance(m_arg_board[rank - 1][file], WhiteSpace.WhiteSpace):
            moves.append((rank - 1, file))
        elif m_arg_board[rank - 1][file].get_color() != m_arg_board[rank][file].get_color():
            moves.append((rank - 1, file))
    if file + 1 <= 7:
        if isinstance(m_arg_board[rank][file + 1], WhiteSpace.WhiteSpace):
            moves.append((rank, file + 1))
        elif m_arg_board[rank][file + 1].get_color() != m_arg_board[rank][file].get_color():
            moves.append((rank, file + 1))
    if file - 1 >= 0:
        if isinstance(m_arg_board[rank][file - 1], WhiteSpace.WhiteSpace):
            moves.append((rank, file - 1))
        elif m_arg_board[rank][file - 1].get_color() != m_arg_board[rank][file].get_color():
            moves.append((rank, file - 1))

    return moves


def legal_moves(piece, arg_board):
    if isinstance(piece, King.King):
        return king_moves(piece.get_rank(), piece.get_file(), arg_board)
    elif isinstance(piece, Queen.Queen):
        return diagonal_moves(piece.get_rank(), piece.get_file(), arg_board) + straight_moves(piece.get_rank(), piece.get_file(), arg_board)
    elif isinstance(piece, Bishop.Bishop):
        return diagonal_moves(piece.get_rank(), piece.get_file(), arg_board)
    elif isinstance(piece, Knight.Knight):
        return knight_moves(piece.get_rank(), piece.get_file(), arg_board)
    elif isinstance(piece, Rook.Rook):
        return straight_moves(piece.get_rank(), piece.get_file(), arg_board)
    elif isinstance(piece, Pawn.Pawn):
        return pawn_moves(piece.get_rank(), piece.get_file(), arg_board)
    else:
        return []


def main():
    pass


if __name__ == "__main__":
    main()
