import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Pass one input file as argument.")
        input("Press any key to finish...")
        sys.exit()
    inputFile = open(sys.argv[1], "r")
    data = inputFile.readlines()
    analyze_data(data)

def analyze_data(data):
    total = 0
    for line in data:
        first = get_first_num(line)
        last = get_last_num(line)
        total += int(first + last) 
    print("Calibration number: {}".format(total))
    input("Press any key to finish...")

def get_first_num(line):
    for c in line:
        if (c.isdigit()):
            return c
    return 0

def get_last_num(line):
    for c in reversed(line):
        if (c.isdigit()):
            return c
    return 0

if __name__ == "__main__":
    main()