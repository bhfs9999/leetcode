class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list()
        words = s.split(" ")
        for aword in words:
            res.append(aword[::-1])
        return " ".join(res)