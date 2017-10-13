class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = list()
        for word in words:
            wordset = set(word.lower())
            found = False
            for aline in keyboard:
                if wordset & aline == wordset:
                    found = True
                    break
            if found:
                res.append(word)
        
        return res