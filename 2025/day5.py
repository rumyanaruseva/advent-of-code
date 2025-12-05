# --- Day 5: Cafeteria ---
# As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.
# You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" 
# Resolute in your quest, you investigate.
# "If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. 
# You ask what's going on. The Elves in the kitchen explain the situation: because of their complicated new inventory management system, 
# they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, 
# they give you a copy of their database (your puzzle input).
# The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges,
# a blank line, and a list of available ingredient IDs. For example:

# 3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. 
# The ranges can also overlap; an ingredient ID is fresh if it is in any range.
# The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

# Ingredient ID 1 is spoiled because it does not fall into any range.
# Ingredient ID 5 is fresh because it falls into range 3-5.
# Ingredient ID 8 is spoiled.
# Ingredient ID 11 is fresh because it falls into range 10-14.
# Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
# Ingredient ID 32 is spoiled.
# So, in this example, 3 of the available ingredient IDs are fresh.

# --- Part Two ---
# The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.
# So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the 
# fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.
# Now, the second section of the database (the available ingredient IDs) is irrelevant. 
# Here are the fresh ingredient ID ranges from the above example:

# 3-5
# 10-14
# 16-20
# 12-18
# The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. 
# So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

# Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?


# Pre-Process Input
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
