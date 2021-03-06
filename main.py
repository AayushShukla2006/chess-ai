import sys
import pygame
import board
import defs
import moves
from defs import IMAGES, DIMENSION, SQ_SIZE, WIDTH, HEIGHT, MAX_FPS, colors, highlight_colors, board_colors, original_colors, legal_move_colors
from Piece import WhiteSpace


# This function loads the images to the app on runtime.
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load('Images/' + piece + '.png')
        IMAGES[piece] = pygame.transform.smoothscale(IMAGES[piece], (SQ_SIZE, SQ_SIZE))


# This function draws the squares on the board.
def draw_squares(screen):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            pygame.draw.rect(screen, board_colors[i][j], (j * SQ_SIZE, i * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def reset_colors():
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            board_colors[i][j] = original_colors[i][j]


# This function draws the pieces on the board depending on the board argument passed.
def draw_pieces(screen, arg_board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = arg_board[i][j]
            if piece.get_alpha() != '--':
                screen.blit(IMAGES[piece.get_alpha()], pygame.Rect(j * SQ_SIZE, i * SQ_SIZE, SQ_SIZE, SQ_SIZE))


# This function integrates draw_squares() method and draw_pieces() method as a single function.
def draw_game_state(screen, gs):
    draw_squares(screen)
    draw_pieces(screen, gs.board)


# This is the main function of the app.
def main():
    # Pygame initialisation.
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    undo = False

    # Load the images and values to the app.
    gs = board.GameState()
    load_images()

    square_selected = ()  # Stores the selected square (tuple: row, col)
    player_clicks = []  # Stores the last two squares clicked by the player [list: (from_row, from_col), (to_row, to_col)]

    # Main game loop.
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()  # (x, y) location of mouse click

                # Chess Definitions:
                # Rank: The horizontal grid of squares is called the rank. The first rank is the bottommost rank. Here in the program, the y-position of the mouse click is the rank.
                # File: The vertical grid of squares is called the file. The first file is the leftmost file. Here in the program, the x-position of the mouse click is the file.

                file = pos[0] // SQ_SIZE
                rank = pos[1] // SQ_SIZE

                if square_selected == (rank, file):  # If the square is already selected, unselect it
                    square_selected = ()
                    player_clicks = []
                    reset_colors()
                elif len(player_clicks) == 0:
                    if isinstance(gs.board[rank][file], WhiteSpace.WhiteSpace):  # If the selected square is empty, do not select it.
                        square_selected = ()
                        player_clicks = []
                        reset_colors()
                    else:
                        player_clicks.append((rank, file))
                        if (rank + file) % 2 == 0:
                            board_colors[rank][file] = highlight_colors[0]
                        else:
                            board_colors[rank][file] = highlight_colors[1]
                        # Highlight the legal moves of the selected piece.
                        if gs.board[rank][file].get_color() == gs.active_player():
                            for i in moves.legal_moves(gs.board[rank][file], gs.board):
                                moves_to_position = defs.get_move_from_id(i)
                                target_rank = moves_to_position[1][0]
                                target_file = moves_to_position[1][1]
                                if (target_rank + target_file) % 2 == 0:
                                    board_colors[target_rank][target_file] = legal_move_colors[0]
                                else:
                                    board_colors[target_rank][target_file] = legal_move_colors[1]

                else:
                    square_selected = (rank, file)
                    player_clicks.append(square_selected)
                    # Highlight the legal moves of the selected piece.
                    if gs.board[rank][file].get_color() == gs.active_player():
                        for i in moves.legal_moves(gs.board[rank][file], gs.board):
                            moves_to_position = defs.get_move_from_id(i)
                            target_rank = moves_to_position[1][0]
                            target_file = moves_to_position[1][1]
                            if (target_rank + target_file) % 2 == 0:
                                board_colors[target_rank][target_file] = legal_move_colors[0]
                            else:
                                board_colors[target_rank][target_file] = legal_move_colors[1]
                    else:
                        reset_colors()

                if len(player_clicks) == 2:  # If the user clicked on two distinct squares, check its validity and move the piece.
                    move = board.Move(player_clicks[0], player_clicks[1], gs.board)
                    valid = gs.make_move(move)

                    initial_rank = player_clicks[0][0]
                    initial_file = player_clicks[0][1]
                    final_rank = player_clicks[1][0]
                    final_file = player_clicks[1][1]

                    # This is a quality-of-life feature to allow the user to move another piece if he/she had mistakenly selected a wrong piece.
                    # The move will be reset when user clicks on a friendly piece, and the square on which he clicks will be treated as the first square.
                    if valid:
                        player_clicks = []
                        square_selected = ()
                        reset_colors()
                    else:
                        player_clicks = [square_selected]
                        reset_colors()
                        if (initial_rank + initial_file) % 2 == 0:
                            board_colors[initial_rank][initial_file] = colors[0]
                        else:
                            board_colors[initial_rank][initial_file] = colors[1]
                        if gs.board[final_rank][final_file].get_alpha() != '--':
                            if (final_rank + final_file) % 2 == 0:
                                board_colors[final_rank][final_file] = highlight_colors[0]
                            else:
                                board_colors[final_rank][final_file] = highlight_colors[1]
                            # Highlight the legal moves of the selected piece.
                            if gs.board[final_rank][final_file].get_color() == gs.active_player():
                                for i in moves.legal_moves(gs.board[final_rank][final_file], gs.board):
                                    moves_to_position = defs.get_move_from_id(i)
                                    target_rank = moves_to_position[1][0]
                                    target_file = moves_to_position[1][1]
                                    if (target_rank + target_file) % 2 == 0:
                                        board_colors[target_rank][target_file] = legal_move_colors[0]
                                    else:
                                        board_colors[target_rank][target_file] = legal_move_colors[1]
                            else:
                                reset_colors()
                        else:
                            if (final_rank + final_file) % 2 == 0:
                                board_colors[final_rank][final_file] = colors[0]
                            else:
                                board_colors[final_rank][final_file] = colors[1]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    gs.undo_move()
                    square_selected = ()
                    player_clicks = []
                    undo = True

        if undo:
            reset_colors()
            undo = False

        draw_game_state(screen, gs)
        pygame.display.update()
        clock.tick(MAX_FPS)


if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()
