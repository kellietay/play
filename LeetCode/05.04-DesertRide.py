"""
start with an example with no oasys an no rocks. 
inputs: desert:List[Lists], Gas:int
outputs: True/False

corner cases:
- can the car start from an oasys? no
- gas = 0?: return False
- desert = 1x1: return False
- no oasys?: return False
desert: [
    [".", ".", ".", "o"],
    [".", "r", "r", "."],
    [".", ".", "r", "r"],
    [".", "c", ".", 20],
    ],
    gas: 2,
    expected: true

"""
from collections import deque
def ride(desert, gas):
    desert_x = len(desert)
    desert_y = len(desert[0])

    if (desert_x <= 1 and desert_y <= 1) or gas == 0:
        return False

    car, oasis, station = None, None, None

    #find car, oasys and gas
    for i in range(0,desert_x):
        for j in range(0,desert_y):
            if desert[i][j] == "c":
                car = (i,j)
            elif desert[i][j] == "o":
                oasis = (i,j)
             #finds location of gas and its value
            elif isinstance(desert[i][j],int):
                station = (i,j)
                station_value = desert[i][j]
    
    if not oasis or not car:
        return False

    #can we move to the cell?
    def canMoveTo(x,y,gas_left):
        #cant move if its outside of grid:
        if x >= desert_x or x < 0 or y >=desert_y or y < 0:
            return False
        #cant move if its a rock
        if desert[x][y] == "r":
            return False
        #cant move if its been visited and gas units in previous visit is greater
        if ((x,y) in visited) and (desert[x][y] > gas_left):
            return False
        return True

    #BFS solution with queue
    queue = deque([[car[0],car[1],gas]])
    visited = set() 

    while queue:
        [x, y, gas_left] = queue.popleft()
        current = (x,y)

        #if current is oasis: return true
        if current == oasis:
            return True   
        
        #if current is station: add value of gas to gas. 
        if current == station: 
            gas_left = station_value + gas_left
        
        #update field with the gas_left
        desert[x][y] = gas_left
        visited.add(current)

        #move and add to queue if canMoveTo returns True:
        next_gas_left = gas_left - 1
        if next_gas_left >= 0:
            if canMoveTo(x-1,y,next_gas_left):
                queue.append([x-1,y,next_gas_left])
            if canMoveTo(x+1,y,next_gas_left):
                queue.append([x+1,y,next_gas_left])
            if canMoveTo(x,y-1,next_gas_left):
                queue.append([x,y-1,next_gas_left])
            if canMoveTo(x,y+1,next_gas_left):
                queue.append([x,y+1,next_gas_left])

    return False


desert = [
    [".", ".", ".", "o"],
    [".", "r", "r", "."],
    [".", ".", "r", "r"],
    [".", "c", ".", 20],
    ]

gas = 2
print(ride(desert,gas)) #True

desert1 = [
    [".", ".", ".", "o"],
    [".", "r", "r", "."],
    [".", ".", "r", "r"],
    [".", "c", ".", 5],
    ]

gas1 = 2
print(ride(desert1,gas1)) #False


