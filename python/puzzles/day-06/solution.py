import sys
import os
import re
import math


# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

pattern = re.compile(r"")

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    equations = []
    
    first = True
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip()
            
            for i, val in enumerate(line.split()):
                if first:
                    equations.append([int(val)])
                else:
                    # Separate digits
                    val = val if not val.isdigit() else int(val)
                    equations[i].append(val)
                    
            first = False
                    
    for eq in equations:
        if eq[-1] == '+':
            score += sum(eq[:-1])
        else:
            score += math.prod(eq[:-1])
    
    # Return Accumulator    
    print(score)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
