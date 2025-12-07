import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

debug = False

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    splits = 0
    
    beams = set()
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            for i, c in enumerate(line):
                if c == 'S':
                    beams.add(i)
                if c == '^' and i in beams:
                    splits += 1
                    beams.remove(i)
                    
                    left = i - 1
                    if left >= 0:
                        beams.add(left)
                
                    right = i + 1
                    if right < len(line):
                        beams.add(right)
            
            if debug:
                out = ''.join([c if i not in beams else '|' for i, c in enumerate(line)])
                print(out, end = "\t  | ")
                print(beams)
    
    if not part2:
        score = splits
        
    # Return Accumulator    
    print(score)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
