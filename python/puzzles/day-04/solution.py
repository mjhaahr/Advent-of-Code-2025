import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    rows = []
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            rows.append([c for c in line])
            
    grid = utils.DictGrid(rows)
    
    lastScore = -1
    
    # loop until the score doesn't change
    while (lastScore != score):
        lastScore = score
        toRemove = []
        
        # Loop over the whole grid
        for cell, val in grid:
            # If it's a paper towel
            if (val == '@'):
                # Check the neighbors
                count = 0
                for n in grid.getNeighborsOf8(cell):
                    count += 1 if n[0] == '@' else 0
                
                if count < 4:
                    score += 1
                    toRemove.append(cell)
                    
        # Remove the ones set aside
        for cell in toRemove:
            grid.set(cell, '.')
            
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
