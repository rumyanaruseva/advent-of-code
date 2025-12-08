# Pre-Process Input
def processInput(file):

    input = open(file, "r").read()
    IDs = [tuple(map(int, range.split("-")) )for range in input.strip().split(",")]

    return IDs

# Repeated exactly twice
def invalidID_part1(num):
    id_str = str(num)

    # If the length is uneven, can't be valid
    if len(id_str) % 2:
        return False

    mid = len(id_str) // 2
    return (id_str[:mid] == id_str[mid:])

# Repeated at least twice)
def invalidID_part2(num):
    id_str = str(num)
    size = len(id_str)
    
    # Try all possible segment lengths from 1 to n//2
    # (We need at least 2 repetitions, so segment can be at most n//2)
    for segment_length in range(1, size // 2 + 1):
        # Check if we can divide the string evenly into segments
        if size % segment_length != 0:
            continue  # Skip if it doesn't divide evenly
        
        # Get the first segment (the pattern to match)
        first_segment = id_str[0:segment_length]
        num_segments = size // segment_length
        
        # Check if all segments match the first one
        all_match = True
        for i in range(1, num_segments):  # Start from 1 (skip first segment)
            start_idx = i * segment_length
            end_idx = (i + 1) * segment_length
            segment = id_str[start_idx:end_idx]
            
            if segment != first_segment:
                all_match = False
                break
        
        # If all segments match, it's an invalid ID
        if all_match:
            return True
    
    # No repeating pattern found
    return False

# Part 1
def part1():
    id_list = processInput("day2-input.txt")
    invalidIDs = []

    for start, end in id_list:
        for i in range(start, end + 1):
            if invalidID_part1(i):
                invalidIDs.append(i)

    return sum(invalidIDs)

# Part 2
def part2():
    id_list = processInput("day2-input.txt")
    invalidIDs = []

    for start, end in id_list:
        for i in range(start, end + 1):
            if invalidID_part2(i):
                invalidIDs.append(i)

    return sum(invalidIDs)


def main():
    res1 = part1()
    print("Part 1:", res1)
    
    res2 = part2()
    print("Part 2:", res2)

if __name__ == "__main__":
    main()
