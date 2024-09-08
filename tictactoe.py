'''
tictactoe.py

Implements the logic behind the computer playing tic tac toe
'''
from typing import List
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

'''
returns an empty 3x3 board
'''
def initial_state() -> List[List]:
    return [[EMPTY] * 3 for _ in range(3)]


'''
determines whose turn it is based on the board. X always starts
'''
def player(board) -> str:
    count = {X: 0, O: 0, EMPTY: 0}
    
    for i in range(3):
        for j in range(3):
            count[board[i][j]] += 1

    if count[X] == count[O]:
        return X
    else:
        return O


'''
checks if the board is at a terminal state
'''
def terminal(board) -> bool:
    if winner(board):
        return True
    
    for row in board:
        if EMPTY in row:
            return False
        
    return True


'''
returns the winner if there is one
'''
def winner(board) -> str | None:
    for i in range(3):
        if (board[i][0]) and (board[i][0] == board[i][1] == board[i][2]):
            return board[i][0]
        if (board[0][i]) and (board[0][i] == board[1][i] == board[2][i]):
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]


'''
returns a set of possible actions computer can take based on the board
'''
def actions(board) -> set:
    if terminal(board):
        return {}
    
    actions = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                actions.add((i,j))

    return actions


'''
returns the resulting state of the board after taking an action
'''
def result(board, action) -> List[List]:
    if action not in actions(board):
        print(action, actions(board))
        raise Exception("Invalid Move")
    
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


'''
returns the utility of the board state
'''
def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


'''
algorithm to determine the optimal action a player can take based on the opponent
Returns the best move based on the state of the board 
'''
def minimax(board):
    # maximize the utility of X with alpha beta pruning
    def maximize(board, alpha):
        value = float('-inf')
        move = None

        if terminal(board):
            return utility(board), None

        for action in actions(board):
            o_util, _ = minimize(result(board, action), value)

            if o_util > value:
                value = o_util
                move  = action
            if alpha < value:
                break

        return value, move

    # minimize the utility of O with alpha beta pruning
    def minimize(board, beta):
        value = float('inf')
        move  = None

        if terminal(board):
            return utility(board), None

        for action in actions(board):
            x_util, _ = maximize(result(board, action), value)

            if x_util < value:
                value = x_util
                move  = action
            if beta > value:
                break

        return value, move

    if player(board) == X:
        return maximize(board, float('inf'))[1] 
    else:
        return minimize(board, float('-inf'))[1]
