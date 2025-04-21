import heapq

class Node:
    def __init__(self, board, player, g=0, parent=None):
        self.board = board
        self.player = player  # 'X' or 'O'
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.parent = parent

    def heuristic(self):
        return 8 - self.count_win_paths('X')  # Closer to win = lower h

    def count_win_paths(self, player):
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        count = 0
        for line in lines:
            if all(self.board[i] == player or self.board[i] == ' ' for i in line):
                if not any(self.board[i] == ('O' if player == 'X' else 'X') for i in line):
                    count += 1
        return count

    def is_terminal(self):
        return check_winner(self.board) is not None or ' ' not in self.board

    def __lt__(self, other):
        return self.f < other.f

def check_winner(board):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combos:
        if board[combo[0]] != ' ' and all(board[combo[0]] == board[i] for i in combo):
            return board[combo[0]]
    return None

def get_children(node):
    children = []
    for i in range(9):
        if node.board[i] == ' ':
            new_board = node.board[:]
            new_board[i] = node.player
            next_player = 'O' if node.player == 'X' else 'X'
            children.append(Node(new_board, next_player, node.g + 1, node))
    return children

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.board)
        node = node.parent
    return path[::-1]

def a_star_tic_tac_toe(start_board):
    root = Node(start_board, 'X')
    open_set = []
    heapq.heappush(open_set, root)
    visited = set()

    while open_set:
        current = heapq.heappop(open_set)
        board_tuple = tuple(current.board)

        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        winner = check_winner(current.board)
        if winner == 'X':
            return reconstruct_path(current)

        for child in get_children(current):
            if tuple(child.board) not in visited:
                heapq.heappush(open_set, child)
    return None
if __name__ == "__main__":
    start = [' ' for _ in range(9)]  # Empty board
    path = a_star_tic_tac_toe(start)

    if path:
        print("Winning path for X:")
        for step_num, board in enumerate(path):
            print(f"Step {step_num}:")
            for i in range(0, 9, 3):
                print(board[i:i+3])
            print()
    else:
        print("No winning path found for X.")
