"""
    Course Organizer w/ Toposort
    Author: Rayhan Alghifari Fauzta (13519039)
"""

""" 
    Read from file
    Input: -
    Process: remove comma and stop from input file
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
    Create adjacency list
    Input: list of courses
    Process: take first element of course as key and its prerequisites as values
    Output: adjacency list (dictionary)
"""
def make_adj_list(courses):
    adj = {}
    for course in courses:
        ls = course.split()
        adj[ls[0]] = ls[1:]

    return adj


'''
    Topological sorting algorithm
    Input: adjacency list (dict), empty list of list, current iteration number (start from 0)
    Process: 
        1. find any node with zero incoming edge
        2. add the node to list with index according to iteration number
        3. make a copy of adjacency list, delete previously visited node as well as any edges containing its value
        4. repeat until all nodes are visited
    Output: list of courses per semester (list of list)
'''
def toposort(adj, list_smt, cur_smt):
    if (adj):
        for k, v in adj.items():
            if (len(adj[k]) == 0):
                list_smt[cur_smt].append(k)

        adj2 = adj.copy()
        for element in list_smt:
            for course in element:
                for k in list(adj2):
                    if k == course:
                        del adj2[k]
                for v in adj2.values():
                    for val in v:
                        if course in val:
                            v.remove(course)

        toposort(adj2, list_smt, cur_smt + 1)
        return list_smt


'''
    Print result with the following style:
        Semester 1: a, b,
        Semester 2: e, f, g, h
        Semester 3: i
            and so on
    Input: courses per semester (list of list)
    Process: printing result according to specified format
    Output: result printed
'''
def print_result(result):
    sem = 1
    for courses in result:
        if courses:
            course = ", ".join(courses)
            print("Semester {}:".format(sem), course)
            sem += 1


''' main program '''
def main():
    f = read_file()
    adj = make_adj_list(f)
    list_smt = [[] for _ in range(8)]
    cur_smt = 0
    result = toposort(adj, list_smt, cur_smt)
    print_result(result)

if __name__ == "__main__":
    main()