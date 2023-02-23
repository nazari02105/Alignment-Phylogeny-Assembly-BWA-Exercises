import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_solution(self, dist):
        to_return = []
        for node in range(self.V):
            to_return.append(dist[node])
        return to_return

    def min_distance(self, dist, spt_set):
        def_min = sys.maxsize
        min_index = None
        for u in range(self.V):
            if dist[u] < def_min and not spt_set[u]:
                def_min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for count in range(self.V):
            x = self.min_distance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        return self.print_solution(dist)


if __name__ == "__main__":
    file1 = open('Q1.txt', 'r')
    main_list = []
    while True:
        line = file1.readline()
        if not line:
            break
        content = line.strip()
        main_list.append(content)
    file1.close()
    n = int(main_list[0])
    main_list = main_list[1:]
    start_nodes = []
    end_nodes = []
    weight_edges = []
    largest_node = -1
    for item in main_list:
        first_split = item.split("->")
        first_number = int(first_split[0])
        second_split = first_split[1].split(":")
        second_number = int(second_split[0])
        weight = int(second_split[1])
        start_nodes.append(first_number)
        end_nodes.append(second_number)
        weight_edges.append(weight)
        if first_number > largest_node:
            largest_node = first_number
        if second_number > largest_node:
            largest_node = second_number
    largest_node += 1
    g = Graph(largest_node)
    to_pass = [[0 for _ in range(largest_node)] for _ in range(largest_node)]
    for i in range(len(start_nodes)):
        to_pass[start_nodes[i]][end_nodes[i]] = weight_edges[i]
    g.graph = to_pass
    for i in range(n):
        returned = g.dijkstra(i)[:n]
        print(*returned, sep=" ")