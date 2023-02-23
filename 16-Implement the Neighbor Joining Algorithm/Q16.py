# with especial thanks to: https://www.tenderisthebyte.com/blog/2022/08/31/neighbor-joining-trees/
file1 = open('Q5.txt', 'r')
main_list = []
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
n = int(main_list[0])
main_distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
main_list = main_list[1:]
for i in range(n):
    for j in range(n):
        main_distance_matrix[i][j] = int(main_list[i].split()[j])


def get_total_distance_of_each_leaf(matrix):
    to_return = []
    for row in matrix:
        to_return.append(sum(row))
    return to_return


def update_distance_matrix(neighbours_def, clusters_def, matrix_row_def, r1, matrix_col_def, r2):
    length = len(neighbours_def)
    neighbours_def.append([])
    neighbours_def[length].append((clusters_def[matrix_row_def], r1))
    neighbours_def[clusters_def[matrix_row_def]].append((length, r1))
    neighbours_def[length].append((clusters_def[matrix_col_def], r2))
    neighbours_def[clusters_def[matrix_col_def]].append((length, r2))
    concat_clusters(clusters_def, matrix_row_def, matrix_col_def)
    clusters_def.append(length)


def get_multiplied_matrix(matrix, number):
    to_return = []
    for i_def in matrix:
        to_return.append([])
        for j_def in i_def:
            to_return[-1].append(j_def * number)
    return to_return


def add_vector(vector1, vector2):
    to_return = []
    for i_def in range(len(vector1)):
        to_return.append(vector1[i_def] + vector2[i_def])
    return to_return


def get_min(matrix):
    min_value = 1000000
    min_row = -1
    min_col = -1
    for first_layer in range(len(matrix)):
        for second_layer in range(len(matrix[first_layer])):
            if matrix[first_layer][second_layer] < min_value:
                min_value = matrix[first_layer][second_layer]
                min_row = first_layer
                min_col = second_layer
    return min_row, min_col


def vector_number_dif(vector, number):
    to_return = []
    for i_def in vector:
        to_return.append(i_def - number)
    return to_return


def not_to_change(vector):
    to_return = []
    for i_def in vector:
        to_return.append(i_def)
    return to_return


def delete_rows(matrix, to_delete):
    to_return = []
    for i_def in range(len(matrix)):
        if i_def not in to_delete:
            to_return.append(matrix[i_def])
    return to_return


def matrix_by_vector_row_dif(matrix, vector):
    to_return = []
    for i_def in matrix:
        to_return.append([])
        for j_def in range(len(i_def)):
            to_return[-1].append(i_def[j_def] - vector[j_def])
    return to_return


def print_result(result):
    counter = -1
    for nodes in result:
        counter += 1
        for key, value in nodes:
            print(str(counter) + '->' + str(key) + ':' + '%0.3f' % value)


def get_empty_result(number):
    return [cluster_index for cluster_index in range(number)], [[] for _ in range(number)]


def vector_number_div(vector, number):
    to_return = []
    for i_def in vector:
        to_return.append(i_def / number)
    return to_return


def matrix_by_vector_col_dif(matrix, vector):
    to_return = []
    for i_def in range(len(matrix)):
        to_return.append([])
        for j_def in matrix[i_def]:
            to_return[-1].append(j_def - vector[i_def])
    return to_return


def get_total_distance_and_to_reduced_matrix(distance_def, number):
    return get_total_distance_of_each_leaf(distance_def), \
           change_diagonal(
               matrix_by_vector_col_dif(matrix_by_vector_row_dif(get_multiplied_matrix(distance_def, number - 2),
                                                                 get_total_distance_of_each_leaf(
                                                                     distance_def)),
                                        get_total_distance_of_each_leaf(distance_def)))


def do_iteration(distance_def, matrix_row_def, matrix_col_def):
    matrix_calculation = matrix_calculator(distance_def, matrix_row_def, matrix_col_def)
    distance_def.append(not_to_change(matrix_calculation))
    matrix_calculation.append(0)
    distance_def = delete_some_cols(
        delete_rows(add_col(distance_def, matrix_calculation), [matrix_row_def, matrix_col_def]),
        [matrix_row_def, matrix_col_def])
    return distance_def


def change_diagonal(matrix):
    to_return = []
    for i_def in range(len(matrix)):
        to_return.append([])
        for j_def in range(len(matrix[i_def])):
            if i_def == j_def:
                to_return[-1].append(0)
            else:
                to_return[-1].append(matrix[i_def][j_def])
    return to_return


def matrix_calculator(distance_def, matrix_row_def, matrix_col_def):
    return vector_number_div(
        vector_number_dif(
            add_vector(distance_def[matrix_row_def], distance_def[matrix_col_def]),
            distance_def[matrix_row_def][matrix_col_def]
        ),
        2
    )


def concat_clusters(clusters_def, matrix_row_def, matrix_col_def):
    if matrix_row_def < matrix_col_def:
        del clusters_def[matrix_col_def]
        del clusters_def[matrix_row_def]
        return
    del clusters_def[matrix_row_def]
    del clusters_def[matrix_col_def]


def add_col(matrix, col):
    to_return = []
    for i_def in range(len(col)):
        this_time = []
        for j_def in matrix[i_def]:
            this_time.append(j_def)
        this_time.append(col[i_def])
        to_return.append(this_time)
    return to_return


def delete_some_cols(matrix, list_to_delete):
    to_return = []
    for i_def in matrix:
        to_return.append([])
        for j_def in range(len(i_def)):
            if j_def not in list_to_delete:
                to_return[-1].append(i_def[j_def])
    return to_return


clusters, adjacency = get_empty_result(n)
while True:
    if n == 2:
        break
    each_distance_matrix, distance_matrix = get_total_distance_and_to_reduced_matrix(main_distance_matrix, n)
    matrix_row, matrix_col = get_min(distance_matrix)
    r1 = (main_distance_matrix[matrix_row][matrix_col] + (
            (each_distance_matrix[matrix_row] - each_distance_matrix[matrix_col]) / (n - 2))) / 2
    r2 = (main_distance_matrix[matrix_row][matrix_col] - (
            (each_distance_matrix[matrix_row] - each_distance_matrix[matrix_col]) / (n - 2))) / 2
    main_distance_matrix = do_iteration(main_distance_matrix, matrix_row, matrix_col)
    update_distance_matrix(adjacency, clusters, matrix_row, r1, matrix_col, r2)
    n -= 1
adjacency[len(adjacency) - 1].append((len(adjacency) - 2, main_distance_matrix[0][1]))
adjacency[len(adjacency) - 2].append((len(adjacency) - 1, main_distance_matrix[0][1]))
print_result(adjacency)