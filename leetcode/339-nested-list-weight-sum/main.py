"""
    1st approach: recursive dfs

    Time  O(n)
    Space O(h)
    20 ms, faster than 83.54%
"""


class Solution(object):

    def __init__(self):
        self.result = 0

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.dfs(nestedList, 1)
        return self.result

    def dfs(self, arr, depth):
        for x in arr:
            if x.isInteger():
                self.result += depth * x.getInteger()
            else:
                self.dfs(x.getList(), depth + 1)


"""
    1st approach: iterative dfs

    Time  O(n)
    Space O(h)
    20 ms, faster than 83.54%
"""


class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        result = 0
        stack = []
        stack.append((nestedList, 1))
        while len(stack) > 0:
            arr, depth = stack.pop()
            for x in arr:
                if x.isInteger():
                    result += depth * x.getInteger()
                else:
                    stack.append((x.getList(), depth + 1))
        return result
