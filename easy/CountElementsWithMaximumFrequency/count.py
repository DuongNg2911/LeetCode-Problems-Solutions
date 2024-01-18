class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_ = {}
        for i in nums: 
            if i not in hash_.keys():
                hash_.update({i: 1})
            else:
                hash_[i] += 1
        
        current_max = 0
        sum_ = 0
        for key in hash_.keys():
            if hash_[key] == current_max:
                sum_ += hash_[key]
            elif hash_[key] > current_max:
                current_max = hash_[key]
                sum_ = hash_[key]
        return sum_
