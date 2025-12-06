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
    
    rows = []
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            rows.append(line)
    
    equations = []
    
    # Loop over last row to find the bounds and the operators
    edges = [0]
    for i, c in enumerate(rows[-1]):
        if c == '+' or c == '*':
            equations.append([c])
            if (i > 0):
                edges.append(i) 
                
    edges.append(len(rows[0]))
    
    # Convert stings to numbers (part1 is simple, just take the value, part2 rotates 90)
    if not part2:
        for row in rows[:-1]:
            for i, val in enumerate(row.split()):
                equations[i].append(int(val))
    else:
        for eq, (low, high) in enumerate(zip(edges[:-1], edges[1:])):
            vals = [''] * (high - low - 1)
            for i in range(high - 2, low - 1, -1):
                for row in rows[:-1]:
                    idx = i - low
                    vals[idx] += row[i]
                
            for val in vals:
                equations[eq].append(int(val.strip()))
                    
    for eq in equations:
        if eq[0] == '+':
            score += sum(eq[1:])
        else:
            score += math.prod(eq[1:])
    
    # Return Accumulator    
    print(score)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
