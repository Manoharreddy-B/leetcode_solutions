class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        # nums_dict = {}
        # for i, num in enumerate(nums2):
        #     nums_dict[num] = i
        
        # result = [-1]*len(nums1)

        # for i, num in enumerate(nums1):
        #     for j in range(nums_dict[num],len(nums2)):
        #         if nums2[j]>num:
        #             result[i] = nums2[j]
        #             break
        # return result

        nums_dict = {}
        for i, num in enumerate(nums1):
            nums_dict[num] = i
        
        result = [-1]*len(nums1)
        stack = []
        for i,cur in enumerate(nums2):
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums_dict[val]
                result[idx] = cur

            if cur in nums_dict:
                stack.append(cur)
        return result



             

