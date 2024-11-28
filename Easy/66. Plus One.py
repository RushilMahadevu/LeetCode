class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        s = int("".join(s))
        s += 1
        x = [int(j) for j in str(s)]
        return x
