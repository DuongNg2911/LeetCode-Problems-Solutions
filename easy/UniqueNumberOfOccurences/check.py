class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_ = {}
        occurences = []
        for i in arr:
            if i in hash_.keys():
                hash_[i] += 1
            else:
                hash_.update({i: 1})
        
        for value in list(hash_.values()):
            if value not in occurences:
                occurences.append(value)
            else:
                return False

        return True
