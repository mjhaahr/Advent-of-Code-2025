import sys
import os
import itertools

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    corners = []
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip()
            corners.append([int(i) for i in line.split(',')]) 
    
    maxA = 0
    # Loop over all combinations to find the one with the greatest area
    for a, b in itertools.combinations(corners, 2):
        area = calcArea(a, b)
        if area > maxA:
            maxA = area
            
    score = maxA
    
    # Return Accumulator    
    print(score)
    
def calcArea(a, b):
    l = [(max(a[i], b[i]) - min(a[i], b[i]) + 1) for i in range(2)]
    
    return l[0] * l[1]
    
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
