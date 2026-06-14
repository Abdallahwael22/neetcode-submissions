# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        s=[[root,1]]
        maximum=0
        while s:
            node,depth=s.pop()
            maximum=max(maximum,depth)
            if node.left:
                s.append([node.left,depth+1])
            if node.right:
                s.append([node.right,depth+1])


        return maximum