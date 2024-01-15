Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

```python3
class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    m = len(s1)
    n = len(s2)
    if m + n != len(s3):
      return False

    # dp[i][j] := true if s3[0..i + j) is formed by the interleaving of
    # s1[0..i) and s2[0..j)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
      dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, n + 1):
      dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
            (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[m][n]
```

```python3
class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    m = len(s1)
    n = len(s2)
    if m + n != len(s3):
      return False

    dp = [False] * (n + 1)

    for i in range(m + 1):
      for j in range(n + 1):
        if i == 0 and j == 0:
          dp[j] = True
        elif i == 0:
          dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        elif j == 0:
          dp[j] = dp[j] and s1[i - 1] == s3[i - 1]
        else:
          dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or \
              (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[n]
```