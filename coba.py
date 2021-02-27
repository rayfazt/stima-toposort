"""
    Course Organizer w/ Toposort using Python
    Author: Rayhan Alghifari Fauzta (13519039)
    References: 
        - https://www.geeksforgeeks.org/topological-sorting/
        - https://www.youtube.com/watch?v=eL-KzMXSXXI
        - https://stackoverflow.com/questions/15038876/topological-sort-python
"""

from collections import defaultdict

""" read from file & create adjacency list """
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

"""
    Performs a depth first search in graph G starting from vertex s
    Input: G - the input graph in the adjacency list representation via a dictionary
    s - the starting vertex
    explored - a set of explored vertices
    distance - a dictionary representing the topological order of the vertices
    current_label - the current order of the topological order, disguised as a mutable list
"""
def dfs(G, s, explored, distance, current_label):
    explored.add(s)
    #print G[s]
    for v in G[s]: # for every edge (s, v)
        if v not in explored:
            dfs(G, v, explored, distance, current_label)
    
    if s in G: 
        for v in G[s]:
            if v not in explored:
                dfs(G, v, explored, distance, current_label)
    
    distance[current_label[0]] = s
    current_label[0] -= 1

"""
    Performs and outputs a topological sort of graph G using dfs
    Input: G - the input graph in the adjacency list representation via a dictionary
    distance - a dictionary representing the topological order of the vertices
"""
def topological_sort(G, distance):
    explored = set()
    current_label = [len(G)]
    for v in G.keys():
        if v not in explored:
            dfs(G, v, explored, distance, current_label)

""" main program """
def main() :
    f = "test2"
    d = makeAdjList(f)
    print("G:", d)
    distance = dict()
    topological_sort(d, distance)
    topo = iter(sorted(distance.items()))
    print("A topological order of G is:")
    for __, vertex in topo:
        print( vertex + " ")
    print()

if __name__ == "__main__":
    main()