class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for c in s:
            print(ord(c))
            if ord(c) <= 122 and ord(c) >= 97:
                ss += c
            elif ord(c) >= 65 and ord(c) <= 90:
                ss += c.lower()
            elif ord(c) >= 48 and ord(c) <= 57:
                ss += c
        i, j = 0, len(ss)-1

        while i < j:
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1
        return True
            
