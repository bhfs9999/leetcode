class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        temp = sorted(people, key=lambda item:(item[0], -item[1]), reverse=True)

        res = list()
        for apeople in temp:
            res.insert(apeople[1], apeople)

        return res