class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = list()
        res = 0
        for aop in ops:
            if aop == "C":
                res -= stack[-1]
                stack.pop()
            elif aop == "D":
                score = stack[-1]*2
                res += stack[-1]*2
                stack.append(score)
            elif aop == "+":
                score = stack[-1] + stack[-2]
                res += score
                stack.append(score)
            else:
                score = int(aop)
                res += score
                stack.append(score)
        
        return res