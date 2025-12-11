import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    rack = {}
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            line = line.split(' ')
            # split = ['aaa:', 'bbb', 'bbb']
            rack[line[0][:-1]] = line[1:]
            
    # List of paths
    paths = findAllPaths(rack, 'you')
    #print(*paths, sep='\n')
    
    score = len(paths)
    # Return Accumulator    
    print(score)

# Find all the paths from a given node to the end
def findAllPaths(rack, current, path=[]):
    # Add the current node to the end of the path
    path = path + [current]

    # If the current node is the end, exit
    if current == 'out':
        return [path]

    # If the current node is not in the rack, no paths exist, return an empty list
    if current not in rack:
        return []

    paths = []
    # Loop over all adjacent nodes
    for node in rack[current]:
        # Check if the node is already in the path to avoid cycles
        if node not in path:
            # Recursively find paths from the adjacent node to the end
            paths.extend(findAllPaths(rack, node, path))
    
    return paths
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
