from collections import deque
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            res = S
            # return min(S[i:] + S[:i] for i in range(len(S))) # O(n^2) time and space
            # O(n^) time , O(n) space
            # note deque can also be used for rotation slightly more efficient
            for i in range(len(S)):
                res = min(res, S[i:] + S[:i])
            return res
        else:
            return ''.join(sorted(S))