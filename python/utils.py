import itertools

class Grid:
    def __init__(self, grid):
        self.bounds = [len(grid[0]) - 1, len(grid) - 1]
        self.grid = grid
        self.__gridIter = iter(grid)
    
    # Returns item at grid cell, else returns None
    def get(self, x, y = 0):
        # Pull out coords from a tuple or list
        if (type(x) == list or type(x) == tuple):
            y = x[1]
            x = x[0]
        
        # If at a bounds, skip, cannot be valid there
        if x < 0 or y < 0 or x > self.bounds[0] or y > self.bounds[1]:
            return None
        else:
            return self.grid[y][x]
    
    # Attempts to set a value, if cannot, returns false   
    def set(self, x, y, val = 0):
        # Pull out coords from a tuple or list
        if (type(x) == list or type(x) == tuple):
            val = y
            y = x[1]
            x = x[0]
            
        # If at a bounds, skip, cannot be valid there
        if x < 0 or y < 0 or x > self.bounds[0] or y > self.bounds[1]:
            return False
        else:
            self.grid[y][x] = val
            return True
        
    def __str__(self):
        rowStrs = []
        for row in self.grid:
            rowStrs.append("".join(list(str(i) for i in row)))
            
        return f"Grid:\nBounds: [0, 0] to {self.bounds}\n  {"\n  ".join(rowStrs)}\n"
        
    def __repr__(self):
        return str(self)
        
    def __iter__(self):
        return self
        
    def __next__(self):
        return next(self.__gridIter)
        
    # returns all neighbors (of 8) in the format [val, x, y, offsetX, offsetY]
    def getNeighborsOf8(self, x, y=0):
        # Pull out coords from a tuple or list
        if (type(x) == list or type(x) == tuple):
            val = y
            y = x[1]
            x = x[0]
            
        neighbors = []
        # Get all Surrounding Cells
        for j in [-1, 0, 1]:
            for i in [-1, 0, 1]:
                # If at the center, skip
                if i == 0 and j == 0:
                    continue
                
                newX = x + i
                newY = y + j
                neighbors.append([self.get(newX, newY), newX, newY, i, j])
        
        return neighbors
        
    # returns all valid neighbors (of 4) in the format [[val, x, y, offsetX, offsetY] (order is U, L, D, R)
    def getNeighborsOf4(self, x, y=0):
        # Pull out coords from a tuple or list
        if (type(x) == list or type(x) == tuple):
            val = y
            y = x[1]
            x = x[0]
            
        neighbors = []
        # Get all Surrounding Cells
        for i, j in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            newX = x + i
            newY = y + j
            neighbors.append([self.get(newX, newY), newX, newY, i, j])
        
        return neighbors
    
    # returns all valid neighbors (of 4 Rotated) in the format [val, x, y, offsetX, offsetY] (order is UL, UR, DL, DR)
    def getNeighborsOf4Rot(self, x, y=0):
        # Pull out coords from a tuple or list
        if (type(x) == list or type(x) == tuple):
            val = y
            y = x[1]
            x = x[0]
            
        neighbors = []
        # Get all Surrounding Cells
        for j in [-1, 1]:
            for i in [-1, 1]:
                newX = x + i
                newY = y + j
                neighbors.append([self.get(newX, newY), newX, newY, i, j])
        
        return neighbors
    
class DictGrid:
    def __init__(self, grid):
        self.bounds = [len(grid[0]) - 1, len(grid) - 1]
        self.grid = {(x, y): grid[y][x] for x, y in itertools.product(range(len(grid[0])), range(len(grid)))}
    
    # Returns item at grid cell, else returns None
    def get(self, cell, y = 0):
        # Pull out coords from a tuple or list
        if (type(cell) == tuple):
            pass
        elif (type(cell) == list):
            cell = (cell[0], cell[1])
        else:
            cell = (cell, y)
        
        # If at a bounds, skip, cannot be valid there
        return self.grid.get(cell, None)
    
    # Attempts to set a value, if cannot, returns false   
    def set(self, cell, y, val = 0):
        # Pull out coords from a tuple or list
        if (type(cell) == tuple):
            val = y
        elif (type(cell) == list):
            cell = (cell[0], cell[1])
            val = y
        else:
            cell = (cell, y)
            
        # If at a bounds, skip, cannot be valid there
        if cell in self.grid:
            self.grid[cell] = val
            return True
        else:
            return False
        
    def __str__(self):
        rowStrs = []
        for y in range(self.bounds[1] + 1):
            rowStrs.append("".join([self.grid.get((x, y)) for x in range(self.bounds[0] + 1)]))
            
        return f"Grid:\nBounds: [0, 0] to {self.bounds}\n  {"\n  ".join(rowStrs)}\n"
        
    def __repr__(self):
        return str(self)
        
    def __iter__(self):
        self.__gridIter = iter(self.grid.items())
        return self
        
    def __next__(self):
        return next(self.__gridIter)
        
    # returns all neighbors (of 8) in the format [val, newCell, offset]
    def getNeighborsOf8(self, cell, y=0):
        # Pull out coords from a tuple or list
        if (type(cell) == tuple):
            pass
        elif (type(cell) == list):
            cell = (cell[0], cell[1])
        else:
            cell = (cell, y)
            
        neighbors = []
        # Get all Surrounding Cells
        for offset in itertools.product([-1, 0, 1], [-1, 0, 1]):
            # If at the center, skip
            if offset == (0, 0):
                continue
            
            newCell = tuple(map(sum, zip(cell, offset)))
            neighbors.append([self.get(newCell), newCell, offset])
    
        return neighbors
        
    # returns all valid neighbors (of 4) in the format [val, newCell, offset] (order is U, R, D, L)
    def getNeighborsOf4(self, cell, y=0):
        # Pull out coords from a tuple or list
        if (type(cell) == tuple):
            pass
        elif (type(cell) == list):
            cell = (cell[0], cell[1])
        else:
            cell = (cell, y)
            
        neighbors = []
        # Get all Surrounding Cells
        for offset in dirList:
            newCell = tuple(map(sum, zip(cell, offset)))
            neighbors.append([self.get(newCell), newCell, offset])
        
        return neighbors
    
    # returns all valid neighbors (of 4 Rotated) in the format [val, newCell, offset] (order is UL, UR, DL, DR)
    def getNeighborsOf4Rot(self, cell, y=0):
        # Pull out coords from a tuple or list
        if (type(cell) == tuple):
            pass
        elif (type(cell) == list):
            cell = (cell[0], cell[1])
        else:
            cell = (cell, y)
            
        neighbors = []
        # Get all Surrounding Cells
        for offset in itertools.product([-1, 1], [-1, 1]):
            newCell = tuple(map(sum, zip(cell, offset)))
            neighbors.append([self.get(newCell), newCell, offset])
        
        return neighbors
        
dirList = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def addDir(cell, d):
    return (cell[0] + d[0], cell[1] + d[1])

def getRight(d):
    d = (d[0], d[1])
    idx = dirList.index(d)
    idx = (idx + 1) % 4
    return dirList[idx]
    
    
def getLeft(d):
    d = (d[0], d[1])
    idx = dirList.index(d)
    idx = (idx + 3) % 4
    return dirList[idx]
            
