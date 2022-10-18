
from functools import reduce


def flatten(board: list) -> list:
    return len([item for sublist in board for item in sublist if item == 'X' or item == 'O'])


def faltten2(board: list) -> list:
    flat = list(reduce(lambda acc, cur: acc, board))
    pass


def checkTicTacToe(board: list) -> str:
    if flatten(board) != 9:
        return "Invalid board, null result"
        # Check for rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0] + 'to win'
    # Check for columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col] + ' to wins'
    # Check for diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0] + ' to wins'
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2] + ' to wins'
    return 'Tie game, no winner'


def main():
    print(checkTicTacToe([['X', 'O', 'X'],
                          ['X', 'O', 'O'],
                          ['O', 'X', 'X']]))

    print(checkTicTacToe([['X', 'O', 'X'],
                          ['O', 'X', 'O'],
                          ['O', 'X', 'X']]))

    print(checkTicTacToe([['X', 'O', 'X'],
                          ['O', 'X', 'O'],
                          ['O', 'X', 'O']]))

    print(checkTicTacToe([['X', 'O', 'X'],
                          ['O', 'X', 'O'],
                          ['O', 'X', ' ']]))


if __name__ == "__main__":
    main()
