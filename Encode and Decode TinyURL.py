class Codec:
    def __init__(self):
        self.urllist = list()

    def getSingle(self, achar):
        if '0' <= achar <= '9':
            return ord(achar) - ord('0')
        if 'a' <= achar <='z':
            return ord(achar) - ord('a') + 10
        if 'A' <= achar <= 'Z':
            return ord(achar) - ord('A') + 36

    def getindex(self, shortUrl):
        index = 0
        for achar in shortUrl:
            index = index*62 + self.getSingle(achar)
        return index

    def createSingle(self, index):
        if 0 <= index <= 9:
            return chr(ord('0')+index)
        if 10 <= index <= 35:
            return chr(ord('a')+index)
        if 36 <= index <= 61:
            return chr(ord('A')+index)

    def creater(self, index):
        result = ""
        while index!=0:
            rem = index%62
            result += self.createSingle(rem)
            index /= 62

        return result[::-1]

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        found = False
        index = 0
        for index, url in enumerate(self.urllist):
            if url==longUrl:
                found = True
                break
        
        if found:
            return self.creater(index)
        else:
            shorturl = self.creater(len(self.urllist))
            self.urllist.append(longUrl)
            return shorturl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        index = self.getindex(shortUrl)
        return self.urllist[index]

# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
res = codec.decode(codec.encode(url))
print res