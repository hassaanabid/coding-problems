class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) is (divisor > 0)
        a, b, res = abs(dividend), abs(divisor), 0
        INT_MAX, INT_MIN = (1<<31) -1, -1<<31
        while a >= b:
            x = 0
            while a >= b << (x+1): x += 1
            res += 1 << x
            a -= b << x
        if not positive: res = -res
        return min(max(INT_MIN, res), INT_MAX)