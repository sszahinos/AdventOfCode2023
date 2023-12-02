import sys
# Itero los carácteres
# Si encuentro un número -> primer numero encontrado
# Si no, cojo el substring hasta el siguiente número (o final)
#   itero el substring y compruebo si puede formar alguno de los números
#   si se forma -> transformar a núm
#
#
#
#
file = 'input.txt' 
NUMS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for line in data:
        line = line.strip()
        first = str(get_first_num(line))
        last = str(get_last_num(line))
        total += int(first + last) 
    print("Calibration number: {}".format(total))
    input("Press any key to finish...")

def get_first_num(line):
    for index, c in enumerate(line):
        if (c.isdigit()):
            return c
        else:
            word = get_word(line, index)
            number = get_number(word)
            if (number != -1):
                return number
    return 0

def get_word(line, index):
    for endIndex, c in enumerate(line[index:]):
        if (c.isdigit()):
            return line[index:endIndex + index]
    return line[index:]

def get_number(word):
    for index in range(1, len(word)):
        if (word[:index + 1] in  NUMS):
            return NUMS.index(word[:index + 1])
    return -1
                
def get_last_num(line):
    for index, c in enumerate(reversed(line)):
        if (c.isdigit()):
            return c
        else:
            word = get_word(line, (index + 1) * -1)
            number = get_number(word)
            if (number != -1):
                return number
    return 0

if __name__ == "__main__":
    main()