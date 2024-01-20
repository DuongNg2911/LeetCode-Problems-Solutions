class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum_ = 0
        stack = []

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i-j
                sum_ += (m * left * right)
            stack.append((i, n))
        
        for i in range(len(stack)):
            j, m = stack[i]
            left = j - stack[i-1][0] if i > 0 else j + 1
            right = len(arr) - j 
            sum_ += (m * left * right) 
          
        return sum_ % (10**9+7)
