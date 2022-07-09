initial_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


def to_matrix(lst, number):
    return [lst[i:i + number] for i in range(0, len(lst), number)]


def pos_to_index(pos):
    return pos[0] * 8 + pos[1]


def index_to_pos(index):
    return [index // 8, index % 8]


def binary_search(lst, element):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return mid
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1
