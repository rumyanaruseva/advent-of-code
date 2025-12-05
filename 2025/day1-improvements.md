# Day 1 Solution Improvements

## Current Solution Analysis

### Current Preprocessing
```python
dials = []
for dial in lines:
    num = int(dial[1:])
    if dial[0] == "L":
        num = num * -1
    dials.append(num)
```

**Issues:**
- Variable name `dial` is confusing (should be `line`)
- Uses `num * -1` instead of `-num`
- Multiple lines for simple logic

### Current Part 1
```python
dial += r
if dial < 0:
    dial += 100
if dial > 99:
    dial -= 100
```

**Issues:**
- Manual wrapping with if statements
- More verbose than necessary
- Two separate conditions instead of one operation

---

## Better Solutions

### ✅ **Recommended: Using Modulo Operator**

```python
dial = (dial + r) % 100
```

**Why it's better:**
- ✅ **Single line** instead of multiple if statements
- ✅ **Handles both cases** (negative and > 99) automatically
- ✅ **More Pythonic** and idiomatic
- ✅ **More efficient** (one operation vs multiple conditionals)
- ✅ **Easier to understand** - modulo is the standard way to handle circular arithmetic

**How modulo works:**
- `(50 + 48) % 100 = 98 % 100 = 98` ✓
- `(50 - 68) % 100 = -18 % 100 = 82` ✓ (Python handles negative modulo correctly)
- `(52 + 48) % 100 = 100 % 100 = 0` ✓
- `(0 - 1) % 100 = -1 % 100 = 99` ✓

### Alternative 1: Clean Modulo (BEST)
```python
def part1_alt1():
    rotations = processInput("day1-input.txt")
    dial = 50
    count = 0

    for r in rotations:
        dial = (dial + r) % 100
        if dial == 0:
            count += 1

    return count
```

### Alternative 2: Using sum() trick
```python
count += (dial == 0)  # True = 1, False = 0
```
- More concise
- Uses Python's boolean-to-int conversion

### Alternative 3: Functional style
```python
positions = []
for r in rotations:
    dial = (dial + r) % 100
    positions.append(dial)
return sum(1 for pos in positions if pos == 0)
```
- Separates calculation from counting
- More functional programming style

### Alternative 4: One-liner (walrus operator)
```python
return sum(1 for r in rotations if (dial := (dial + r) % 100) == 0)
```
- Most concise
- Uses Python 3.8+ walrus operator `:=`
- Less readable for beginners

---

## Preprocessing Improvements

### Current
```python
dials = []
for dial in lines:
    num = int(dial[1:])
    if dial[0] == "L":
        num = num * -1
    dials.append(num)
```

### Better: More Pythonic
```python
rotations = []
for line in lines:
    direction, distance = line[0], int(line[1:])
    rotations.append(-distance if direction == "L" else distance)
```

**Improvements:**
- ✅ Better variable names (`line` instead of `dial`)
- ✅ Uses ternary operator
- ✅ More readable

### Even Better: List Comprehension
```python
return [-int(line[1:]) if line[0] == "L" else int(line[1:]) for line in lines]
```

**Pros:**
- Most concise
- Pythonic

**Cons:**
- Slightly less readable for beginners

---

## Comparison

| Approach | Lines | Readability | Performance | Recommendation |
|----------|-------|-------------|-------------|----------------|
| **Current** | 6 | Good | Good | ⚠️ Manual wrapping |
| **Modulo (Alt 1)** | 1 | Excellent | Excellent | ⭐ **BEST** |
| **Sum trick (Alt 2)** | 1 | Good | Excellent | ✅ Good |
| **Functional (Alt 3)** | 5 | Good | Good | ✅ Alternative |
| **One-liner (Alt 4)** | 1 | Fair | Excellent | ⚠️ Less readable |

---

## Final Recommendation

**Use this for Part 1:**
```python
def part1():
    rotations = processInput("day1-input.txt")
    dial = 50
    count = 0

    for r in rotations:
        dial = (dial + r) % 100
        if dial == 0:
            count += 1

    return count
```

**And this for preprocessing:**
```python
def processInput(file):
    with open(file, "r") as f:
        lines = f.read().strip().split("\n")
    
    rotations = []
    for line in lines:
        direction, distance = line[0], int(line[1:])
        rotations.append(-distance if direction == "L" else distance)
    
    return rotations
```

---

## Key Takeaway

**Modulo operator (`%`) is the standard way to handle circular/wrapping arithmetic in programming.**

Instead of:
```python
if value < 0:
    value += max_value
if value >= max_value:
    value -= max_value
```

Use:
```python
value = value % max_value
```

This is cleaner, more efficient, and more Pythonic!

