# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1==None and t2==None:
            return None
        if t1==None:
            t3 = TreeNode(t2.val)
            t3.left = self.mergeTrees(None, t2.left)
            t3.right = self.mergeTrees(None, t2.right)
        elif t2==None:
            t3 = TreeNode(t1.val)
            t3.left = self.mergeTrees(t1.left, None)
            t3.right = self.mergeTrees(t1.right, None)
        else:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)

        return t3