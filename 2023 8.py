import re

def sol(part):
    with open("2023 8.txt") as input_file:
        lines = input_file.read().strip().split('\n')
        dirs = lines[0]

        nodes = {}
        for line in lines[2:]:
            #arr = np.asarray(line.split(" = "))
            arr = re.split(r"[\b\W\b]+", line)
            nodes[arr[0]] = {}
            nodes[arr[0]]['L'] = arr[1]
            nodes[arr[0]]['R'] = arr[2]

    if part==1:
        return navigate(nodes, dirs)

    if part ==2:
        return navigateMultiple(nodes, dirs)

def navigate(nodes, dirs):
        i = 0; current = 'AAA'
        n = len(dirs)
        while current !='ZZZ':
            current = nodes[current][dirs[i%n]]
            i+=1
            if i>10000000:
                break
        return i
def navigateMultiple(nodes, dirs):
    i = 0; current = []

    current = [node for node, value in nodes.items() if node.endswith("A")]
    n = len(dirs)

    while (len([a for a in current if a.endswith("Z")]) != len(current)):
        current = [nodes[a][dirs[i % n]] for a in current]
        i += 1
        print(i)
    return i


if __name__ == "__main__":
    #print(sol(1))
    print(sol(2))
