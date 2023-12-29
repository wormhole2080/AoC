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

    empty_rows, empty_cols = empty_dimensions(universe)

    if part ==1:
        expansion = (2-1)
    elif part ==2:
        expansion=(1000000-1)

    galaxies = find_galaxies(universe)

    for i, galaxy in enumerate(galaxies):
        for j, other_galaxy in enumerate(galaxies):
            if j > i:
                distance += distance_1dimension_scaled(galaxy[0], other_galaxy[0], empty_rows, expansion)
                distance += distance_1dimension_scaled(galaxy[1], other_galaxy[1], empty_cols, expansion)
    return distance
def find_galaxies(universe):
    galaxies=[]
    for x, line in enumerate(universe):
        for y, char in enumerate(line):
            if '#' in char:
                galaxies.append([x,y])
    return galaxies

def distance_1dimension_scaled(a, b, empties, expansion) -> int:
    Max = max(a,b)
    Min = min(a,b)

    return Max - Min + (sum( Min <= x <= Max for x in empties)) * expansion

def parse_input(input):
    lines = input.split('\n')
    output = []
    for line in lines:
        output.append([*line])
    return output

def empty_dimensions(universe):
    empty_rows = find_empty(universe)
    universe = np.array(universe).T.tolist()
    empty_cols = find_empty(universe)

    return empty_rows, empty_cols

def find_empty(universe):
    empty_lines = []
    for x, line in enumerate(universe):
        if not any('#' in i for i in enumerate(line)):
            empty_lines.append(x)
    return empty_lines

if __name__ == "__main__":
    input = open("2023_11.txt").read()
    print(sol(1, input))
    print(sol(2, input))
