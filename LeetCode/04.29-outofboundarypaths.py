"""
https://leetcode.com/problems/out-of-boundary-paths/
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
"""

class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        1. memoize startrow, startcolumn and maxmove.
        2. base case: a ball with one move will be out of bounds if startrow/col < -1 or row >= m or col >= n
        3. recursive case: each move consists of one step up down left or right.
        """
        pathsMemo = {} #store set of (maxMove, startRow, startColumn)

        def helper(m, n, maxMove, startRow, startColumn):
            position = (maxMove, startRow, startColumn)
            if position in pathsMemo:
                return pathsMemo[position]

            outofBounds = False
            paths = 0 #number of paths out of bounds

            if startRow < 0 or startRow >= m or startColumn < 0 or startColumn >= n:
                outofBounds = True
            
            if maxMove <= 0 and outofBounds == True:
                paths += 1
            elif maxMove <=0 and outofBounds == False:
                pass
            elif outofBounds == False:
                paths = helper(m,n,maxMove-1,startRow-1,startColumn) \
                    + helper(m,n,maxMove-1,startRow+1,startColumn) \
                    + helper(m,n,maxMove-1,startRow,startColumn-1) \
                    + helper(m,n,maxMove-1,startRow,startColumn+1)
            else: #outofBounds == True
                paths += 1
                
            pathsMemo[position] = paths
            return paths
        return helper(m, n, maxMove, startRow, startColumn)

#Complexity: Time = O(m x n x maxMove). Space = O(m x n x N)

a = Solution()
print(a.findpaths(2,2,2,0,0))