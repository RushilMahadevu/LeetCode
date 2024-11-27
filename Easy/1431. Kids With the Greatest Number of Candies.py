class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = 0
        n = len(candies)
        result = []
        largest = max(candies)

        for i in range(n):
            current = candies[i]
            current += extraCandies
            if current >= largest:
                result.append(True)
            else:
                result.append(False)
        return result
