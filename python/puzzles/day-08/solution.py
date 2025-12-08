import sys
import os
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
    # Generate all connections as a list, format: (distance, low node, high node) (node stored by index)
    connections = [(distance(a, b), i, j) for (i, a), (j, b) in itertools.combinations(enumerate(boxes), 2)]
    # print(*connections, sep='\n')
    
    # Create the initial DSU with each box on it's own circuit (given boxes as indices)
    circuits = DSU(range(len(boxes)))
    
    if not part2:
        num = 10 if 'example' in filename else 1000
    
        # Get the relevant shortest ones
        shortest = heapq.nsmallest(num, connections, key=lambda x: x[0])
        #print(*shortest, sep='\n')
    
        # Loop over the shortest to build the circuits, using the DSU class
        for dist, i, j in shortest:
            # Run the DSU union to connect i and j
            circuits.union(i, j)
        
        # print(*circuits, sep='\n')
        sizes = sorted(circuits.sizes.values(), reverse=True)
        score = sizes[0] * sizes[1] * sizes[2]
        
    else:
        # Turn the list of connections into a min heap
        heapq.heapify(connections)
        # Loop while there are connections to iterate through (shouldn't be unsolvable, but who knows)
        while connections:
            # Pop the next shortest connection
            dist, i, j = heapq.heappop(connections)
            
            circuits.union(i, j)
             
            # If all boxes are connected to each other, assign the score and break
            if circuits.allConnected:
                score = boxes[i][0] * boxes[j][0]
                break
    
    
    # Return Accumulator    
    print(score)
    

# Euclidean Distance Squared (doesn't need the sqrt, and dropping it is faster)  
def distance(a, b):
    return sum([(b[i] - a[i])**2 for i in range(3)])
    
# This is a Disjoint Set Problem, make a class to implement it
class DSU:
    # Initialize all data as discrete circuits
    def __init__(self, data):
        self.parents = {}
        self.sizes = {}
        self.allConnected = False
        self.numNodes = len(data)
        for d in data:
            # Initialize all to a first level
            self.parents[d] = d
            self.sizes[d] = 1  # Size of 1 to start
    
    # Find the Root for a given node (first node of circuit for a given circuit)
    def find(self, x):
        # if x isn't it's own parent, find the root of x
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
      
    # Union two sets  
    def union(self, i, j):
        # Find the root nodes
        i = self.find(i)
        j = self.find(j)
        
        # Exit if the same root (thus in the same set)
        if i == j:
            return
            
        # Ensure i is the larger set
        if self.sizes[i] < self.sizes[j]:
            # swap if i is smaller
            i, j = j, i
            
        # Set j's parent to i
        self.parents[j] = i
        # Update i's size
        self.sizes[i] += self.sizes[j]
        # Check if there's one set
        if self.sizes[i] == self.numNodes:
            self.allConnected = True
    
if __name__ == "__main__":
    # Check number of Arguments, expect 2 (after script itself)
    # Args: input file, part number
    if (len(sys.argv) != 3):
        print(f"Error: Expected 2 arguments, got {len(sys.argv) - 1}")
        
    else:
        puzzle(sys.argv[1], sys.argv[2] == '2')
