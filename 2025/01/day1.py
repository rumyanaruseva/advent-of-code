def processInput(file):

    with open(file, "r") as f:
        lines = f.read().strip().split("\n")

    dials = []
    for dial in lines:
        num = int(dial[1:])
        if dial[0] == "L":
            num = num * -1
        dials.append(num)

    return dials

def part1():

    rotations = processInput("day1-input.txt")
    dial = 50
    count = 0

    for r in rotations:
        dial = (dial + r) % 100
        if dial == 0: count += 1

    return count

def part2():

    rotations = processInput("day1-input.txt")
    dial = 50
    count = 0

    # step through the rotations one by one
    for r in rotations:
        if r > 0:
            for _ in range(r):
                dial = (dial + 1) % 100
                if dial == 0:
                    count += 1
        if r < 0:
            for _ in range(-r):
                dial = (dial - 1) % 100
                if dial == 0:
                    count += 1

    return count

def main():
    res = part1()
    print ("Part 1: ", res)
    res = part2()
    print ("Part 2: ", res)

if __name__ == "__main__":
    main()
