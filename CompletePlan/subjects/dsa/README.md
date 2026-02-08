# 📊 Data Structures & Algorithms

> **Time Allocation:** 30 min DSA + 30 min Interview Prep = 1 hour/day  
> **Target:** 180+ LeetCode Problems  
> **Focus:** FAANG Interview Preparation

---

## 📚 Course Overview

Master data structures and algorithms through deliberate practice. Progress from easy warmups to hard interview questions, building pattern recognition and problem-solving speed.

---

## 🗓️ Learning Path by Pattern

### **Arrays & Hashing (Weeks 1-2)**

#### Core Problems
1. **Two Sum** - HashMap basics
2. **Valid Anagram** - Character frequency
3. **Contains Duplicate** - Set operations
4. **Group Anagrams** - Sorted key trick
5. **Top K Frequent Elements** - Bucket sort O(n)
6. **Product of Array Except Self** - Prefix/suffix arrays
7. **Valid Sudoku** - Row/col/box set checking

**Key Patterns:**
- HashMap for O(1) lookup
- Frequency counting
- Index-based tricks
- Prefix/suffix arrays

**Time Complexity Targets:**
- Two Sum: O(n)
- Group Anagrams: O(n * k log k)
- Product Array: O(n) without division

**📝 Deliverables:**
- 15+ array problems solved
- Pattern recognition cheat sheet

---

### **Two Pointers (Weeks 2-3)**

#### Core Problems
1. **Valid Palindrome** - Basic two pointer
2. **Two Sum II** - Sorted array variant
3. **3Sum** - Sort + skip duplicates O(n²)
4. **Container With Most Water** - Greedy proof
5. **Trapping Rain Water** - Two pointer logic

**Key Patterns:**
- Opposite direction pointers
- Same direction (fast/slow)
- Sliding window preparation

**📝 Deliverables:**
- 10+ two pointer problems
- Proof of greedy approaches

---

### **Sliding Window (Weeks 3-4)**

#### Core Problems
1. **Best Time to Buy/Sell Stock** - Single pass
2. **Longest Substring Without Repeating** - Variable window
3. **Longest Repeating Character Replacement** - Window + frequency
4. **Minimum Window Substring** - Hard template
5. **Permutation in String** - Fixed window

**Template:**
```python
def sliding_window(s, target):
    window = {}
    left = 0
    result = 0
    
    for right in range(len(s)):
        # Expand window
        window[s[right]] = window.get(s[right], 0) + 1
        
        # Contract window if needed
        while not valid(window):
            window[s[left]] -= 1
            left += 1
        
        # Update result
        result = max(result, right - left + 1)
    
    return result
```

**📝 Deliverables:**
- Sliding window template mastered
- 10+ problems solved

---

### **Stack (Weeks 4-5)**

#### Core Problems
1. **Valid Parentheses** - Stack basics
2. **Min Stack** - O(1) getMin trick
3. **Evaluate Reverse Polish Notation** - Stack eval
4. **Generate Parentheses** - Backtracking
5. **Daily Temperatures** - Monotonic stack
6. **Car Fleet** - Sort + merge
7. **Largest Rectangle in Histogram** - Hard stack problem

**Monotonic Stack Pattern:**
```python
def next_greater_element(nums):
    stack = []  # Monotonic decreasing
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

**📝 Deliverables:**
- Stack patterns mastered
- Monotonic stack problems (5+)

---

### **Linked Lists (Weeks 5-6)**

#### Core Problems
1. **Reverse Linked List** - Iterative + recursive
2. **Merge Two Sorted Lists** - Dummy node
3. **Reorder List** - Find mid + reverse + merge
4. **Remove Nth From End** - Two pointer gap
5. **Copy List with Random Pointer** - HashMap clone
6. **Add Two Numbers** - Carry propagation
7. **Detect Cycle** - Floyd's algorithm
8. **LRU Cache** - DLL + HashMap O(1)

**Key Patterns:**
- Dummy node for edge cases
- Fast/slow pointers
- Reversal in-place
- HashMap for complex pointers

**📝 Deliverables:**
- All linked list patterns
- LRU Cache implementation

---

### **Trees (Weeks 6-8)**

#### Binary Tree Basics
1. **Invert Binary Tree**
2. **Maximum Depth**
3. **Same Tree**
4. **Subtree of Another Tree**
5. **Binary Tree Level Order** - BFS with levels
6. **Binary Tree Right Side View** - Rightmost per level
7. **Count Good Nodes** - Path tracking

#### Binary Search Trees
1. **Validate BST** - Inorder or range checking
2. **Kth Smallest in BST** - Counter or inorder
3. **Construct from Preorder/Inorder**

**DFS Template:**
```python
def dfs(root):
    if not root:
        return base_case
    
    left = dfs(root.left)
    right = dfs(root.right)
    
    # Combine results
    return process(root.val, left, right)
```

**BFS Template:**
```python
def bfs(root):
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # Process node
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

**📝 Deliverables:**
- 20+ tree problems
- DFS/BFS templates mastered

---

### **Backtracking (Week 8)**

#### Core Problems
1. **Subsets** - Include/exclude
2. **Combination Sum**
3. **Permutations**
4. **Word Search** - 2D grid DFS
5. **Palindrome Partitioning**

