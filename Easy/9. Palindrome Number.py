# String Method
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         digits = [int(digit) for digit in str(x)]

#         return digits == digits[::-1]


# Fast String Method
# class Solution:
#     def isPalindrome(self, x: int) -> bool:

#         x = str(x)
#         y = x[::-1]

#         if x == y:
#             return True
#         return False


# No String Method
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x >= 10 * div:  # Make div as big as possible (1000 for 1221)
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False

            x = (x % div) // 10  # Chop off side values (1221 to 22)
            div /= 100

        return True
