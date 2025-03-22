class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.helper(n)
            if n == 1:
               return True
        return False
    
    def helper(self, n):
        # total = 0
        # n_str = str(n)
        # for num in n_str:
        #     total += int(num)**2
        # return total

        total = 0
        while n:
            digit = n%10
            digit = digit**2
            total += digit
            n = n//10
        return total
        

