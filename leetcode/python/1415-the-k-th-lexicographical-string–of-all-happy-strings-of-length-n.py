# credit: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/discuss/585590/C%2B%2BJava-DFS-and-Math
# TC: O(n * k) k strings computed of size n each
# SC: O(n) since n is the depth of the tree


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(height, prev_ch):
            nonlocal k, n
            # print('before k=', k, ' n=', n, ' h=', height, 'ch=', prev_ch)
            # base case reached 1 level out of bound (since height is 0-based while n is 1-based)
            # return empty str
            if height == n:
                k -= 1
                return ''
            else:
                for c in 'abc':
                    # prev_ch check ensures no adj duplicates
                    if prev_ch != c:
                        # recurse further until height == n
                        rv = dfs(height + 1, c)
                        # print('after k=', k, ' n=', n, ' h=', height, 'ch=', prev_ch, 'rv=')
                        # first time k == 0 means reached kth node at nth lvl
                        # note k is global so result will be pushed upwards
                        if k == 0:
                            return (c + rv)
            # reached when unable to find kth element in any of the children hence return empty string
            # happens in two cases: (1) k is not in children (2) k is invalid (i.e. never reaches 0)
            # print('node exhausted')
            return ''
        res = dfs(0, '')
        return res
