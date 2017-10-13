class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = sorted(nums)
        count = 0
        for i in range(len(res)/2):
            count += res[i*2]
        return count