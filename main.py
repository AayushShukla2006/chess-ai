import pygame
import board
from Piece import WhiteSpace

# Some pre-defined constants.
WIDTH = HEIGHT = 400
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 30
IMAGES = {}


# This function loads the images to the app on runtime.
def load_images():
    global IMAGES
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.image.load('Images/' + piece + '.png')
        IMAGES[piece] = pygame.transform.smoothscale(IMAGES[piece], (SQ_SIZE, SQ_SIZE))


# This function draws the squares on the board.
def draw_squares(screen):
    colors = [(238, 238, 210), (118, 150, 86)]

    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[(i + j) % 2]
            pygame.draw.rect(screen, color, (j * SQ_SIZE, i * SQ_SIZE, SQ_SIZE, SQ_SIZE))


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
                # Rank: The horizontal grid of squares is called the rank. The first rank is the bottom rank. Here in the program, the y-position of the mouse click is the rank.
                # File: The vertical grid of squares is called the file. The first file is the leftmost file. Here in the program, the x-position of the mouse click is the file.

                file = pos[0] // SQ_SIZE
                rank = pos[1] // SQ_SIZE

                if square_selected == (rank, file):  # If the square is already selected, unselect it
                    square_selected = ()
                    player_clicks = []
                elif len(player_clicks) == 0:
                    if isinstance(gs.board[rank][file], WhiteSpace.WhiteSpace):  # If the selected square is empty, do not select it.
                        square_selected = ()
                        player_clicks = []
                    else:
                        player_clicks.append((rank, file))
                else:
                    square_selected = (rank, file)
                    player_clicks.append(square_selected)

                if len(player_clicks) == 2:  # If the user clicked on two distinct squares, check its validity and move the piece.
                    move = board.Move(player_clicks[0], player_clicks[1], gs.board)
                    gs.make_move(move)
                    player_clicks = []
                    square_selected = ()

        draw_game_state(screen, gs)
        pygame.display.update()
        clock.tick(MAX_FPS)


if __name__ == '__main__':
    main()
