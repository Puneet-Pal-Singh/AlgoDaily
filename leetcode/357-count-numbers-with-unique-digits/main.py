"""
    1st approach: math

    Time  O(n)
    Space O(1)
    20 ms, faster than 66.67% 
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        total, start = 10, 9
        for i in range(1, n):
            start = start*(10-i)
            total += start
        return total
