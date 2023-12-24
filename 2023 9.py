
import numpy as np
import csv
from itertools import zip_longest  # Use zip_longest in Python 3.
from itertools import cycle

def sol(part):
    with open("2023 9.txt") as input_file:
        lines = input_file.read().strip().split('\n')

        aggregate = []

        for line in lines:

            series = []; i=0
            series.append(np.asarray(line.split(" "),dtype=np.int64))

            while not np.all(series[-1]==0):
                series.append(np.diff(np.array(series[-1], dtype=np.int64),n=1))

            if part ==1:
                while not (i+2) > len(series):
                    series[-2-i] = np.append(series[-2-i], int(series[-2-i][-1])+int(series[-1-i][-1]))
                    i+=1
                aggregate.append(series[0][-1])

            if part ==2:
                #series[-1] = np.concatenate(0,series[-1])
                i=len(series)-2
                while not i < 0:
                    series[i] = np.insert(series[i],0,(int(series[i][0]) - int(series[i+1][0])))
                    i-=1
                aggregate.append(series[0][0])

            with open("test.csv", "w+") as f:
                writer = csv.writer(f)
                for values in zip_longest(*series):
                    writer.writerow(values)

        return sum(aggregate)

if __name__ == "__main__":
    print(sol(1))
    print(sol(2))
