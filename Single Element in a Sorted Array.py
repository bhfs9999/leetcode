class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = len(nums)-1
        left = 0
        while left < right:
            mid = (left+right)/2
            if nums[mid] == nums[mid-1]:
                right = mid
            else:
                left = mid
        return nums[mid]