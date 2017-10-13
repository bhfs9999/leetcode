class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row = len(nums)
        col = len(nums[0])
        res = [[]]
        if row*col == r*c:
            crow = ccol = 0
            for arow in nums:
                for anum in arow:
                    res[crow].append(anum)
                    ccol += 1
                    if ccol == c:
                        crow += 1
                        ccol = 0
                        if crow == r:
                            return res
                        res.append([])
            return res
        else:
            return nums

test = Solution()
print test.matrixReshape([[1,2],[3,4]], 4, 1)