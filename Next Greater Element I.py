class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = list()
        mapping = dict(zip(nums, [-1]*len(nums)))
        for num in nums:
            while len(stack)!=0 and stack[-1] < num:
                mapping[stack[-1]] = num
                stack.pop()
            stack.append(num)
        
        for index, num in enumerate(findNums):
            findNums[index] = mapping[num]

        return findNums