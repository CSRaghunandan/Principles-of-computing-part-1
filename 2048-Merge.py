
"""
Merge function for 2048 game
"""

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
