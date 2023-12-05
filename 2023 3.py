import numpy as np
import csv

def sol(part):

    with open("2023 3.txt") as input_file:
        reader = csv.reader(input_file)
        data = list(reader)

        data_array = np.array(data)
        s = "[]()!@#$%^&*-=_+~<>?/\;:|"
        for idx, x in np.ndenumerate(data_array):
            if s.find(x) ==-1: #character found


if __name__ == "__main__":
            print(sol(1))
            print(sol(2))
