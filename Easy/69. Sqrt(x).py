# Brute Force Method
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0

#         i = 1
#         while i**2 <= x:
#             i += 1

#         return i - 1


# Refined Method
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r - l) // 2)  # Finding Middle
            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m
        return res
