# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = list()
        queue = list()
        queue.append(root)
        curlevel = 1
        nextlevel = 0
        curval = curnum = 0.0

        while queue:
            out = queue.pop()
            curlevel -= 1
            curval += out.val
            curnum += 1

            if out.left:
                queue.insert(0, out.left)
                nextlevel += 1
            if out.right:
                queue.insert(0, out.right)
                nextlevel += 1
            
            if curlevel==0:
                res.append(curval/curnum)
                curlevel = nextlevel
                nextlevel = 0
                curval = curnum = 0.0
        return res