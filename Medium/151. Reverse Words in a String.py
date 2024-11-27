class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        x = x[::-1]
        x = " ".join(x)
        return x