import defs
import moves
from Piece import King, Queen, Bishop, Knight, Rook, Pawn, WhiteSpace


# This class contains the current game state and all the values required to keep it running.
class GameState:
    def __init__(self):
        self.board = self.fen_to_board(defs.initial_board)
        self.white_to_move = True
        self.move_log = []

    # This method converts the FEN string to a board of list data type using the 'to_matrix()' method.
    def fen_to_board(self, fen):
        fen_list = fen.split(' ')
        board = []
        rank, file = 0, 0

        if fen_list[1] == 'w':
            self.white_to_move = True
        else:
            self.white_to_move = False

        for char in fen_list[0]:
            if char == '/':
                rank += 1
                file = 0
            elif char.isdigit():
                for i in range(int(char)):
                    board.append(WhiteSpace.WhiteSpace(file, rank))
                    file += 1
            else:
                if char == 'k':
                    board.append(King.King(rank, file, "black"))
                elif char == 'q':
                    board.append(Queen.Queen(rank, file, "black"))
                elif char == 'b':
                    board.append(Bishop.Bishop(rank, file, "black"))
                elif char == 'n':
                    board.append(Knight.Knight(rank, file, "black"))
                elif char == 'r':
                    board.append(Rook.Rook(rank, file, "black"))
                elif char == 'p':
                    board.append(Pawn.Pawn(rank, file, "black"))
                elif char == 'K':
                    board.append(King.King(rank, file, "white"))
                elif char == 'Q':
                    board.append(Queen.Queen(rank, file, "white"))
                elif char == 'B':
                    board.append(Bishop.Bishop(rank, file, "white"))
                elif char == 'N':
                    board.append(Knight.Knight(rank, file, "white"))
                elif char == 'R':
                    board.append(Rook.Rook(rank, file, "white"))
                elif char == 'P':
                    board.append(Pawn.Pawn(rank, file, "white"))
                file += 1

        return defs.to_matrix(board, 8)

    def make_move(self, move):
        if self.board[move.start_rank][move.start_file].color == self.board[move.end_rank][move.end_file].color:  # If you are trying to overlap pieces, it will not be allowed.
            return False
        elif (self.board[move.start_rank][move.start_file].color == "white" and not self.white_to_move) or (self.board[move.start_rank][move.start_file].color == "black" and self.white_to_move):  # If it's not your move, it will not be allowed.
            return False
        else:
            if (move.end_rank, move.end_file) in moves.legal_moves(self.board[move.start_rank][move.start_file], self.board):  # If the move is legal, it will be executed.
                self.board[move.end_rank][move.end_file] = self.board[move.start_rank][move.start_file]
                self.board[move.end_rank][move.end_file].set_rank(move.end_rank)
                self.board[move.end_rank][move.end_file].set_file(move.end_file)
                self.board[move.start_rank][move.start_file] = WhiteSpace.WhiteSpace(move.start_file, move.start_rank)
                self.white_to_move = not self.white_to_move
                return True
            else:
                return False


# This class defines a 'Move' object responsible for identification, validation and execution of a move.
class Move:
    def __init__(self, start_pos, end_pos, board):
        self.start_rank = start_pos[0]
        self.start_file = start_pos[1]
        self.end_rank = end_pos[0]
        self.end_file = end_pos[1]

        self.piece_moved = board[self.start_rank][self.start_file]
        self.piece_captured = board[self.end_rank][self.end_file]
