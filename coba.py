from collections import defaultdict

def makeAdjList(filename):
    with open(filename + ".txt") as f:
        lines = f.read().strip().split("\n")
    
    temp_lines = []
    for l in lines:
        temp_lines.append(l.replace(",", ' '))
    
    final_lines = []
    for l in temp_lines:
        final_lines.append(l.replace(".", ''))
    
    d = defaultdict(list)

    for line in final_lines:
        ls = line.split(" ")
        d[ls[0]] = ls[1:]

    return d

f = "test1"
d = makeAdjList(f)
print(d)