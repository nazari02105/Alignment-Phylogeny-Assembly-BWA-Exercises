def when_not_exist(main_matrix_def, first_index, prev_q_value, before, now, value, distances):
    main_matrix_def.append({})
    main_matrix_def[first_index][len(main_matrix_def) - 1] = prev_q_value
    main_matrix_def[len(main_matrix_def) - 1][first_index] = prev_q_value
    main_matrix_def[before].pop(now)
    main_matrix_def[now].pop(before)
    main_matrix_def[before][len(main_matrix_def) - 1] = value - distances[before]
    main_matrix_def[len(main_matrix_def) - 1][before] = value - distances[before]
    main_matrix_def[now][len(main_matrix_def) - 1] = distances[now] - value
    main_matrix_def[len(main_matrix_def) - 1][now] = distances[now] - value


def to_build(value, distance, before, main_matrix_def, first_index, prev_q_value, now):
    if value == distance[before]:
        main_matrix_def[before][first_index] = prev_q_value
        main_matrix_def[first_index][before] = prev_q_value
        return
    when_not_exist(main_matrix_def, first_index, prev_q_value, before, now, value, distance)


file1 = open('Q3.txt', 'r')
main_list = []
while True:
    line = file1.readline()
    if not line:
        break
    content = line.strip()
    main_list.append(content)
n = int(main_list[0])
main_list = main_list[1:]
main_distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        main_distance_matrix[i][j] = int(main_list[i].split()[j])
counter = -1
enterance_of_algorithm = [{} for _ in range(n)]
enterance_of_algorithm[0][1] = main_distance_matrix[0][1]
enterance_of_algorithm[1][0] = main_distance_matrix[1][0]
tuple_value = None
for j in range(2, n):
    prev_question_value = 1000000
    # this is exactly previous question
    i = j - 1 if j > 0 else j + 1
    for k in range(j + 1):
        if i != k and k != j:
            now_one = (main_distance_matrix[i][j] + main_distance_matrix[j][k] - main_distance_matrix[i][k]) // 2
            if now_one < prev_question_value:
                prev_question_value = now_one
                tuple_value = (i, k)
    # end of previous question
    i = tuple_value[0]
    k = tuple_value[1]
    value = main_distance_matrix[i][j] - prev_question_value
    main_distance_list = [1000000 if index != i else 0 for index in range(len(enterance_of_algorithm))]
    edges_list = [-1000000 for _ in range(len(enterance_of_algorithm))]
    FIFO = [i]
    check = True
    while len(FIFO) != 0 and check:
        now_compute = FIFO.pop(0)
        for node, weight in enterance_of_algorithm[now_compute].items():
            if main_distance_list[node] == 1000000:
                main_distance_list[node] = main_distance_list[now_compute] + weight
                edges_list[node] = now_compute
                FIFO.append(node)
                if node == k:
                    next_compute = node
                    while value < main_distance_list[next_compute]:
                        now_compute = next_compute
                        next_compute = edges_list[now_compute]
                    to_build(value, main_distance_list, next_compute, enterance_of_algorithm, j, prev_question_value, now_compute)
                    check = False
                    break
for to_print in enterance_of_algorithm:
    counter += 1
    for dict_key, dict_value in to_print.items():
        print(str(counter) + '->' + str(dict_key) + ':' + str(dict_value))