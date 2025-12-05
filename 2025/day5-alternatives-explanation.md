# Part 2 Alternative Solutions Explained

## Overview
All solutions produce the same result but differ in style, readability, and efficiency.

## Solution Comparison

### Original Solution (`part2`)
```python
fresh_all = set()
for start, end in fresh_ranges:
    ingredient = start
    while ingredient <= end:
        fresh_all.add(ingredient)
        ingredient += 1
```
**Pros:**
- Very explicit and easy to understand
- Good for beginners

**Cons:**
- More verbose
- Manual iteration

**Time Complexity:** O(m × k) where m = ranges, k = average range width
**Space Complexity:** O(n) where n = unique IDs

---

### Alternative 1: Using `range()` (`part2_alt1`)
```python
for start, end in fresh_ranges:
    fresh_all.update(range(start, end + 1))
```
**Pros:**
- More Pythonic
- Uses built-in `range()` function
- Cleaner than manual while loop

**Cons:**
- Still requires explicit loop

**Time Complexity:** O(m × k)
**Space Complexity:** O(n)

---

### Alternative 2: Set Union (`part2_alt2`)
```python
fresh_all = set().union(*(range(start, end + 1) for start, end in fresh_ranges))
```
**Pros:**
- Functional style
- More concise
- Uses generator expression

**Cons:**
- Less readable for beginners
- Unpacking operator `*` might be confusing

**Time Complexity:** O(m × k)
**Space Complexity:** O(n)

---

### Alternative 3: One-liner Set Comprehension (`part2_alt3`)
```python
return len({id for start, end in fresh_ranges for id in range(start, end + 1)})
```
**Pros:**
- Most concise
- Single expression
- Pythonic

**Cons:**
- Can be harder to read
- Nested comprehension might be confusing

**Time Complexity:** O(m × k)
**Space Complexity:** O(n)

---

### Alternative 4: Interval Merging (`part2_alt4`)
```python
# Sort and merge overlapping intervals
sorted_ranges = sorted(fresh_ranges)
merged = [sorted_ranges[0]]
for start, end in sorted_ranges[1:]:
    last_start, last_end = merged[-1]
    if start <= last_end + 1:
        merged[-1] = (last_start, max(last_end, end))
    else:
        merged.append((start, end))
total = sum(end - start + 1 for start, end in merged)
```
**Pros:**
- Most efficient for large ranges
- Doesn't store individual IDs in memory
- Better for very wide ranges

**Cons:**
- More complex logic
- Requires sorting first
- Overkill for typical Advent of Code inputs

**Time Complexity:** O(m log m + m) = O(m log m) for sorting + merging
**Space Complexity:** O(m) for merged ranges (much better than O(n) if ranges are large)

---

### Alternative 5: Using `itertools.chain` (`part2_alt5`)
```python
from itertools import chain
all_ids = chain(*(range(start, end + 1) for start, end in fresh_ranges))
return len(set(all_ids))
```
**Pros:**
- Functional programming style
- Efficient memory usage (lazy evaluation)
- Clean and readable

**Cons:**
- Requires import
- Similar to Alt 2

**Time Complexity:** O(m × k)
**Space Complexity:** O(n)

---

## Performance Notes

For typical Advent of Code inputs:
- **Best choice:** Alternative 1 or 3 (good balance of readability and conciseness)
- **For very large ranges:** Alternative 4 (interval merging)
- **For learning:** Original or Alternative 1

## Recommendation

**For this problem:** Use **Alternative 1** (`part2_alt1`) - it's clean, Pythonic, and easy to understand.

**For production with large ranges:** Use **Alternative 4** (`part2_alt4`) - it's the most memory-efficient.

