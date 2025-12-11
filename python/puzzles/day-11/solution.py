import sys
import os
from collections import defaultdict
from functools import cache

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

rack = defaultdict(list)
def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            line = line.split(' ')
            # split = ['aaa:', 'bbb', 'bbb']
            rack[line[0][:-1]] = line[1:]
            
    # List of paths
    start = 'you' if not part2 else 'svr'
    score = findAllPaths(start, part2)
    # Return Accumulator    
    print(score)

# Find the number of paths from a given node to the end
# Default Part 2 quantities to False so Part 1 can run without interruption
@cache
def findAllPaths(current, part2=False, fftSeen=False, dacSeen=False):
    # If the current node is the end, exit, return a 1, this is a valid path
    if current == 'out':
        return 1 if not part2 else (fftSeen and dacSeen)

    # If the current node is not in the rack, no paths exist, return a 0, not a solution
    if current not in rack:
        return 0
        
    pathCount = 0
    # Loop over all adjacent nodes
    for node in rack[current]:
        # Recursively find number of paths from the adjacent node to the end
        if not part2:
            pathCount += findAllPaths(node)
        else:
            # If the node is one of the special values, set the flag, 
            if node == 'fft':
                fftSeen = True
            elif node == 'dac':
                dacSeen = True
                
            pathCount += findAllPaths(node, part2, fftSeen, dacSeen)
    
    return pathCount
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
