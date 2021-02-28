"""
    Course Organizer w/ Toposort using Python
    Author: Rayhan Alghifari Fauzta (13519039)
    References: 
        - https://www.geeksforgeeks.org/topological-sorting/
        - https://www.youtube.com/watch?v=eL-KzMXSXXI
        - https://stackoverflow.com/questions/15038876/topological-sort-python
"""

""" 
    Read from file
    Proses: membersihkan tanda koma dan titik dari masukan file
    Output: list of courses 
"""
def read_file():
    filename = input('Masukkan test case (tanpa ".txt"): ')
    with open("../test/" + filename + ".txt") as f:
        lines = f.read().strip().split("\n")
    
    clear_comma = []
    for l in lines:
        clear_comma.append(l.replace(",", ' '))
    
    clear_stop = []
    for l in clear_comma:
        clear_stop.append(l.replace(".", ''))
    
    return clear_stop
    

""" 
    Create adjacency list from list of courses
    Input: list of courses
    Proses: untuk setiap elemen list of courses, diambil course pertama sebagai keys dan course setelahnya sebagai values
    Output: adjacency list in the form dictionary
"""
def make_adj_list(courses):
    adj = {}
    for course in courses:
        ls = course.split()
        adj[ls[0]] = ls[1:]

    return adj

"""
    Algoritma depth first search dalam graph
    Input: 
    graph - input graf dalam bentuk adjacency list yg disimpan pada dictionary
    start - starting node
    visited - kumpulan node yg sudah dikunjungi, disimpan dalam bentuk set
    order - topological order dari node-node dalam graph, disimpan dalam bentuk dict
    current_order - order yg sedang dikunjungi, disimpan dalam bentuk list
"""
def dfs(graph, start, visited, order, current_order):
    visited.add(start)
    for node in graph[start]: 
        if node not in visited:
            dfs(graph, node, visited, order, current_order)
    
    if start in graph: 
        for node in graph[start]:
            if node not in visited:
                dfs(graph, node, visited, order, current_order)
    
    order[current_order[0]] = start
    current_order[0] = current_order[0] - 1

"""
    Performs and outputs a topological sort of graph G using dfs
    Input: adjacency list, topological order dari node
"""
def topological_sort(graph, order):
    visited = set()
    current_order = [len(graph)]
    for node in graph.keys():
        if node not in visited:
            dfs(graph, node, visited, order, current_order)

""" solver """
def dec_and_conq(adj_list):
    order_dict = dict()
    topological_sort(adj_list, order_dict)
    result = iter(sorted(order_dict.items(), reverse = True))

    return result

""" print course per semester """
def print_result(result):
    sem = 1
    for __, node in result:
        print("Semester {}: ".format(sem), end='')
        print(node + ' ')
        sem += 1

""" main program """
def main() :
    file = read_file()
    adj_list = make_adj_list(file)
    result = dec_and_conq(adj_list)
    print_result(result)

if __name__ == "__main__":
    main()