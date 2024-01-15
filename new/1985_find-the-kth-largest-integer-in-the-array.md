You are given an array of strings `nums` and an integer `k`. Each string in `nums` represents an integer without leading zeros.

Return *the string that represents the *`k<sup>th</sup>`*** largest integer** in *`nums`.

 **Note** : Duplicate numbers should be counted distinctly. For example, if `nums` is `["1","2","2"]`, `"2"` is the first largest integer, `"2"` is the second-largest integer, and `"1"` is the third-largest integer.

```python3
class Solution:
  # Similar to 215. Kth Largest Element in an Array
  def kthLargestNumber(self, nums: List[str], k: int) -> str:
    minHeap = []

    for num in nums:
      heapq.heappush(minHeap, int(num))
      if len(minHeap) > k:
        heapq.heappop(minHeap)

    return str(minHeap[0])
```
