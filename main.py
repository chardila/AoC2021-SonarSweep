# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    INPUT_FILE = "inputs/01_sonar_sweep.txt"

    with open(INPUT_FILE, "r") as f:
        file = f.read()

    depths = [int(i) for i in file.split('\n')]

    count = 0
    for i in range(len(depths) - 1):
        if depths[i] < depths[i + 1]:
            count += 1

    print("Sonar Sweep - Part 1:", count)
