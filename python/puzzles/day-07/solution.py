import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

printTree = False
debug = False

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    splits = 0
    
    paths = []
    
    activeBeams = set()
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        row = 0
        for line in fp.readlines():
            line = line.strip() 
            toRemove = set()
            for i, c in enumerate(line):
                if row == 0:
                    if c == 'S':
                        paths.append(1)
                        activeBeams.add(i)
                    else:
                        paths.append(0)
                
                if c == '^' and i in activeBeams:
                    splits += 1
                    
                    left = i - 1
                    if left >= 0:
                        activeBeams.add(left)
                        paths[left] += paths[i]
                
                    right = i + 1
                    if right < len(line):
                        activeBeams.add(right)
                        paths[right] += paths[i]
                        
                    activeBeams.remove(i)
                    paths[i] = 0
                                
            if printTree:
                out = ''.join(['|' if c == '.' and i in activeBeams else c for i, c in enumerate(line)])
                if debug:
                    print(out, end = f"  | {paths}\n")
                
            row += 1
    
    if not part2:
        score = splits
    else:
        score = sum(paths)
        
        
    # Return Accumulator    
    print(score)
        
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
