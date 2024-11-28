class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        l = s[len(s)-1]
        return len(l)
