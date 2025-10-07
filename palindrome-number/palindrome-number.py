from math import trunc
from operator import truediv


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if ( x < 0 or (x % 10 == 0 and x !=0)):
            return False
        reverse = 0
        while (x > reverse):
            reverse = reverse * 10 + x % 10
            x = x // 10
        return (reverse == x) or (x == reverse // 10 )




print(Solution().isPalindrome(-12231))