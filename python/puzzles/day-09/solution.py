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
            
    areas = [] # Store the areas and what corners make them up, used for part 2
    maxA = 0
    # Loop over all combinations to find the one with the greatest area
    for a, b in itertools.combinations(corners, 2):
        area = calcArea(a, b)
        areas.append((area, a, b))
        if area > maxA:
            maxA = area
    
    # Score for Part 1 is just the max area
    if not part2:   
        score = maxA    
    else:
        # Sort the areas list, by max val, meaning that the first one seen that's valid will be the largest
        areas.sort(key=lambda x: x[0], reverse=True)
        
        # Loop over all rectangles
        for (area, (ax, ay), (bx, by)) in areas:
            # Sort the coordinates so the validity test is always running over the correct points
            x1, x2 = sorted([ax, bx])
            y1, y2 = sorted([ay, by])
            
            # Validity is proof by contradiction
            valid = True
        
            # Loop over lines (pairs of corners) (adding the first corner to the end to get a loop)
            # To check if the rectangle is valid
            corners.append(corners[0])
            for (l1x, l1y), (l2x, l2y) in itertools.pairwise(corners):
                # Sort the lines, so the validity check holds
                minX, maxX = sorted([l1x, l2x])
                minY, maxY = sorted([l1y, l2y])
                
                # Validity check: if the line is intersected by the boxes bounds or that the box is out of the include area
                # if invalid, break and try next
                if not (maxX <= x1 or x2 <= minX or maxY <= y1 or y2 <= minY):
                    valid = False
                    break
            
            # If the rectangle is valid, assign the score and break
            if valid:
                score = area
                break
        
    
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
