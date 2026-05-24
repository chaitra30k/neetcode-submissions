class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = n
        n = abs(n)

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x

            x *= x
            n //= 2

        return ans if power >= 0 else 1 / ans