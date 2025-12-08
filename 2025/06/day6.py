import sys

def processInput(file):
    with open(file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    column_data = [line.split() for line in lines]

    return column_data

def part1():
    columns_data = processInput("day6-input.txt")
    num_columns = len(columns_data[0])

    result_all = 0
    # For each column index:
    for col_idx in range(num_columns):
        numbers = []
        for row in columns_data[:-1]:  # All except last row
            numbers.append(int(row[col_idx]))
        
        operation = columns_data[-1][col_idx]  # Last row

        # Calculate: multiply or add
        if operation == '*':
            result = 1
            for number in numbers:
                result *= number 
        else:
            # result = sum of all numbers
            result = 0
            result = sum(numbers)

        result_all += result

    return result_all

def part2():
    
    return

def main():
    result = part1()
    print("Part 1:", result)
    
    result = part2()
    print("Part 2:", result)

if __name__ == "__main__":
    main()
