# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()
        l=[]
        q.append(root)
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                output=q.popleft()
                if output:
                    level.append(output.val)
                    q.append(output.left)
                    q.append(output.right)
            if level:
                l.append(level)
                
        return l

        
