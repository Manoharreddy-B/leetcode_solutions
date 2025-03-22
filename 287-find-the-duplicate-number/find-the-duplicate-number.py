class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if not nums:
        #     return None
        # dic = {}
        # for num in nums:
        #     if num in dic: 
        #         dic[num] += 1
        #         return num
        #     else:
        #         dic[num] = 0

        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast

'''above  is not exact solution 
exact solution uses floyd's algorithm
because problem asks you to solve without using extra space'''
        