# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self,r,t):
        if not r and not t:
            return True
        if r and t and r.val== t.val:
            return(self.isSameTree(r.right,t.right) and self.isSameTree(r.left,t.left))
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root,subRoot) :
            return True
        return (self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot))

