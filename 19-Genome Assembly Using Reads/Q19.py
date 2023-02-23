import copy

convert_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}


def rev_comp(string):
    rev_com = ""
    reversed_seq = string[::-1]
    for character in reversed_seq:
        rev_com += str(convert_dict[character])
    return rev_com


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(self.v)]

    def number_of_connected_components(self):
        global connected_components_list
        visited = [False for _ in range(self.v)]
        count = 0
        for v in range(self.v):
            if not visited[v]:
                connected_components_list.append([])
                self.dfs_util(v, visited, count)
                count += 1
        return count

    def dfs_util(self, v, visited, count):
        visited[v] = True
        for i_def in self.adj[v]:
            if not visited[i_def]:
                break
                self.dfs_util(i_def, visited, count)

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


def create_edge(element, graph):
    k = len(list(graph)[0])
    return [element[0:k - 1], element[1:k]]


def q1_job(the_list):
    reverse_complement_list = list()
    for seq in the_list:
        rev_com = ""
        reversed_seq = seq[::-1]
        for character in reversed_seq:
            rev_com += str(convert_dict[character])
        reverse_complement_list.append(rev_com)
    the_list += reverse_complement_list
    the_list = [*set(the_list)]
    to_return = []
    for seq in the_list:
        to_return.append((str(seq[:len(seq) - 1]), str(seq[1:])))
    return to_return


def break_k_mers(the_list, k):
    to_return = list()
    for seq in the_list:
        for i in range(0, len(seq) - k + 1):
            to_return.append(seq[i:i + k])
    return to_return


def create_graph(graph, input_file, k):
    for k_mer in input_file:
        for i in range(k):
            the_number = len(k_mer) + i - k + 1
            graph.add(k_mer[i:the_number])
            graph.add(rev_comp(k_mer[i:the_number]))


def solve(input_file):
    to_return = None
    for k in range(1, len(input_file[0])):
        my_graph = set()
        create_graph(my_graph, input_file, k)
        graph_edges = [create_edge(element, my_graph) for element in my_graph]
        to_return = []
        for _ in range(2):
            popped = graph_edges.pop(0)
            last_char = popped[0][-1]
            while popped[1] in [edge[0] for edge in graph_edges]:
                last_char += popped[1][-1]
                [new_list] = [i for i, pair in enumerate(graph_edges) if pair[0] == popped[1]]
                popped = graph_edges.pop(new_list)
            to_return.append(last_char)
        if len(graph_edges) == 0:
            break
    return to_return


def get_number_of_connected_components_for_each_k(the_list):
    global connected_components_list
    mapper_seq_to_number = dict()
    mapper_number_to_seq = dict()
    counter_def = 0
    for i_def in the_list:
        for j_def in i_def:
            if j_def not in mapper_seq_to_number.keys():
                mapper_seq_to_number[j_def] = counter_def
                mapper_number_to_seq[counter_def] = j_def
                counter_def += 1
    g = Graph(counter_def)
    connected_components_list = list()
    for i_def in the_list:
        g.add_edge(mapper_seq_to_number[i_def[0]], mapper_seq_to_number[i_def[1]])
    g.number_of_connected_components()

    # find cycles
    first_element_in_each_connected_component = list()
    N = 10000
    graph = [[] for _ in range(N)]
    cycles = [[] for _ in range(N)]

    def dfs_cycle(u, p, color_def, par_def):
        global cycle_number
        if color_def[u] == 2:
            return
        if color_def[u] == 1:
            v = []
            cur = p
            v.append(cur)
            while cur != u:
                cur = par_def[cur]
                v.append(cur)
            cycles[cycle_number] = v
            cycle_number += 1
            return
        par_def[u] = p
        color_def[u] = 1
        for v in graph[u]:
            if v == par_def[u]:
                continue
            dfs_cycle(v, u, color_def, par_def)
        color_def[u] = 2

    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)

    for i_def in the_list:
        add_edge(mapper_seq_to_number[i_def[0]] + 1, mapper_seq_to_number[i_def[1]] + 1)
    for i_def in first_element_in_each_connected_component:
        global cycle_number
        color = [0] * N
        par = [0] * N
        cycle_number = 0
        dfs_cycle(i_def, 0, color, par)


file1 = open('Q2.txt', 'r')
main_list = list()
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
file1.close()
main_list = [*set(main_list)]
connected_components_list = list()
cycle_number = 0
final_result = list()
counter = len(main_list[0])
while counter > 2:
    k_1_mer = break_k_mers(copy.deepcopy(main_list), counter)
    k_1_mer = [*set(k_1_mer)]
    returned = q1_job(copy.deepcopy(k_1_mer))
    final_result.append(returned)
    counter -= 1
for i in final_result:
    get_number_of_connected_components_for_each_k(copy.deepcopy(i))
print(solve(main_list)[0])