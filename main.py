# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    INPUT_FILE = "inputs/01_sonar_sweep.txt"

    with open(INPUT_FILE, "r") as f:
        depths = [int(line) for line in f]

    count = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            count += 1

    print("Sonar Sweep - Part 1:", count)

    count2 = 0
    for i in range(3, len(depths)):
        left = depths[i - 3] + depths[i - 2] + depths[i - 1]
        right = depths[i - 2] + depths[i - 1] + depths[i]
        if left < right:
            count2 += 1

    print("Sonar Sweep - Part 2:", count2)
