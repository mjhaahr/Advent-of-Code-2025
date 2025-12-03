import sys
import os
import re


# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    ranges = []
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            
            ranges = line.split(',')
            
    pattern = re.compile(r"^(\d+)\1$") if not part2 else re.compile(r"^(\d+)\1+$")
            
    for r in ranges:
        low, high = r.split('-')
        
        for i in range(int(low), (int(high) + 1)):
            string = str(i)
            if pattern.search(string) is not None:
                score += i
    
    # Return Accumulator    
    print(score)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
