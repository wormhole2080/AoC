
import numpy as np

def sol(part):
    with open("2023 9.txt") as input_file:
        lines = input_file.read().strip().split('\n')
        for line in lines:
            series = []
            series.append(line.split(" "))

            while not np.all(series[-1]==0):
                series.append(np.diff(np.array(series[-1], dtype=np.uint16),n=1))

            i=0
            while not (i+2) > len(series):
                series[-2-i].append(series[-2-i][-1] + series[-1-i][-1])
                i+=1


    return series[1][-1]

if __name__ == "__main__":
    print(sol(1))
    #print(sol(2))
