from collections import deque

def min_dice_throws(board):
    """
    board[i] = j means there is a snake or ladder from i → j
    board[i] = -1 means normal cell
    """

    N = len(board)
    visited = [False] * N

    # BFS queue → (cell, distance)
    queue = deque()
    queue.append((0, 0))  # start at cell 0 with 0 throws
    visited[0] = True

    while queue:
        cell, dist = queue.popleft()

        # If reached last cell
        if cell == N - 1:
            return dist

        # Explore next dice moves
        for dice in range(1, 7):
            next_cell = cell + dice

            if next_cell < N and not visited[next_cell]:
                visited[next_cell] = True

                # If there's a snake or ladder, move to its destination
                if board[next_cell] != -1:
                    queue.append((board[next_cell], dist + 1))
                else:
                    queue.append((next_cell, dist + 1))

    return -1  # unreachable (should not happen in valid boards)


# ------------------------------
# EXAMPLE: Snakes and Ladders board
# ------------------------------

# board index represents square number
# value -1 means no snake or ladder
# otherwise it jumps to another square

board = [-1] * 30

# Ladders
board[2] = 21
board[4] = 7
board[10] = 25
board[19] = 28

# Snakes
board[26] = 0
board[20] = 8
board[16] = 3
board[18] = 6

print("Minimum dice throws required:", min_dice_throws(board))
