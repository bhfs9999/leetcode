class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = len(set(candies))
        if kinds > len(candies)/2:
            return len(candies) / 2
        else:
            return kinds
