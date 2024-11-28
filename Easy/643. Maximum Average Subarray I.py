class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxSum = curSum

        for i in range(k, len(nums)):
            curSum = curSum - nums[i-k] + nums[i]
            maxSum = max(maxSum, curSum)
        
        return maxSum / k
