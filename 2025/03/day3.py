# Pre-Process Input
def processInput(file):
    with open(file, "r") as f:
        banks = [line.strip() for line in f.readlines()]
    return banks

# Two pass greedy
def part1():
    batteries = processInput("day3-input.txt")
    joltage = 0

    for bank in batteries:
        max1 = 0
        max10 = 0
        max10pos = 0
        # First pass, max 10 digit
        for i in range (len(bank) - 1):
            if int(bank[i]) > max10:
                max10 = int(bank[i])
                max10pos = i

        #Second pass, max 1 digit
        for i in range(max10pos + 1, len(bank)):
            # print(i)
            max1 = max(max1, int(bank[i]))

        # add up
        joltage += (max10 * 10 + max1)

    return joltage

def main():
    res = part1()
    print ("Part 1: ", res)
    # res = part2()
    # print ("Part 2: ", res)

if __name__ == "__main__":
    main()
