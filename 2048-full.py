"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    
    # line_copy will now contain the list with all the non-zero
    # elements slid over to the beginning
    line_copy = rearrange(line)
    
    # line merged will now hold a copy of rearranged list
    line_merged = list(line_copy)
    
    # code to iterate over the list and merge tiles
    for idx in range(len(line_copy) - 1):
        if line_merged[idx] == line_merged[idx + 1]:
            line_merged[idx] = 2 * line_merged[idx]
            line_merged[idx + 1] = 0
    
    # rearrange the tiles after merging
    line_merged_rearranged = rearrange(line_merged)

    return line_merged_rearranged

# rearrange function for a list
def rearrange(line):
    """
    Function that re-arranges the list to have all non-zero elemnts
    first followed by a set number of zeroes
    """
    line_copy = [0] * len(line)
    line_copy_idx = 0
    
    for idx in range(len(line)):
        if line[idx] != 0:
            line_copy[line_copy_idx] = line[idx]
            line_copy_idx += 1
    return line_copy


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # initialise the height and width of the 2048 board
        self._grid_height = grid_height
        self._grid_width = grid_width
        
        # call the reset method to create an empty grid except
        # for two initial tiles
        self.reset()
              
        # compute the initial lists for all the directions
        self._initial_list = { UP : self.traverse_grid((0, 0), (0, 1), self._grid_width),
                               DOWN : self.traverse_grid((self._grid_height -1, 0), (0, 1), self._grid_width),
                               LEFT : self.traverse_grid((0, 0), (1, 0), self._grid_height),
                               RIGHT : self.traverse_grid((0, self._grid_width - 1), (1, 0), self._grid_height)}
        
        print self._initial_list
        
    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction and generates a list containing 
        touple of index
        """
        traverse_list = []
    
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            traverse_list.append((row, col))
        
        return traverse_list

    def traverse_grid_value(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction and generates a list containing 
        touple of index
        """
        traverse_list = []
    
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            traverse_list.append(self._grid[row][col])
        
        return traverse_list

    def traverse_grid_store(self, start_cell, direction, num_steps, merged_list):
        """
        Function that iterates through the cells in a grid
        in a linear direction and generates a list containing 
        touple of index
        """
 
        idx = 0
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self._grid[row][col] = merged_list[idx]
            idx += 1
    
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # create an empty list with all 0s
        self._grid = [[0 * (row + col) for col in range(self._grid_width)]
                      for row in range(self._grid_height)]
        # call method to initialise two of the tiles of the grid
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_string = ""
        
        for row in range(self._grid_height):
            grid_string += str(self._grid[row]) + "\n"
            
        return grid_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        before = self.__str__()
        for tiles in self._initial_list[direction]:
            if direction == UP or direction == DOWN:
                temp_list = self.traverse_grid_value(tiles, OFFSETS[direction], self._grid_height)
            elif direction == LEFT or direction == RIGHT:
                temp_list = self.traverse_grid_value(tiles, OFFSETS[direction], self._grid_width)
            temp_list = merge(temp_list)
            
            if direction == UP or direction == DOWN: 
                self.traverse_grid_store(tiles, OFFSETS[direction], self._grid_height, temp_list)
            elif direction == LEFT or direction == RIGHT:
                self.traverse_grid_store(tiles, OFFSETS[direction], self._grid_width, temp_list)
        after = self.__str__()
        if before != after:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_index = []        
        
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._grid[row][col] == 0:
                    empty_index.append((row, col))
                    
        pos = random.choice(empty_index)
        
        if random.random() < 0.9:
            self._grid[pos[0]][pos[1]] = 2
        else:
            self._grid[pos[0]][pos[1]] = 4
                   
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(5, 6))
