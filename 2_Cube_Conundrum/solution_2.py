import sys

max_cubes = {'red': '12', 'green': '13', 'blue': '14'}
file = 'input.txt'

def main():
	inputFile = open(file, 'r')
	data = inputFile.readlines()
	analyze_data(data)

def analyze_data(data):
    total = 0
    for count, line in enumerate(data):
        cutLine = line.strip().split(':')
        if (is_game_possible(cutLine[1])):
            total += count + 1
    print(total)
    input()
        
def is_game_possible(line):
    gameSets = line.split(';')
    for gameSet in gameSets:
        reveals = gameSet.split(',')
        revealArr = []
        for reveal in reveals:
            revealArr.append(reveal.strip().split(' ')[::-1])
        revealDict = dict(revealArr)
        for key in revealDict:
            if (int(revealDict[key]) > int(max_cubes[key])):
                return False
    return True

        
        


if __name__ == "__main__":
    main()