import sys

"""
    1st: intervals
    - create intervals and check if the current item is within any one of the intervals

    e.g. [5 6 4 7 3 8 2 9]
    intervals = [(5,6), (4,7), (3,8), (2,9)]
    if there is a 8, it will be within the last interval, 2 < 8 < 9

    Time    O(n^2)
    Space   O(n)
    TLE 93/95
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        intvs = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                if start < i - 1:
                    intvs.append([nums[start], nums[i-1]])
                start = i
            for a, b in intvs:
                if a < nums[i] < b:
                    return True
        return False


"""
    2nd: stack, learned from others
    - see ./idea.jpeg
    ref:
    - #4 in https://leetcode.com/problems/132-pattern/solution/

    Time    O(n)
    Space   O(n)
    148 ms, faster than 20.87%
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        mins = [nums[0]]
        minVal = nums[0]
        for i in range(1, len(nums)):
            minVal = min(minVal, nums[i])
            mins.append(minVal)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if mins[i] < nums[i]:
                while len(stack) > 0 and stack[-1] <= mins[i]:
                    stack.pop()
                if len(stack) > 0 and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
