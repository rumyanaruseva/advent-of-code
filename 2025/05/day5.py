def processInput(file):
    input = open(file, "r").read()    
    fresh_raw, available_raw = input.split("\n\n")
    fresh = [tuple(map(int, range.split("-")) )for range in fresh_raw.strip().split("\n")]
    available = list(map(int, available_raw.strip().split("\n")))

    return fresh, available

# Part 1
def part1():
    fresh, available = processInput("day5-input.txt")

    # Iterate through all ingredients
    # O(n * m) - number of available * number of fresh ranges
    count = 0
    for ingredient in available:
        if (any(start <= ingredient <= end for start, end in fresh)):
            count += 1

    return count

# Part 2 - Original Solution (hangs)
def part2_og():
    fresh_ranges, _ = processInput("day5-input.txt")
    fresh_all = set()

    # O(m * k) - number of fresh ranges * range width
    for start, end in fresh_ranges:
        fresh_all.update(range(start, end + 1))

    return len(fresh_all)

# Part 2 - Alternative 4: Interval Merging (Most Efficient for Large Ranges)
# Resorted to cursor's suggestion
def part2_alt():
    fresh_ranges, _ = processInput("day5-input.txt")
    
    # Sort ranges by start value
    sorted_ranges = sorted(fresh_ranges)
    
    if not sorted_ranges:
        return 0
    
    # Merge overlapping intervals
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # If current range overlaps or is adjacent to last range
        if start <= last_end + 1:
            # Merge: extend the last range if needed
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))
    
    # Calculate total from merged ranges
    total = sum(end - start + 1 for start, end in merged)
    return total

def main():
    fresh_ingredients = part1()
    print("Part 1:", fresh_ingredients)

    fresh_ingredients = part2_alt()
    print("Part 2:", fresh_ingredients)

if __name__ == "__main__":
    main()
