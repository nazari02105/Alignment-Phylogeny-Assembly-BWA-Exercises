file1 = open('Q4.txt', 'r')
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


def create_matrix(matrix):
    for i_def in range(len(matrix)):
        matrix[i_def][i_def] = 1000000


def create_empty_result(number):
    return [[cluster_index, 1] for cluster_index in range(number)], \
           [[] for _ in range(number)], \
           [0. for _ in range(number)]


def delete_some_indexes(matrix, list_to_delete):
    to_return = []
    for i_def in range(len(matrix)):
        if i_def not in list_to_delete:
            to_return.append(matrix[i_def])
    return to_return


def get_positive(number):
    if number < 0:
        return number * -1
    return number


def delete_some_cols(matrix, list_to_delete):
    to_return = []
    for i_def in matrix:
        to_return.append(delete_some_indexes(i_def, list_to_delete))
    return to_return


def create_neighbour(neighbour, to_change, clusters_def, row_to_change, col_to_change):
    neighbour.append([])
    neighbour[to_change].append(clusters_def[row_to_change][0])
    neighbour[to_change].append(clusters_def[col_to_change][0])
    neighbour[clusters_def[row_to_change][0]].append(to_change)
    neighbour[clusters_def[col_to_change][0]].append(to_change)


def add_col(matrix, col):
    to_return = []
    for i_def in range(len(col)):
        this_time = []
        for j_def in matrix[i_def]:
            this_time.append(j_def)
        this_time.append(col[i_def])
        to_return.append(this_time)
    return to_return


def concat_clusters(clusters_def, matrix_row_def, matrix_col_def):
    if matrix_row_def < matrix_col_def:
        del clusters_def[matrix_col_def]
        del clusters_def[matrix_row_def]
        return
    del clusters_def[matrix_row_def]
    del clusters_def[matrix_col_def]


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


def next_level_matrix(dist_def, matrix_row_def, clusters_def, matrix_col_def):
    d_new = create_new_row(dist_def, matrix_row_def, clusters_def, matrix_col_def)
    d_new = delete_some_indexes(d_new, [matrix_row_def, matrix_col_def])
    dist_def = delete_some_indexes(dist_def, [matrix_row_def, matrix_col_def])
    dist_def = delete_some_cols(dist_def, [matrix_row_def, matrix_col_def])
    dist_def.append(copy_list(d_new))
    d_new.append(1000000)
    dist_def = add_col(dist_def, d_new)
    return dist_def


def multiply_list(matrix, number):
    for i_def in range(len(matrix)):
        matrix[i_def] = matrix[i_def] * number
    return matrix


def add_list(matrix1, matrix2):
    to_return = []
    for i_def in range(len(matrix1)):
        to_return.append(matrix1[i_def] + matrix2[i_def])
    return to_return


def copy_list(list_def):
    to_return = []
    for i_def in list_def:
        to_return.append(i_def)
    return to_return


def create_new_row(dist_def, matrix_row_def, clusters_def, matrix_col_def):
    return div_list(
        add_list(
            multiply_list(not_to_change(dist_def, matrix_row_def), clusters_def[matrix_row_def][1]),
            multiply_list(not_to_change(dist_def, matrix_col_def), clusters_def[matrix_col_def][1])
        ),
        clusters_def[matrix_row_def][1] + clusters_def[matrix_col_def][1]
    )


def div_list(matrix, number):
    to_return = []
    for i_def in matrix:
        to_return.append(i_def / number)
    return to_return


def not_to_change(matrix, number):
    to_return = []
    for i_def in matrix[number]:
        to_return.append(i_def)
    return to_return


create_matrix(main_distance_matrix)
clusters, neighbours, age = create_empty_result(n)
while True:
    if len(main_distance_matrix) == 2:
        matrix_row, matrix_col = get_min(main_distance_matrix)
        change_i = len(neighbours)
        create_neighbour(neighbours, change_i, clusters, matrix_row, matrix_col)
        age.append(main_distance_matrix[matrix_row][matrix_col] / 2)
        break
    matrix_row, matrix_col = get_min(main_distance_matrix)
    change_i = len(neighbours)
    create_neighbour(neighbours, change_i, clusters, matrix_row, matrix_col)
    age.append(main_distance_matrix[matrix_row][matrix_col] / 2)
    clusters.append([change_i, clusters[matrix_row][1] + clusters[matrix_col][1]])
    main_distance_matrix = next_level_matrix(main_distance_matrix, matrix_row, clusters, matrix_col)
    concat_clusters(clusters, matrix_row, matrix_col)
new_neighbours = copy_list(neighbours)
for i in range(len(neighbours)):
    for j in range(len(neighbours[i])):
        new_neighbours[i][j] = (neighbours[i][j], get_positive(age[i] - age[neighbours[i][j]]))
counter = -1
for row in new_neighbours:
    counter += 1
    for key, value in row:
        print(str(counter) + '->' + str(key) + ':' + '%0.3f' % value)