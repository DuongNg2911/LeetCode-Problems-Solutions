class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_ = {}
        result = []
        for i in nums:
            if i not in hash_.keys():
                hash_.update({i:1})
            else:
                hash_[i] += 1
        continue_ = True
        
        while continue_:
            n = []
            for y in hash_.keys():
                if hash_[y] > 0:
                    n.append(y)
                    hash_[y] -= 1

            if len(n) != 0:
                result.append(n)
            else:
                continue_ = False

        return result
