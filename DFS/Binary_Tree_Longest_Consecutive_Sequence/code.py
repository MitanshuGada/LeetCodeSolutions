# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def recurse(prevVal, longestSeq, node):
            nonlocal res
            if prevVal + 1 == node.val:
                longestSeq += 1
                res = max(res, longestSeq)
            else:
                longestSeq = 1

            if node.left:
                recurse(node.val, longestSeq, node.left)

            if node.right:
                recurse(node.val, longestSeq, node.right)
        
        longestSeq = 1
        res = 1
        
        recurse(root.val, longestSeq, root)

        return res
"""
Time Complexity: O(N)
Space Complexity: O(N) => function calls
"""