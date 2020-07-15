# credit: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33815/My-accepted-JAVA-solution
# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = [[]]
        # self._dfs(root, res, 0)
        self._bfs(root, res)
        self._zigzag(res)
        return res
    
    def _dfs(self, root: TreeNode, res: List[List[int]], lvl: int) -> None:
        if not root:
            return
        if len(res) == lvl:
            res.append([])
        
        res[lvl].append(root.val)
        self._dfs(root.left, res, lvl + 1)
        self._dfs(root.right, res, lvl + 1)
    
    def _bfs(self, root: TreeNode, res: List[List[int]]) -> None:
        queue = collections.deque()
        queue.append(root)
        lvl = 0
        while queue:
            size = len(queue)
            if len(res) <= lvl: res.append([]) 
            while size:
                ele = queue.popleft()
                res[lvl].append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                size -= 1
            lvl += 1
            
    def _zigzag(self, res: List[List[int]]) -> None:
        for i, l in enumerate(res):
            if i % 2 == 1:
                res[i].reverse()