# --- Day 6: Trash Compactor ---
# After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene 
# when you over-enthusiastically jumped into the garbage chute!

# A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

# As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure 
# they can get the door open, but it will take some time. While you wait, they're curious if you 
# can help the youngest cephalopod with her math homework.

# Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) 
# consists of a list of problems; each problem has a group of numbers that need to be either added (+) 
# or multiplied (*) together.

# However, the problems are arranged a little strangely; they seem to be presented next to each other 
# in a very long horizontal list. For example:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the 
# operation that needs to be performed. Problems are separated by a full column of only spaces. 
# The left/right alignment of numbers within each problem can be ignored.

# So, this worksheet contains four problems:

# 123 * 45 * 6 = 33210
# 328 + 64 + 98 = 490
# 51 * 387 * 215 = 4243455
# 64 + 23 + 314 = 401
# To check their work, cephalopod students are given the grand total of adding together all of the 
# answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

# Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

# Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?

# --- Part Two ---
# The big cephalopods come back to check on how things are going. When they see that your grand total 
# doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

# Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant 
# digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting 
# only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

# Here's the example worksheet again:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# Reading the problems right-to-left one column at a time, the problems are now quite different:

# The rightmost problem is 4 + 431 + 623 = 1058
# The second problem from the right is 175 * 581 * 32 = 3253600
# The third problem from the right is 8 + 248 + 369 = 625
# Finally, the leftmost problem is 356 * 24 * 1 = 8544
# Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

# Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?

import sys

# Increase the limit for integer string conversion (needed for large numbers in part 2)
sys.set_int_max_str_digits(10000)

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
    # Read lines as strings (preserve character positions)
    with open("day6-input.txt", "r") as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    if not lines:
        return 0
    
    # Find maximum line length
    max_len = max(len(line) for line in lines)
    
    result_all = 0
    
    # Process character columns right-to-left
    current_problem_numbers = []
    current_problem_cols = []
    
    for col_idx in range(max_len - 1, -1, -1):
        # Read digits from this character column (top to bottom)
        digits = []
        has_digits = False
        
        for row_idx in range(len(lines) - 1):  # All except operation row
            if col_idx < len(lines[row_idx]):
                char = lines[row_idx][col_idx]
                if char.isdigit():
                    digits.append(char)
                    has_digits = True
        
        # Check if column is empty (all rows are spaces)
        is_empty = True
        if has_digits:
            is_empty = False
        else:
            # Check all rows including operation row
            all_spaces = True
            for row_idx in range(len(lines)):
                if col_idx < len(lines[row_idx]):
                    char = lines[row_idx][col_idx]
                    if char.strip() != '':  # Not a space
                        all_spaces = False
                        break
            is_empty = all_spaces
        
        if has_digits:
            # This column contains digits of a number (stacked top-to-bottom)
            # Form number from digits (most significant at top)
            number = int(''.join(digits)) if digits else 0
            current_problem_numbers.append(number)
            current_problem_cols.append(col_idx)
        elif is_empty and current_problem_numbers:
            # Empty column - marks end of current problem
            # Get operation from the rightmost column of this problem
            rightmost_col = current_problem_cols[0]  # First in list (rightmost)
            if rightmost_col < len(lines[-1]):
                operation = lines[-1][rightmost_col].strip()
                
                # Only process if we have a valid operation
                if operation in ['*', '+']:
                    # Calculate result for this problem
                    if operation == '*':
                        result = 1
                        for num in current_problem_numbers:
                            result *= num
                    else:  # operation == '+'
                        result = sum(current_problem_numbers)
                    
                    result_all += result
            
            # Reset for next problem
            current_problem_numbers = []
            current_problem_cols = []
    
    # Handle last problem (if file doesn't end with empty column)
    if current_problem_numbers:
        rightmost_col = current_problem_cols[0]
        if rightmost_col < len(lines[-1]):
            operation = lines[-1][rightmost_col].strip()
            
            if operation in ['*', '+']:
                if operation == '*':
                    result = 1
                    for num in current_problem_numbers:
                        result *= num
                else:  # operation == '+'
                    result = sum(current_problem_numbers)
                
                result_all += result
    
    return result_all

def main():
    result = part1()
    print("Part 1:", result)
    
    result2 = part2()
    print("Part 2:", result2)

if __name__ == "__main__":
    main()
