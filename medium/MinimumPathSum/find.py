class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
        
        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]
        
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                grid[r][c] = min(grid[r-1][c] + grid[r][c], grid[r][c-1]+grid[r][c])
        
        return grid[-1][-1]
