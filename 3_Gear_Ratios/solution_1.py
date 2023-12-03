import sys
import hashlib

file = 'input_example.txt'
schema = []

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        schema.append(line.strip())
    analyze_schema()
    #print('answer: ', answer)
    input()
        
def analyze_schema():
    for lineIndex, line in enumerate(schema):
        numStarted = -1
        numFinished = -1
        for index, c in enumerate(line):
            if (numStarted == -1 and c.isdigit()):
                numStarted = index
            elif (numStarted != -1 and not c.isdigit()):
                numFinished = index
            if (numStarted != -1 and numFinished != -1):
                is_part(lineIndex, numStarted, numFinished)
                numStarted == -1
                numFinished == -1
        if (numStarted != -1):
            numFinished = index
            is_part(lineIndex, numStarted, numFinished)

def is_part(line, start, end):
    print("NUMS: {}".format(schema[line][start:end]), line, start, end)
    print("TOP: ", check_top(line, start, end))
    print("BOT: ", check_bot(line, start, end))
    print("LFT: ", check_left(line, start))
    print("RGT: ", check_right(line, end))
    input()
    #check_top_left(line, start, end)
    #check_top_right(line, start, end)
    #check_bot_left(line, start, end)
    #check_bot_right(line, start, end)

def check_top(line, start, end):
    if (line == 0):
        return False
    for c in schema[line - 1][start:end]:
        print(c, end="")
        if (not c.isdigit() and c != '.'):
            return True
    return True

def check_bot(line, start, end):
    if (line == len(schema) - 1):
        return False
    for c in schema[line + 1][start:end]:
        if (not c.isdigit() and c != '.'):
            return True
    return True

def check_left(line, start):
    if (start == 0):
        return False
    c = schema[line][start - 1]
    if (not c.isdigit() and c != '.'):
        return True
    return True

def check_right(line, end):
    if (end == len(schema[line]) - 1):
        return False
    c = schema[line][end]
    if (not c.isdigit() and c != '.'):
        return True
    return True
    

                


if __name__ == "__main__":
    main()