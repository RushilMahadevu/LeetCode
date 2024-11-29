class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curSum = 0
        maxSum = 0

        for i in range(len(gain)):
            curSum += gain[i]
            maxSum = max(maxSum, curSum)
        return maxSum
