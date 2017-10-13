class complex(object):
    def __init__(self, real, vitural):
        self.real = real
        self.vitural = vitural
    
    def __mul__(self, other):
        real = self.real*other.real - self.vitural*other.vitural
        vitural = self.real*other.vitural + self.vitural*other.real
        return complex(real, vitural)

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        tempa = a.split("+")
        tempb = b.split("+")
        numa = complex(int(tempa[0]), int(tempa[1][:-1]))
        numb = complex(int(tempb[0]), int(tempb[1][:-1]))
        numc = numa * numb
        res =  "{}+{}i".format(numc.real, numc.vitural)
        return res