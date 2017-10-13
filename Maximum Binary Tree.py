class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def getMaxIndex(self, nums):
        maxnum = 0
        maxindex = 0
        for i, val in enumerate(nums):
            if val > maxnum:
                maxnum = val
                maxindex = i
        return maxindex

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        maxindex = self.getMaxIndex(nums)
        leftnums = nums[:maxindex]
        rightnums = nums[maxindex+1:]
        root = TreeNode(nums[maxindex])
        root.left = self.constructMaximumBinaryTree(leftnums)
        root.right = self.constructMaximumBinaryTree(rightnums)
        return root