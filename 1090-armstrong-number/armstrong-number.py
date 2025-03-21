class Solution:
    def isArmstrong(self, n: int) -> bool:

        total = 0
        k = len(str(n))
        
        for d in str(n):
            prod = 1
            d = int(d)
            i = 0
            while i < k:
                prod *= d
                i += 1
            total += prod
        return n == total