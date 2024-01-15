from collections import Counter
from collections import defaultdict
from collections import deque
import heapq

# use defaultdict to give default values to dictionaries
defaultdict(int)    # new keys are initialized to zero
defaultdict(lambda: 5)     # new keys are initialized to 5

# Use Counter to count the number of unique occurances in a array
Counter(['A', 'B', 'B', 'C'])

# use heap to compute minimum or maximum of collection, or to access items in sorted order
minHeap = [1, 2, 7, 5, 3, 8, 0]
heapq.heapify(minHeap)

# lists are not valid keys, convert to tuple instead
invalidKeyList = defaultdict(int)
validKeyList = defaultdict(int)
invalidKeyList[[1, 2]] = 5            # throws error
validKeyList[tuple([1, 2])] = 5       # works

# use deque
q = deque()

# as a standard queue ( one side )
q.append([1, 2])
q.popleft()

# or both ends
q.appendleft([1, 2])
q.pop()

# DFS
visited = set()


def dfs(r, c, visited):  # potentially more variables
    if (r, c) in visited or False:  # replace False with criteria for dropping
        return
    visited.add((r, c))
    # call dfs for leaf nodes


# 2d array
rows, cols = 5, 3
two_d_array = [[False for _ in range(cols)] for _ in range(rows)]

for row in two_d_array:
    print(row)

# loop through all instances in 2d array
for row in two_d_array:
    for col in row:
        pass

# loop over 1 bits in n
n = b'010010100'
n = n & (n-1)
