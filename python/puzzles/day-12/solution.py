import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    numShapes = 0
    # Shape is represented as a set of points
    shapes = []
    regions = []
    
    # Observation: Always 6 shapes and Always 3x3
    
    points = [] # Start with an empty list of points
    row = 0 # Start at row 0
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            
            if numShapes < 6:
                if line == '':
                    numShapes += 1
                    # Add shape to list
                    shapes.append(set(points))
                elif line[0].isdigit():
                    points = [] # Reset to an empty list (when new label appears)
                    row = 0 # Reset to row 0
                else:
                    # Build the shape
                    for i, c in enumerate(line):
                        if c == '#':
                            points.append((i, row))
                    
                    # Increment row
                    row += 1
                    
            else:
                # Build regions
                size, presents = line.split(':')
                pDict = {}
                for i, n in enumerate(presents.strip().split(' ')):
                    n = int(n)
                    if n:
                        pDict[i] = n
                    
                regions.append(([int(i) for i in size.split('x')], pDict))
    
    """
    for i, shape in enumerate(shapes):
        print(i)
        grid = [['.', '.', '.'] for _ in range(3)]
        
        for x, y in shape:
            grid[y][x] = '#'
        
        for row in grid:
            print(''.join(row))
        
        print()
    """
    
    # Maybe I'll do a general solution (will be hard), trying naive solution where I check if there's enough space in both length and width for the presents to fit
    # Naive solution works for puzzle input, not the example
    for (x, y), presents in regions:
        upperLim = sum(presents.values())
        if (upperLim <= (x * y / 9)):
            score += 1
    
    # Return Accumulator    
    print(score)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
