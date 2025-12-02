import sys
import os

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Start Accumulator at 0
    score = 0
    
    moves = []
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            offset = int(line[1:])
            moves.append((line[0], offset))
          
    
    # Dial starts at 50
    dial = 50
      
    if not part2:
        for d, offset in moves:
            if d == 'L':
                dial -= offset
            else:
                dial += offset
        
            dial = dial % 100
            # If the Dial ever is exactly 0, the score increases
            if (dial == 0):
                score += 1
    else:
        # Count number of zero crossings
        for d, offset in moves:
            crossings = offset // 100
            offset = offset % 100
            if d == 'L':
                newDial = dial - offset
            else:
                newDial = dial + offset
                
            corDial = newDial % 100
            if (corDial == 0):
                # If the Dial ever is exactly 0, the score increases
                crossings += 1
            elif (dial == 0):
                # Skip a start at 0
                pass
            elif (newDial != corDial):
                # If the mod has been applied, score increases
                crossings += 1
                
            dial = corDial
                
            score += crossings
    
    # Return Accumulator    
    print(score)
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
