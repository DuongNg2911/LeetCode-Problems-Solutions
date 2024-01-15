class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash_table = {}
        for i in matches:
            if i[0] not in hash_table.keys():
                hash_table.update({i[0]: 0})
            
            if i[1] not in hash_table.keys():
                hash_table.update({i[1]: 1})
            else:
                hash_table[i[1]] += 1
                
        answer_0 = []
        answer_1 = []

        for w in hash_table.keys():
            if hash_table[w] == 0:
                answer_0.append(w)
            elif hash_table[w] == 1:
                answer_1.append(w)

        hash_table.clear()
        answer_0.sort()
        answer_1.sort()
    
        return [answer_0, answer_1]
