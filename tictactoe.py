"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
'''
    Importing deepcopy from copy to create a copy of the board to avoid changing the original board.
'''

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


def player(board):
    """
    Returns player who has the next turn on a board.
    For this function, we assume that X always plays first.
    We start by counting the number of X's and O's on the board.
    Because X always plays first, we can use the number of X's and O's to determine the next player.
    By using the modulo of 2, we can determine if the number of plays is even or odd.
    With this information, we can determine the next player, and return the player.
    This function doesn't have in consideration the case where the board is full, it will return the player that should play next.
    """
    X_count = 0
    O_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                X_count += 1
            elif cell == O:
                O_count += 1
    if X_count % 2 == 0:
        if O_count % 2 == 0:
            return X
        elif O_count % 2 == 1:
            return O
    elif X_count % 2 == 1:
        if O_count % 2 == 0:
            return O
        elif O_count % 2 == 1:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    In this function, we create a set of all possible actions available on the board.
    To achieve this, we iterate through the rows and columns of the board, getting each individual cell.
    We get the index of each cell with the enumerate function.
    If the cell is empty, we add the index of the cell to the set of actions.
    We then return the set of actions.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    In this function we return the board results after a play.
    We make a deep copy of the board, to avoid changing the original board.
    If the action its not valid, we raise an exception, informing the user what went wrong.
    If everything is ok, we return the board with the new play.
    """
    cloned_board = deepcopy(board)
    subscritable_action = list(deepcopy(action))
    turn = player(board)
    if cloned_board[subscritable_action[0]][subscritable_action[1]] is not EMPTY:
        raise Exception("Invalid Play. Cell is not empty.")
    else:
        cloned_board[subscritable_action[0]][subscritable_action[1]] = turn
        return cloned_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    In this function we check if there is a winner and return the winner, if there is one.
    To achieve this, we iterate through the rows and columns of the board, getting each individual cell.
    We get the index of each cell with the enumerate function.
    To check if there is a winner in the iterations, we check:
        - diagonal i = j
        - diagonal j = 2 - i
        - rows = i
        - columns = j
    If any of these expressions is fulfilled, we add set the respective player as the winner.
    At the end of the function, we check if there is only one winner.
    If there is only one winner, we return the winner.
    If there is no winner or both are winners, we return None, because in conjuction with the terminal function, we can conclude that the game is a draw.
    """
    X_columns_count = [0, 0, 0]
    O_columns_count = [0, 0, 0]
    X_diagonal_count_1 = 0
    O_diagonal_count_1 = 0
    X_diagonal_count_2 = 0
    O_diagonal_count_2 = 0
    X_won = False
    O_won = False
    for i, row in enumerate(board):
        X_row_count = 0
        O_row_count = 0
        for j, cell in enumerate(row):
            if cell == X:
                X_row_count += 1
                X_columns_count[j] += 1
                if i == j:
                    X_diagonal_count_1 += 1
                if 2 - i == j:
                    X_diagonal_count_2 += 1    
            elif cell == O:
                O_row_count += 1
                O_columns_count[j] += 1
                if i == j:
                    O_diagonal_count_1 += 1
                if 2 - i == j:
                    O_diagonal_count_2 += 1 
        if X_row_count == 3:
            X_won = True
        if O_row_count == 3:
            O_won = True
    if 3 in X_columns_count or X_diagonal_count_1 == 3 or X_diagonal_count_2 == 3:
        X_won = True
    if 3 in O_columns_count or O_diagonal_count_1 == 3 or O_diagonal_count_2 == 3:
        O_won = True
    if X_won is True and O_won is False:
        return X
    elif O_won is True and X_won is False:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    In this function we check if the game is over.
    First we check if there is a winner, if there is a winner, we return True.
    If there is no winner, we iterate through the board, checking if there is any empty cell.
    If there is an empty cell, we return False, wich means that the game is not over.
    If there is no empty cell, we return True, wich means that the game is over.
    """
    if winner(board) is not None:
        return True
    else:
        for rows in board:
            if EMPTY in rows:
                return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    This function is mainly used by the minmax algorithm.
    More info in the minmax function.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    This function is the brain of the AI.
    First we check if the game is over, if it is, we return None.
    If it is not, we check if the current player is X or O.
    We have to make this verification because:
        - If the AI plays as X
            - The AI will try to maximize the utility of the board, so it will try to get the highest value possible.
            - The start value that will compare the values will be -infinity.
            - It will use the minvalue function to get the lowest value possible, so it can choose the highest value possible.
            - It will try to reach 1, because its previously defined that X win is 1.
            - The values will range from -1 to 1.
            - With this AI, the value will never be -1, because the AI will always try to win.
        - If the AI plays as O
            - The AI will try to minimize the utility of the board, so it will try to get the lowest value possible.
            - The start value that will compare the values will be infinity.
            - It will use the maxvalue function to get the highest value possible, so it can choose the lowest value possible.
            - It will try to reach -1, because its previously defined that O win is -1.
            - The values will range from -1 to 1.
            - With this AI, the value will never be 1, because the AI will always try to win.
        If the AI play as X, and it is the first move, it will return the center of the board, because it is the best move, arguably.
    """
    if terminal(board) == True:
        return None
    if player(board) == X:
        if board == initial_state():
            return (1, 1)
        value = -math.inf
        optimal_action = None
        for action in actions(board):
            min_value_result = minvalue(result(deepcopy(board), action))
            if min_value_result > value:
                value = min_value_result
                optimal_action = action
    else:
        value = math.inf
        optimal_action = None
        for action in actions(board):
            max_value_result = maxvalue(result(deepcopy(board), action))
            if max_value_result < value:
                value = max_value_result
                optimal_action = action
    return optimal_action


def maxvalue(board):
    '''
    This function is used by the minimax function.
    This function uses recursion with the minvalue function, until it reaches a terminal state.
    The start value that will compare the values will be -infinity.
    It will iterate through the actions, and will call the minvalue function to get the lowest value possible.
    For the result of the minvalue function, it will compare it with the start value, and will choose the highest value possible and will update the start value.
    After, it will return the max value of the actions.
    '''
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, minvalue(result(board, action)))
    return value


def minvalue(board):
    '''
    This function is used by the minimax function.
    This function uses recursion with the maxvalue function, until it reaches a terminal state.
    The start value that will compare the values will be infinity.
    It will iterate through the actions, and will call the maxvalue function to get the highest value possible.
    For the result of the maxvalue function, it will compare it with the start value, and will choose the lowest value possible and will update the start value.
    After, it will return the min value of the actions.
    '''
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, maxvalue(result(board, action)))
    return value
            