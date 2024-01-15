You are given a positive integer `n`, you can do the following operation **any** number of times:

* Add or subtract a **power** of `2` from `n`.

Return *the **minimum** number of operations to make *`n`* equal to *`0`.

A number `x` is power of `2` if `x == 2<sup>i</sup>` where `i >= 0`*.*

```python
class Solution:
  def minOperations(self, n: int) -> int:
    # The strategy is that when the end of n is
    #   1. consecutive 1s, add 1 (2^0).
    #   2. single 1, substract 1 (2^0).
    #   3. 0, substract 2^k to omit the last 1. Equivalently, n >> 1.
    #
    # e.g.
    #
    #         n = 0b101
    # n -= 2^0 -> 0b100
    # n -= 2^2 -> 0b0
    #         n = 0b1011
    # n += 2^0 -> 0b1100
    # n -= 2^2 -> 0b1000
    # n -= 2^3 -> 0b0
    ans = 0

    while n > 0:
      if (n & 3) == 3:
        n += 1
        ans += 1
      elif (n & 1) == 1:
        n -= 1
        ans += 1
      else:
        n >>= 1

    return ans
```
