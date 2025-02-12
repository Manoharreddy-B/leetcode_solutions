# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # def checking(p,q):
        #     if not p and not q:
        #         return True
        #     elif not p and q:
        #         return False
        #     elif p and not q:
        #         return False
        #     left_p, left_q  = p.left, q.left
        #     boolean_left = checking(left_p, left_q)
        #     if left_p and left_q:
        #         if left_p.val != left_q.val:
        #             boolean_left = False
            
        #     right_p, right_q = p.right, q.right
        #     boolean_right = checking(right_p, right_q)
        #     if right_p and right_q:
        #         if right_p.val != right_q.val:
        #             boolean_right  = False

        #     boolean = boolean_left and boolean_right
        #     return boolean
        # if p and q:
        #     return checking(p,q) and p.val == q.val
        # else:
        #     return checking(p,q)
                    