import numpy as np

sample = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def sol(part, input_file):
    universe = parse_input(input_file)
    distance = 0

    expanded_universe, empty_rows, empty_cols = expand_universe(universe)

    if part ==1:
        galaxies = find_galaxies(expanded_universe)

        for i, galaxy in enumerate(galaxies):
            for j, other_galaxy in enumerate(galaxies):
                if j > i:
                    distance += distance_1dimension(galaxy[0], other_galaxy[0]) + distance_1dimension(galaxy[1], other_galaxy[1])

    if part == 2:
        galaxies = find_galaxies(universe)

        for i, galaxy in enumerate(galaxies):
            for j, other_galaxy in enumerate(galaxies):
                if j > i:
                    distance += distance_1dimension_scaled(galaxy[0], other_galaxy[0],empty_rows) + distance_1dimension_scaled(galaxy[1],
                                                                                                      other_galaxy[1],empty_cols)

    return distance
def find_galaxies(universe):
    galaxies=[]
    for x, line in enumerate(universe):
        for y, char in enumerate(line):
            if '#' in char:
                galaxies.append([x,y])
    return galaxies

def distance_1dimension(a, b) -> int:
    return max(a,b) - min(a,b)

def distance_1dimension_scaled(a, b, empties) -> int:
    Max = max(a,b)
    Min = min(a,b)

    return Max - Min + (sum( Min <= x <= Max for x in empties)) * (10)

def parse_input(input):
    lines = input.split('\n')
    output = []
    for line in lines:
        output.append([*line])

    return output

def expand_universe(universe):
    universe, empty_rows = insert_rows(universe)
    universe = np.array(universe).T.tolist()
    universe, empty_cols = insert_rows(universe)
    universe = np.array(universe).T.tolist()

    return universe, empty_rows, empty_cols

def insert_rows(universe):
    empty = '.' * len(universe[0])
    flag_empty = False
    empty_lines = []

    for x, line in enumerate(universe):
        if flag_empty == True:
            flag_empty = False
            continue

        if not any('#' in i for i in enumerate(line)):
            universe.insert(x,[*empty])
            flag_empty = True
            empty_lines.append(x)

    return universe, empty_lines

def count(list1, l, r):
    c = 0
    # traverse in the list1
    for x in list1:
        # condition check
        if x>= l and x<= r:
            c+= 1
    return c

if __name__ == "__main__":
    input = sample #open("2023_11.txt").read())
    print(sol(1, input))
    print(sol(2, input))
