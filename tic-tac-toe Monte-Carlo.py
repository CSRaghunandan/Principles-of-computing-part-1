"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

def mc_trial(board, player):
    """
    This function takes the current board and the next player to move.
    This function should play a game starting with the given player, 
    by making random moves starting alternating btw the players
    function returns when the game is over
    """
    
    # get all the empty squares in which a player can make a move
    empty_list = board.get_empty_squares()
    size_empty_list = len(empty_list)
    
    # iterate through all the elements in the empty list
    for idx in range(size_empty_list):                             
        # check if game is over, if so, return.
        if board.check_win() == None:
            # get a random index in the empty list
            random_idx = empty_list[random.randrange(0, size_empty_list)]
            
            if player == provided.PLAYERX:
                board.move(random_idx[0], random_idx[1], provided.PLAYERX)
            else:
                board.move(random_idx[0], random_idx[1], provided.PLAYERO)
            
            # switch the player after making a move
            player = provided.switch_player(player)
            # remove the square in which the player moved from the empty list
            empty_list.remove(random_idx)
            # decrement the size after removing an element
            size_empty_list -= 1
            idx = idx
            
def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores( a list of list) with 
    the same dimension as board, a completed board and which player
    the machine is. The function should score the completed board
    and update the scores grid
    """
    
    # iterate the board and update the score accordingly
    for row_idx in range(board.get_dim()):
        for col_idx in range(board.get_dim()):
            # if the player wins
            if board.check_win() == player:
                if board.square(row_idx, col_idx) == player:
                    scores[row_idx][col_idx] += SCORE_CURRENT
                elif board.square(row_idx, col_idx) == provided.EMPTY:
                    scores[row_idx][col_idx] += 0
                else:
                    scores[row_idx][col_idx] -= SCORE_OTHER
                    
            # if the board is a draw, return doing nothing
            elif board.check_win() == provided.DRAW:
                return
            
            # if the player loses
            else:
                if board.square(row_idx, col_idx) == player:
                    scores[row_idx][col_idx] -= SCORE_CURRENT
                elif board.square(row_idx, col_idx) == provided.EMPTY:
                    scores[row_idx][col_idx] += 0
                else:
                    scores[row_idx][col_idx] += SCORE_OTHER
                        
        
def get_best_move(board, scores):
    """
    This function takes the current board and a grid of scores.
    This function should find all the empty squares with the max
    score and return one of them.
    """
    # if the board has no empty squares, return doing nothing
    if len(board.get_empty_squares()) == 0:
        return
    
    # temporary variables
    empty_scores = []
    max_list = []    
    # get all the indices where it's empty
    empty_list = board.get_empty_squares()
    
    # find the max element
    for elem in empty_list:
        empty_scores.append(scores[elem[0]][elem[1]])        
    max_elem = max(empty_scores)
    
    # get all the places where 
    for idx in empty_list:
        if scores[idx[0]][idx[1]] == max_elem:
            max_list.append((idx[0], idx[1]))
            
    return random.choice(max_list)

def mc_move(board, player, trials):
    """
    This function takes the current board, which player the machine
    is, the number of trails to perform. This function should return
    the best move that the machine player should perform in the form
    of a touple (row, col)
    """
    temp_board = board.clone()
    scores_list = [[0 * (row_idx + col_idx) for col_idx in range(temp_board.get_dim())]
                      for row_idx in range(temp_board.get_dim())]
    
    for idx in range(trials):  
        # play a random game
        mc_trial(temp_board, player)
        # score that agame 
        mc_update_scores(scores_list, temp_board, player)
        temp_board = board.clone()
        idx = idx
        
    return get_best_move(board, scores_list)
        
        
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
