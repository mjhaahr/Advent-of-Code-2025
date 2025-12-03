import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            score += calcJoltage(line, part2)
    
    # Return Accumulator    
    print(score)
    
    
def calcJoltage(bank, part2):
    # Highest Joltage is highest value + highest value to the right of that (+ repeating for the next values)

    joltage = ""
    offset = 12 if part2 else 2
    idx = 0
    
    # Next Highest Value is max of the string minus the remaining indices (from the start index)
    for i in range(offset - 1, -1, -1):
        subBank = bank[idx:-i] if i > 0 else bank[idx:]
        
        val = max(subBank)
        joltage += val
        
        idx = subBank.index(val) + idx + 1
        
    return int(joltage)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
