import heapq
import copy

class Node:
    def __init__(self, board, player, g, h):
        self.board = board
        self.player = player
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def is_win(board, player):
    lines = [
        board[0], board[1], board[2],  # rows
        [board[0][0], board[1][0], board[2][0]],  # columns
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],  # diagonals
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player]*3 in lines

def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0
    for line in [
        board[0], board[1], board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]:
        if line.count(opponent) == 0:
            score += line.count(player)
    return -score  # Negative because we want to win (lower h)

def get_successors(board, player):
    successors = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = copy.deepcopy(board)
                new_board[i][j] = player
                successors.append((new_board, i, j))
    return successors

def a_star_tic_tac_toe(start_board, player):
    open_list = []
    heapq.heappush(open_list, Node(start_board, player, 0, heuristic(start_board, player)))

    while open_list:
        node = heapq.heappop(open_list)

        if is_win(node.board, player):
            return node.board  # Found a winning state

        next_player = 'O' if node.player == 'X' else 'X'

        for successor_board, i, j in get_successors(node.board, node.player):
            h = heuristic(successor_board, next_player)
            heapq.heappush(open_list, Node(successor_board, next_player, node.g + 1, h))

    return None  # No win found

# Example usage
start_board = [[' ']*3 for _ in range(3)]
result = a_star_tic_tac_toe(start_board, 'X')
for row in result:
    print(row)
