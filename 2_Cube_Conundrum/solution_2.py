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
        minCubes = get_game_set_min_cubes(cutLine[1])
        cubesPower = get_cubes_power(minCubes)
        total += cubesPower
    print("Total: ", total)
    input()
        
def get_cubes_power(minCubes):
    total = 1
    for key in minCubes:
        total *= int(minCubes[key])
    return total

def get_game_set_min_cubes(line):
    gameSets = line.split(';')
    minCubes = {}
    for gameSet in gameSets:
        revealDict = get_reveal_dict(gameSet)
        for key in revealDict:
            if (key not in minCubes or int(minCubes[key]) < int(revealDict[key])):
                minCubes[key] = revealDict[key]
    return minCubes

def get_reveal_dict(gameSet):
    reveals = gameSet.split(',')
    revealArr = []
    for reveal in reveals:
        revealArr.append(reveal.strip().split(' ')[::-1])
    return dict(revealArr)
        
        


if __name__ == "__main__":
    main()