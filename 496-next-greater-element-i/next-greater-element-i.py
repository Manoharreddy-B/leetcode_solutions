class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # for i in range(len(nums)):
        #     if i == 0:
        #         stack.append(nums[i])
        #     else:
        #         if nums[i] > nums[i-1]:
        #             stack.append(nums[i])
        
        # for num in 
        nums_dict = {}
        for i, num in enumerate(nums2):
            nums_dict[num] = i
        
        result = [-1]*len(nums1)

        for i, num in enumerate(nums1):
            for j in range(nums_dict[num],len(nums2)):
                if nums2[j]>num:
                    result[i] = nums2[j]
                    break
        return result