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
    
    towels = set()
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        y = 0
        for line in fp.readlines():
            line = line.strip() 
            for x, c in enumerate(line):
                if c == '@':
                    towels.add((x, y))
            
            y += 1
            
    lastScore = -1
    
    # loop until the score doesn't change
    while (lastScore != score):
        lastScore = score
        toRemove = []

        for towel in towels:
            towelsInNeighbors = 0
            removable = True
            # Get all Surrounding Cells
            for offset in itertools.product([-1, 0, 1], [-1, 0, 1]):
                # If at the center, skip
                if offset == (0, 0):
                    continue
            
                newCell = tuple(map(sum, zip(towel, offset)))
                if newCell in towels:
                    towelsInNeighbors += 1
                
                if towelsInNeighbors >= 4:
                    removable = False
                    break
        
            if removable:
                score += 1
                toRemove.append(towel)
            
        # Remove the ones set aside
        for cell in toRemove:
            towels.remove(cell)
            
        # Run once if part 1
        if not part2:
            break
            
    # Return Accumulator  
    print(score)
    
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
