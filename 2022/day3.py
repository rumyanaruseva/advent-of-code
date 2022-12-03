
GROUP_SIZE = 3

# Priority
def get_priority(elem):
    if elem.islower():
        # 'a' = 97, 'b' = 98, ...
        return ord(elem) - 96
    if elem.isupper():
        # 'A' = 65, 'B' = 66, ...
        return ord(elem) - 38
    return 0

# Part 1
def day3_part1():
    f = open("day3-input.txt", "r")
    priority_sum = 0

    for line in f:
        str1 = line[ :len(line)//2]     # first half
        str2 = line[len(line)//2: ]     # second half
        inter = set(str1) & set(str2)   # compartments intersection
        priority_sum += get_priority(inter.pop())

    return priority_sum

# Part 2
def day3_part2():
    f = open("day3-input.txt", "r")

    groups = [set() for i in range(GROUP_SIZE)]
    priority_sum = 0
    group_count = 0

    for line in f:
        groups[group_count] = line
        group_count += 1

        if group_count >= GROUP_SIZE:
            group_count = 0
            inter = set(groups[0])
            for g in groups:
                inter = inter.intersection(g)
            inter.discard('\n')
            priority_sum += get_priority(inter.pop())

    return priority_sum

# Day 3
print("Day 3, part 1: ", day3_part1())
print("Day 3, part 2: ", day3_part2())
