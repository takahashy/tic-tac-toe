"""
Tic Tac Toe Player
"""
from typing import List
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board) -> str | None :
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    count = {X: 0, O: 0}
    for row in board:
        for player in row:
            if player != EMPTY:
                count[player] += 1

    if count[X] == count[O]:
        return X
    else:
        return O


def actions(board) -> tuple | None:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action) -> List[List]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if (board[i][j] != EMPTY) or (i < 0 or i > 2 or j < 0 or j > 2):
        raise Exception("Invalid Move Error")
    
    new_board = deepcopy(board)
    if player(board) == X:
        new_board[i][j] = "X"
    elif player(board) == O:
        new_board[i][j] = "O"

    return new_board


def winner(board) -> str | None:
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and (board[i][0] != EMPTY):
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and (board[0][i] != EMPTY):
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """    
    if winner(board):
        return True
    
    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    X wants to maximize its output
    O wants to minimize its output

    Player's move is dependent on each other
    """
    if player(board) == X:
        return maximize(board, float('inf'))[1]
    elif player(board) == O:
        return minimize(board, float('-inf'))[1]
    else:
        return None


def maximize(board, alpha):
    value = float('-inf')
    max_action = None
    
    if terminal(board):
        return utility(board), max_action
     
    for action in actions(board):
        o_decision = minimize(result(board, action), value)
        
        if o_decision[0] > value:
            value = o_decision[0]
            max_action = action
        if value > alpha:
            break
            
    return value, max_action

def minimize(board, beta):
    value = float('inf')
    min_action = None

    if terminal(board):
        return utility(board), min_action
    
    for action in actions(board):
        x_decision = maximize(result(board, action), value)

        if x_decision[0] < value:
            value = x_decision[0]
            min_action = action
        if value < beta:
            break
            
    return value, min_action
