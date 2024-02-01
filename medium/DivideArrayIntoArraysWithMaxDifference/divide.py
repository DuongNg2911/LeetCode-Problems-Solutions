class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for n in range(0, len(nums)-2, 3):
            if nums[n+2] - nums[n] <= k:
                res.append(nums[n:n+3])
            else:
                return []
        return res
