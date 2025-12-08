# Day 7: 
# https://adventofcode.com/2025/day/7

def processInput(file):
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    
    # Convert each line string into a list of characters
    data = [list(line) for line in lines]
    
    return data

def part1():
    data = processInput("day7-input.txt")

    # Start the beam, find the position of S in the first row
    start_row = data[0]
    start_pos = 0
    for pos in range(len(start_row)):
        if start_row[pos] == 'S':
            start_pos = pos
            break

    # Mark the beam in the second row
    data[1][start_pos] = '|'

    # O(n * m)
    # Start from the second row
    num_rows = len(data)
    num_cols = len(data[0])
    split_count = 0
    for row in range(1, num_rows - 1):
        for col in range(num_cols):
            if data[row][col] == '|':
                # follow the beam, see if it's followed by a split
                if data[row + 1][col] == '^':
                    # split, mark the split ray in next row
                    if col > 0:
                        data[row + 1][col - 1] = '|'
                    if col < num_cols - 1:
                        data[row + 1][col + 1] = '|'
                    split_count += 1
                else:
                    # no split, continiue the ray
                    data[row + 1][col] = '|'

    return split_count

def part2():
    """ 
    Each path carries with it the count of different routes you can take to get there.
    Start from S with 1. Each time paths merge, sum their counts.
    Each time they split, put the count on both sides.
    """
    data = processInput("day7-input.txt")
    
    num_rows = len(data)
    num_cols = len(data[0])
    
    # Find starting position
    start_pos = 0
    for pos in range(len(data[0])):
        if data[0][pos] == 'S':
            start_pos = pos
            break
    
    # Initialize counts array: same dimensions as data, all zeros
    counts = [[0] * num_cols for _ in range(num_rows)]
    
    # Initialize: start position has count 1
    counts[0][start_pos] = 1
    
    # Process each row from top to bottom
    for row in range(num_rows - 1):
        next_row = row + 1
        # Temporary array to accumulate counts for next row
        next_counts = [0] * num_cols
        
        # For each position in current row that has a count
        for col in range(num_cols):
            if counts[row][col] > 0:
                count = counts[row][col]
                
                # Check what's in the next row at this column
                if next_row < num_rows:
                    if data[next_row][col] == '^':
                        # Splitter: count goes to both left and right positions
                        if col > 0:
                            next_counts[col - 1] += count
                        if col < num_cols - 1:
                            next_counts[col + 1] += count
                    else:
                        # Empty space ('.'): count continues straight down
                        next_counts[col] += count
        
        # Update counts for next row (merging happens automatically via +=)
        for col in range(num_cols):
            counts[next_row][col] = next_counts[col]
    
    # Sum all counts in the last row (all possible timelines)
    total_timelines = sum(counts[num_rows - 1])
        
    return total_timelines

def main():
    result = part1()
    print("Part 1:", result)
    
    result2 = part2()
    print("Part 2:", result2)

if __name__ == "__main__":
    main()
