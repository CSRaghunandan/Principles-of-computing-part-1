"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for idx in range(1, len(self._board)):
            if self._board[idx] != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        move_in_range = 0 < house_num < len(self._board)
        index_is_right = house_num == self._board[house_num]
        return move_in_range and index_is_right
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            for idx in range(0, house_num):
                self._board[idx] += 1
            self._board[house_num] = 0

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for idx in range(1, len(self._board)):
            if self._board[idx] == idx:
                return self._board[idx]
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """        
        board_copy = SolitaireMancala()
        board_copy.set_board(self._board)
        
        moves_list = []
        
        while board_copy.choose_move() != 0:
            chosen_move = board_copy.choose_move()
            if board_copy.is_legal_move(chosen_move):
                moves_list.append(chosen_move)
                board_copy.apply_move(chosen_move)
        
        return moves_list

