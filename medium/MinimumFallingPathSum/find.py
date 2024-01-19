class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for r in range(1, len(matrix)):
            for c in range(0, len(matrix[0])):
                if c - 1 < 0:
                    matrix[r][c] = min(matrix[r-1][c] + matrix[r][c], matrix[r-1][c+1]+matrix[r][c])
                elif c + 1 == len(matrix[0]):
                    matrix[r][c] = min(matrix[r-1][c] + matrix[r][c], matrix[r-1][c-1]+matrix[r][c])
                else:
                    matrix[r][c] = min(matrix[r-1][c] + matrix[r][c], matrix[r-1][c-1]+matrix[r][c], matrix[r-1][c+1]+matrix[r][c])

        return min(matrix[-1])
