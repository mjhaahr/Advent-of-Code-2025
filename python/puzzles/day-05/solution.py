import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    ranges = []
    ingredients = []
    
    # Open File
    with open(filename, 'r') as fp:
        readingRanges = True
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            if line == "":
                readingRanges = False
            elif readingRanges:
                low, high = [int(i) for i in line.split('-')]
                ranges.append([low, high])
            else:
                ingredients.append(int(line))
    
    ranges = sorted(ranges, key=lambda x: x[0])
    
    combinedRanges = [ranges[0]]

    lastHigh = combinedRanges[0][1]
    for low, high in ranges[1:]:
        high = max(high, lastHigh)
        if low <= lastHigh + 1:
            combinedRanges[-1][1] = high
        else:
            combinedRanges.append([low, high])
        
        lastHigh = high 
    
    if not part2:
        # Binary Search for each ingredient in the ranges
        score = sum(IsInRange(i, combinedRanges) for i in ingredients)
    else:
        # Sum the span of the ranges
        score = sum(r[1] - r[0] + 1 for r in combinedRanges)
    
    # Return Accumulator    
    print(score)
    
# Recursive Binary Search
def IsInRange(val, ranges):
    l = len(ranges)
    # End Conditions: One range to check
    if l == 1:
        # One range (if in list return true, if not return false)
        return (ranges[0][0] <= val and val <= ranges[0][1])
    elif l == 2:
        # Two range, check both ranges, if in neither, return false
        return (IsInRange(val, ranges[0:1])) or (IsInRange(val, ranges[1:2]))
    else:
        # If more than two ranges, check "center" range and if in, return true, too low return IsInRange for below, and same for high and above
        idx = l // 2
        r = ranges[idx]
        if val < r[0]:
            # Check below
            return IsInRange(val, ranges[0:idx])
        elif val > r[1]:
            # Check above
            return IsInRange(val, ranges[idx + 1:])
        else:
            # Otherwise it's in
            return True
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
