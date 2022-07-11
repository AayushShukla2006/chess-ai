import defs
import error
import moves
import pygame
from Piece import King, Queen, Bishop, Knight, Rook, Pawn, WhiteSpace


# This class contains the current game state and all the values required to keep it running.
class GameState:
    def __init__(self):
        self.white_to_move = False
        self.move_check = False
        self.board = self.fen_to_board(defs.initial_board)
        self.move_log = []
        self.white_king_position = (7, 4)
        self.black_king_position = (0, 4)
        self.get_valid_moves()
        pygame.init()

    # This method converts the FEN string to a board of list data type using the 'to_matrix()' method.
    def fen_to_board(self, fen):
        fen_list = fen.split(' ')
        board = []
        rank, file = 0, 0

        if fen_list[1] == 'w':
            self.white_to_move = True
        else:
            self.white_to_move = False

        if ('K' not in fen_list[0]) or ('k' not in fen_list[0]):
            raise error.NoKingError(defs.no_king_error)

        for char in fen_list[0]:
            if char == '/':
                rank += 1
                file = 0
            elif char.isdigit():
                for i in range(int(char)):
                    board.append(WhiteSpace.WhiteSpace(file, rank))
                    file += 1
            else:
                match char:
                    case 'K':
                        board.append(King.King(rank, file, "white"))
                    case 'Q':
                        board.append(Queen.Queen(rank, file, "white"))
                    case 'B':
                        board.append(Bishop.Bishop(rank, file, "white"))
                    case 'N':
                        board.append(Knight.Knight(rank, file, "white"))
                    case 'R':
                        board.append(Rook.Rook(rank, file, "white"))
                    case 'P':
                        board.append(Pawn.Pawn(rank, file, "white"))
                    case 'k':
                        board.append(King.King(rank, file, "black"))
                    case 'q':
                        board.append(Queen.Queen(rank, file, "black"))
                    case 'b':
                        board.append(Bishop.Bishop(rank, file, "black"))
                    case 'n':
                        board.append(Knight.Knight(rank, file, "black"))
                    case 'r':
                        board.append(Rook.Rook(rank, file, "black"))
                    case 'p':
                        board.append(Pawn.Pawn(rank, file, "black"))
                    case _:
                        raise error.InvalidFenError(defs.fen_error)
                file += 1

        if len(board) != 64:
            raise error.InvalidFenError(defs.invalid_fen_error)
        return defs.to_matrix(board, 8)

    def make_move(self, move):
        if self.board[move.start_rank][move.start_file].color == self.board[move.end_rank][move.end_file].color:  # If you are trying to overlap pieces, it will not be allowed.
            return False
        elif (self.board[move.start_rank][move.start_file].color == "white" and not self.white_to_move) or (self.board[move.start_rank][move.start_file].color == "black" and self.white_to_move):  # If it's not your move, it will not be allowed.
            return False
        else:
            if defs.get_move_id([(move.start_rank, move.start_file), (move.end_rank, move.end_file)]) in moves.legal_moves(self.board[move.start_rank][move.start_file], self.board):  # If the move is legal, it will be executed.
                self.board[move.end_rank][move.end_file] = self.board[move.start_rank][move.start_file]
                self.board[move.end_rank][move.end_file].set_rank(move.end_rank)
                self.board[move.end_rank][move.end_file].set_file(move.end_file)
                self.board[move.start_rank][move.start_file] = WhiteSpace.WhiteSpace(move.start_file, move.start_rank)
                self.move_log.append(move)

                if move.piece_captured.get_alpha() == 'wK' or move.piece_captured.get_alpha() == 'bK':
                    raise error.KingCapturedError(defs.king_captured_error)

                # If any of the kings were moved, update their positions.
                if move.piece_moved.get_alpha() == "wK":
                    self.white_king_position = (move.end_rank, move.end_file)
                elif move.piece_moved.get_alpha() == "bK":
                    self.black_king_position = (move.end_rank, move.end_file)

                if not self.move_check:
                    if self.active_player() == "white":
                        if self.in_check("black"):
                            pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/check.wav"))
                        else:
                            if move.piece_captured.get_alpha() != "--":  # If you captured a piece, it will be executed with a capture sound.
                                pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/capture.wav"))
                            elif move.piece_captured.get_alpha() == "--":  # If you made a normal move, it will be executed with a normal sound.
                                pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/normal.wav"))
                    elif self.active_player() == "black":
                        if self.in_check("white"):
                            pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/check.wav"))
                        else:
                            if move.piece_captured.get_alpha() != "--":
                                pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/capture.wav"))
                            elif move.piece_captured.get_alpha() == "--":
                                pygame.mixer.Sound.play(pygame.mixer.Sound("sounds/normal.wav"))
                self.white_to_move = not self.white_to_move
                return True
            else:
                return False

    def undo_move(self):
        if len(self.move_log) > 0:
            move = self.move_log.pop()
            self.board[move.start_rank][move.start_file] = move.piece_moved
            self.board[move.start_rank][move.start_file].set_rank(move.start_rank)
            self.board[move.start_rank][move.start_file].set_file(move.start_file)
            self.board[move.end_rank][move.end_file] = move.piece_captured
            if move.piece_moved.get_alpha() == "wK":
                self.white_king_position = (move.start_rank, move.start_file)
            elif move.piece_moved.get_alpha() == "bK":
                self.black_king_position = (move.start_rank, move.start_file)
            self.white_to_move = not self.white_to_move
            return True
        else:
            return False

    def all_possible_moves(self):
        possible_moves = []

        for rank in range(8):
            for file in range(8):
                if self.board[rank][file].get_alpha() != "--":
                    possible_moves.append(moves.legal_moves(self.board[rank][file], self.board))

        return possible_moves

    def in_check(self, color):
        if color == "white":
            king_position = self.white_king_position
        else:
            king_position = self.black_king_position
        if self.is_square_under_attack(king_position[0], king_position[1]):
            return True
        else:
            return False

    def active_player(self):
        if self.white_to_move:
            return "white"
        else:
            return "black"

    @staticmethod
    def opposite_color(color):
        if color == "white":
            return "black"
        else:
            return "white"

    def get_valid_moves(self):
        valid_moves = self.all_possible_moves()

        for i in self.board:
            for j in i:
                if j.get_alpha() != "--":
                    move = moves.legal_moves(j, self.board)
                    for k in move:
                        move_to_make_temp = defs.get_move_from_id(k)
                        move_to_make = Move((move_to_make_temp[0][0], move_to_make_temp[0][1]), (move_to_make_temp[1][0], move_to_make_temp[1][1]), self.board)
                        self.make_move(move_to_make)
                        if self.in_check(self.opposite_color(self.active_player())):
                            print("Invalid move: " + str(move_to_make_temp))
                        self.undo_move()

        return valid_moves

    def is_square_under_attack(self, rank, file):
        for row in self.board:
            for piece in row:
                if piece.get_alpha() != "--":
                    if piece.get_color() != self.board[rank][file].get_color():
                        temp = str(rank) + str(file)
                        for k in moves.legal_moves(piece, self.board):
                            if temp == k[2:]:
                                return True
        return False


# This class defines a 'Move' object responsible for identification, validation and execution of a move.
class Move:
    def __init__(self, start_pos, end_pos, board):
        self.start_rank = start_pos[0]
        self.start_file = start_pos[1]
        self.end_rank = end_pos[0]
        self.end_file = end_pos[1]
        self.move_type = None
        self.move_id = self.start_rank * 1000 + self.start_file * 100 + self.end_rank * 10 + self.end_file
        self.SOUND = {"CAPTURE": pygame.mixer.Sound("sounds/capture.wav"), "NORMAL": pygame.mixer.Sound("sounds/normal.wav")}

        self.piece_moved = board[self.start_rank][self.start_file]
        self.piece_captured = board[self.end_rank][self.end_file]

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_move_type(self):
        return self.move_type

    def set_move_type(self, move_type):
        self.move_type = move_type
