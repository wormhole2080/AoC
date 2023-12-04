import re
import csv

def sol(part):

    with open("2023 1.txt") as input_file:
        values = input_file.read().strip().split('\n')
        summed = []
        for value in values:
            if part == 2:
                value = convert_to_numbers(value)
            
            digits = [int(s) for s in [*value] if s.isdigit() ]
            
            valOne = int(digits[0])*10 + int(digits[-1])
            
            summed.append(valOne)
        return sum(summed)

def convert_to_numbers(s):
   
    words_to_numbers = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }
 
    pattern = re.compile(r'(' + '|'.join(words_to_numbers.keys()) + r')')
    s = re.sub(pattern, lambda x: words_to_numbers[x.group()], s) #twice because of overlaps
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], s)
 
def csvwriter(c):

    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(c)

if __name__ == "__main__":
    print(sol(1))
    print(sol(2))
    