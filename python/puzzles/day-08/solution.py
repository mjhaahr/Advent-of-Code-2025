import sys
import os
import math
from functools import cache
import itertools
import heapq

# Modifying Path to include Repo Directory (for util import)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# Import Utilities
import utils

def puzzle(filename, part2):
    # Zero the Accumulator
    score = 0
    
    boxes = []
    
    # Open File
    with open(filename, 'r') as fp:
        # Loop over all lines
        for line in fp.readlines():
            line = line.strip() 
            boxes.append(tuple([int(i) for i in line.split(',')]))
            
    #print(*boxes, sep='\n')
    
    # Solve for the distances first
    # Generate all connections as a list, format: (distance, low node, high node) (nodes by index)
    connections = [(distance(a, b), i, j) for (i, a), (j, b) in itertools.combinations(enumerate(boxes), 2)]
    # print(*connections, sep='\n')
    
    # Create the initial list of circuits with just one box
    circuits = [{i} for i in range(len(boxes))]
    
    if not part2:
        num = 10 if 'example' in filename else 1000
    
        # Get the relevant shortest ones
        shortest = heapq.nsmallest(num, connections, key=lambda x: x[0])
        #print(*shortest, sep='\n')
    
        # Loop over the shortest to build the circuits
        for dist, i, j in shortest:
            # Where the connections are found
            iIdx = -1
            jIdx = -1
    
            # Loop over circuits to check if there's a circuit containing either key
            for idx, circuit in enumerate(circuits):
                if i in circuit:
                    iIdx = idx
                if j in circuit:
                    jIdx = idx
                    
            # If the two indices are not the same, add j's circuit to i's circuit and remove j's circuit
            if iIdx != jIdx:
                circuits[iIdx].update(circuits[jIdx])
                circuits.pop(jIdx)
        
        # print(*circuits, sep='\n')
        sizes = sorted([len(c) for c in circuits], reverse=True)
        score = sizes[0] * sizes[1] * sizes[2]
        
    else:
        # Turn the list of connections into a min heap
        heapq.heapify(connections)
        
        # Loop while there are connections to iterate through (shouldn't be unsolvable, but who knows)
        while connections:
            # Pop the next shortest connection
            dist, i, j = heapq.heappop(connections)
            
            iIdx = -1
            jIdx = -1
    
            # Loop over circuits to check if there's a circuit containing either key
            for idx, circuit in enumerate(circuits):
                if i in circuit:
                    iIdx = idx
                if j in circuit:
                    jIdx = idx
                    
             # If the two indices are not the same, add j's circuit to i's circuit and remove j's circuit
            if iIdx != jIdx:
                circuits[iIdx].update(circuits[jIdx])
                circuits.pop(jIdx)
                
                # If circuits is now one long circuit, assign the score and break
                if len(circuits) == 1:
                    score = boxes[i][0] * boxes[j][0]
                    break
    
    
    # Return Accumulator    
    print(score)
    
def distance(a, b):
    return math.sqrt(sum([(b[i] - a[i])**2 for i in range(3)]))
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
