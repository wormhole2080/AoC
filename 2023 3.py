import numpy as np
import csv
import itertools
from itertools import product
import re

def sol(part):
    #data_array = np.genfromtxt("2023 3.txt", delimiter=1)

    adjacents = list(itertools.product([-1,0,1],[-1,0,1]))

    with open("2023 3.txt",'r') as input_file:
        lines = input_file.read().strip().splitlines()
        s = "[]()!@#$%^&*-=_+~<>?/;:,|"
        coord_char = []
        coord_num=[]
        for x, line in enumerate(lines):
            coord_num = list(itertools.chain(re.finditer(r'\d{2,3}', line)))
            #coord_char = itertools.chain(re.finditer(r'/ [-._!"#%&,:;<>=@{}~\$\(\)\*\+\/\\\?\[\]\^\|]+/]', line))
            for y, chr in enumerate(line):
                if chr in s: #character found:
                    coord_char.append([x,y])
        coord_num.append
    return coord_char

#def adjacents(idx,dimensions):
def convert_by_list_comprehension(size):
    [e for e in iter(range(size))]

if __name__ == "__main__":
            print(sol(1))
            print(sol(2))