**Template:**
```python
def backtrack(path, choices):
    if is_solution(path):
        results.append(path[:])
        return
    
    for choice in choices:
        # Make choice
        path.append(choice)
        
        # Recurse
        backtrack(path, next_choices)
        
        # Undo choice
        path.pop()
```

**📝 Deliverables:**
- Backtracking template
- 8+ problems solved

---

### **Graphs (Weeks 9-11)**

#### DFS/BFS Problems
1. **Number of Islands** - DFS flood fill
2. **Clone Graph** - HashMap clone
3. **Pacific Atlantic Water Flow** - Reverse BFS
4. **Course Schedule** - Cycle detection
5. **Course Schedule II** - Topological sort
6. **Rotting Oranges** - Multi-source BFS
7. **Walls and Gates** - Multi-source BFS

#### Advanced Graphs
1. **Graph Valid Tree** - Union-Find
2. **Number of Connected Components** - Union-Find
3. **Alien Dictionary** - Topological sort from characters

**Union-Find Template:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            px, py = py, px
        self.parent[px] = py
        self.rank[py] += self.rank[px]
        return True
```

**📝 Deliverables:**
- Graph patterns mastered
- Union-Find implementation

---

### **Dynamic Programming (Weeks 10-13)**

#### 1D DP
1. **Climbing Stairs** - Fibonacci
2. **House Robber** - Max non-adjacent
3. **Decode Ways** - String DP
4. **Coin Change** - Unbounded knapsack
5. **Longest Increasing Subsequence** - O(n²) → O(n log n)

#### 2D DP
1. **Unique Paths** - 2D grid
2. **Longest Common Subsequence** - 2D table + traceback
3. **0/1 Knapsack** - Classic problem
4. **Edit Distance** - 3 operations
5. **Target Sum** - Convert to subset sum
6. **Partition Equal Subset Sum** - Bitset optimization

**DP Template:**
```python
# Bottom-up approach
def dp_solution(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = base_case
    
    for i in range(1, n + 1):
        for prev in possible_transitions:
            dp[i] = optimize(dp[i], dp[prev] + cost)
    
    return dp[n]
```

**📝 Deliverables:**
- DP pattern recognition
- 25+ DP problems

---

### **Advanced Topics (Weeks 11-13)**

#### Shortest Path
1. **Dijkstra's Algorithm** - Min-heap + relaxation
2. **Network Delay Time** - Single source
3. **Cheapest Flights K Stops** - Modified Bellman-Ford
4. **Swim in Rising Water** - Dijkstra variant

#### Minimum Spanning Tree
1. **Prim's Algorithm**
2. **Kruskal's Algorithm** - Union-Find

#### Greedy
1. **Jump Game I & II**
2. **Gas Station** - Net gain O(n)
3. **Merge Intervals** - Sort + greedy
4. **Non-Overlapping Intervals**
5. **Meeting Rooms I & II** - Sort + heap

#### Bit Manipulation
1. **Single Number** - XOR
2. **Counting Bits** - Brian Kernighan
3. **Reverse Bits**
4. **Number of 1 Bits**
5. **Missing Number** - XOR or Gauss sum

#### Tries
1. **Implement Trie** - insert/search/startsWith
2. **Word Search II** - Trie + backtracking + pruning

---

## 🎯 Weekly Schedule

### Daily Pattern
- **Monday-Thursday:** 2-3 problems per day
  - 1 easy (warmup)
  - 1 medium (main practice)
  - 1 medium/hard (stretch)

- **Friday:** Review + pattern consolidation
  - Re-solve 3-5 problems without hints
  - Update pattern cheat sheet

- **Saturday:** Review week's hardest
  - 5 most difficult problems

- **Sunday:** HARD practice day
  - 2-3 hard problems
  - Focus on weak patterns

---

## 📊 Progress Tracking

### Metrics to Track
```markdown
## Week [N] Progress

### Problems Solved: [X]/180
- Easy: [X]
- Medium: [X]
- Hard: [X]

### Patterns Mastered
- [x] Arrays & Hashing
- [ ] Two Pointers
- [ ] Sliding Window
...

### Time Stats
- Average time per problem: [X] min
- Stuck problems: [List]
- Need review: [List]

### Interview Readiness
- Can solve medium in 25 min: Yes/No
- Can explain approach clearly: Yes/No
- Can optimize on spot: Yes/No
```

---

## 🎯 Success Metrics

- [ ] 180+ problems solved
- [ ] All patterns mastered
- [ ] Can solve medium in 25 minutes
- [ ] Can solve hard in 45 minutes
- [ ] Pass mock interviews (3+)
- [ ] Company-specific problems (FAANG)
  - [ ] Microsoft (20 tagged)
  - [ ] Google (20 tagged)
  - [ ] Amazon (20 tagged)

---

## 📚 Resources

### Platforms
- **LeetCode** - Primary platform
- **NeetCode** - Curated problem list
- **AlgoExpert** - Video explanations

### Study Guides
- [NeetCode 150](https://neetcode.io/)
- [Blind 75](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
- [Grind 75](https://www.techinterviewhandbook.org/grind75)

### Books
- **Cracking the Coding Interview** - McDowell
- **Elements of Programming Interviews** - Aziz

---

## 🔗 Related Resources

- [Back to Complete Plan](../../README.md)
- [Interview Prep Guide](../../templates/interview-prep.md)

---

**Remember:** Consistency > Intensity. Better to solve 2 problems daily than 20 on Sunday!

*Last Updated: Day 0*
