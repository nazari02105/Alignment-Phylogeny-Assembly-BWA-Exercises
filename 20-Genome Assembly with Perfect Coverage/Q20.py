file1 = open('Q3.txt', 'r')
main_list = list()
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
file1.close()
main_list = [*set(main_list)]
graph_edges = list()
for i in main_list:
    graph_edges.append([i[0:len(main_list[0])-1], i[1:len(main_list[0])]])
first_element = graph_edges.pop(0)
result = first_element[0][-1]
while graph_edges:
    result += first_element[1][-1]
    first_element = graph_edges.pop([i for i, pair in enumerate(graph_edges) if pair[0] == first_element[1]][0])
print(result)