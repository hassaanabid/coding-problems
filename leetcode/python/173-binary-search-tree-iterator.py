# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import partial 
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.fun = self.inorder(root)
        self.data = self._get_next()
        
    def _get_next(self):
        try:
            return next(self.fun)
        except StopIteration:
            return None
            
    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmp = self.data
        self.data = self._get_next()
        return tmp.val
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.data else False

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)
            
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()