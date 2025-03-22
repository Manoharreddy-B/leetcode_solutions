class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            if n == 1:
               return True
            n = self.helper(n)

        return False
    
    def helper(self, n):
        total = 0
        n_str = str(n)
        for num in n_str:
            total += int(num)**2
        return total
        

