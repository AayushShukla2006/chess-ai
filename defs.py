# initial_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
initial_board = "4q3/8/8/8/8/8/8/4K3 w - - 0 1"

WIDTH = HEIGHT = 650
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}

# Colors format - [LIGHT, DARK]
colors = [(238, 216, 192), (171, 122, 101)]
highlight_colors = [(207, 172, 106), (197, 173, 96)]
legal_move_colors = [(221, 89, 89), (197, 68, 79)]

board_colors = [
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]],
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]],
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]],
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]]
]

original_colors = [
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]],
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]],
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]],
    [colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1]],
    [colors[1], colors[0], colors[1], colors[0], colors[1], colors[0], colors[1], colors[0]]
]

fen_error = "Invalid character in FEN string."
color_error = "Invalid color value. Must be 'white' or 'black' (case-sensitive) only." \
              "To fix - Check all 'color' arguments of pieces in board.fen_to_board() method, or if you've defined the board by yourself, check the 'color' argument entered."


def to_matrix(lst, number):
    return [lst[i:i + number] for i in range(0, len(lst), number)]


def pos_to_index(pos):
    return pos[0] * 8 + pos[1]


def index_to_pos(index):
    return [index // 8, index % 8]


def get_move_id(arg_move):
    move_id = 0
    count = 0

    for i in arg_move:
        move_id += (i[0] * (10 ** (3 - count))) + (i[1] * (10 ** (2 - count)))
        count += 2

    return move_id


def get_move_from_id(move_id):
    count = 0
    move_id = str(move_id)

    if len(move_id) < 4:
        move_id = "0" * (4 - len(move_id)) + move_id

    return [(int(move_id[0]), int(move_id[1])), (int(move_id[2]), int(move_id[3]))]
