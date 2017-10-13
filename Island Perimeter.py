class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        res = 0
        for row in range(r):
            for col in range(c):
                if grid[row][col] == 1:
                    res += col==0 or grid[row][col-1]==0
                    res += col==c-1 or grid[row][col+1]==0
                    res += row==0 or grid[row-1][col]==0
                    res += row==r-1 or grid[row+1][col]==0
        
        return res