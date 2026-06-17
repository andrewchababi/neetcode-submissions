# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None: return (True, 0)

            l_b, l_h = dfs(root.left)
            r_b, r_h = dfs(root.right)

            if (l_b is False) or (r_b is False):
                return False, 0

            return abs(l_h - r_h) <= 1, max(l_h, r_h) + 1

        res, _ = dfs(root)
        return res
        