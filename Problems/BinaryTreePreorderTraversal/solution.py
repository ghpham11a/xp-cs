# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        
        output = []

        if root is None:
            return output

        stack = [root]
        
        while stack:
            current = stack.pop()

            if current is not None:

                output.append(current.val)

                if current.right:
                    stack.append(current.right)
                    
                if current.left:
                    stack.append(current.left)

        return output