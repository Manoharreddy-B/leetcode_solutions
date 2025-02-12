# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def inside(root):
            if not root:
                return (True, 0)
            
            left_balanced, left_len = inside(root.left)
            right_balanced, right_len = inside(root.right)
            if left_balanced and right_balanced and abs(left_len-right_len)<=1:
                return (True, max(left_len, right_len)+1)
            else:
                return(False, max(left_len, right_len)+1)
        return inside(root)[0]
            