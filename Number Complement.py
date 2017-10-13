class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        len = 1
        while num>>len:
            len += 1
        return (1<<len) - 1 - num