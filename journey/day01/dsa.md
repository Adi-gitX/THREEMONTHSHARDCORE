# 🧮 DSA Practice - Day 01

---

## Problem 1: Two Sum (LeetCode #1)

### Approach: Brute Force O(n²)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

### Complexity
| Metric | Value |
|--------|-------|
| Time   | O(n²) |
| Space  | O(1)  |

### Optimal: HashMap O(n)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

### Complexity
| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(n)  |

**⏱️ Solved in: <5 min**

---

## Problem 2: Valid Anagram (LeetCode #242)

### Approach: Sorting

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False
```

### Complexity
| Metric | Value |
|--------|-------|
| Time   | O(n log n) |
| Space  | O(n)  |

### Optimal: Frequency Map O(n)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for c in t:
            if c not in freq or freq[c] == 0:
                return False
            freq[c] -= 1
        return True
```

### Complexity
| Metric | Value |
|--------|-------|
| Time   | O(n)  |
| Space  | O(1)  |

> Space is O(1) because at most 26 lowercase letters (constant)

**⏱️ Solved in: <5 min**

---

## 🔑 Key Takeaways

- **Two Sum**: HashMap trades space for time (O(n²) → O(n))
- **Anagram**: Sorting works but frequency counting is optimal
- Both are classic "frequency/lookup" pattern problems

---

*Day 1 DSA ✅*
