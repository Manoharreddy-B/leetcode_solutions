class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        dic = {}
        for num in nums:
            if num in dic: 
                dic[num] += 1
                return num
            else:
                dic[num] = 0


'''above  is not exact solution 
exact solution uses floyd's algorithm'''
        