# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = root.val
        queue = list()
        queue.append(root)
        curlevel = 1
        nextlevel = 0
        while queue:
            out = queue.pop()
            curlevel -= 1  

            if out.left:
                queue.insert(0, out.left)
                nextlevel += 1
            if out.right:
                queue.insert(0, out.right)
                nextlevel += 1
            
            if curlevel == 0 and nextlevel != 0:
                curlevel = nextlevel
                nextlevel = 0
                res = queue[-1].val
        
        return res