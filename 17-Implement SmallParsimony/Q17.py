char_to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
int_to_char = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


class Structures:
    @staticmethod
    def create_matrix_to_analyse(n_class, vector_class):
        to_return = [[] for _ in range(n_class)]
        to_return += [[] for _ in range(n_class)]
        for i_class in to_return:
            i_class += [vector_class]
        return to_return

    @staticmethod
    def not_to_change(vector):
        to_return = []
        for i_class in vector:
            to_return.append(i_class)
        return to_return


def read_from_file():
    file1 = open('Q6.txt', 'r')
    main_list = []
    while True:
        line = file1.readline()
        if not line:
            break
        main_list.append(line.strip())
    first_line_number = int(main_list[0])
    main_list = main_list[1:]
    return first_line_number, main_list


def get_empty_result(nu):
    Structures.create_matrix_to_analyse(nu, Structures.not_to_change([] for _ in range(nu)))
    return [[] for _ in range(nu)], [[] for _ in range(nu)], [dict() for _ in range(nu)], ['' for _ in range(nu)]


def k_update(left_operator, right_operator, neighbours, index_def, first_def):
    if left_operator != right_operator:
        neighbours[index_def][first_def] += 1
        neighbours[first_def][index_def] += 1


def print_result(neighbours, result_int):
    print(result_int)
    counter = -1
    for neighbour_i in neighbours:
        counter += 1
        for key, value in neighbour_i.items():
            print(parts[counter] + '->' + parts[key] + ':' + str(value))


def update_neighbours(neighbours_second_def, first_def, main_parts_def, int_to_char_def, third_def, forth_def,
                      fifth_def, fifo):
    if len(neighbours_second_def[first_def]) > 0:
        main_parts_def[first_def] += int_to_char_def[third_def]
        main_parts_def[forth_def] += int_to_char_def[fifth_def]
        Structures.create_matrix_to_analyse(forth_def, Structures.not_to_change(main_parts_def))
        fifo.append((first_def, third_def))
        fifo.append((forth_def, fifth_def))
        Structures.create_matrix_to_analyse(fifth_def, Structures.not_to_change(fifo))


def update_results(left_operator, third_def, neighbours_def, vector, first_def, fifth_def, forth_def, neighbours_second,
                   main_parts_def, int_to_char_def, fifo):
    k_update(left_operator, third_def, neighbours_def, vector, first_def)
    k_iterate(left_operator, fifth_def, neighbours_def, vector, forth_def)
    update_neighbours(neighbours_second, first_def, main_parts_def, int_to_char_def, third_def, forth_def, fifth_def,
                      fifo)


def get_min(vector):
    index = -1
    min_value_def = 10000000
    for index_def in range(len(vector)):
        if vector[index_def] < min_value_def:
            min_value_def = vector[index_def]
            index = index_def
    return index


def k_iterate(left_operator, fifth_def, neighbours_def, vector, forth_def):
    if left_operator != fifth_def:
        neighbours_def[vector][forth_def] += 1
        neighbours_def[forth_def][vector] += 1


def check_results(sixth_def, neighbours_sixth, to_get_max, neighbours_second, neighbours_def):
    if sixth_def > len(neighbours_second) - 1 or to_get_max > len(neighbours_second) - 1:
        neighbours_second.extend([[] for _ in range(max([sixth_def, to_get_max]) - len(neighbours_second) + 1)])
        Structures.create_matrix_to_analyse(len(neighbours_second), Structures.not_to_change(neighbours_second))
        neighbours_sixth.extend([[] for _ in range(max([sixth_def, to_get_max]) - len(neighbours_sixth) + 1)])
        neighbours_def.extend([dict() for _ in range(max([sixth_def, to_get_max]) - len(neighbours_def) + 1)])
    apply_changes(neighbours_second, sixth_def, to_get_max, neighbours_def, neighbours_sixth)


def get_iteration_lists(neighbours_second):
    return [[1000000, 1000000, 1000000, 1000000] for _ in range(len(neighbours_second))], [[(-1, -1) for _ in range(4)]
                                                                                           for __ in range(
            len(neighbours_second))], [0 for _ in range(len(neighbours_second))]


def apply_changes(neighbours_second, left_operator, second_def, neighbours_def, neighbours_sixth):
    neighbours_second[left_operator].append(second_def)
    neighbours_sixth[second_def].append(left_operator)
    Structures.create_matrix_to_analyse(len(neighbours_second), Structures.not_to_change(neighbours_second))
    neighbours_def[left_operator][second_def] = 0
    neighbours_def[second_def][left_operator] = 0
    Structures.create_matrix_to_analyse(len(neighbours_sixth), Structures.not_to_change(neighbours_sixth))


def analyse_input(second_to_last_lines, main_parts, neighbours_sixth, neighbours_second, neighbours, first_line):
    to_update_if_st = 0
    for line in second_to_last_lines:
        line = line.split('->')
        left_part = int(line[0])
        if line[1].isdigit():
            right_part = int(line[1])
        else:
            right_part = to_update_if_st
            main_parts[right_part] = line[1]
            to_update_if_st += 1
        check_results(left_part, neighbours_sixth, right_part, neighbours_second, neighbours)
    main_parts.extend(['' for _ in range(len(neighbours_second) - first_line)])


def check_mapped(mapping, neighbours_second, index_def, update_list):
    for four in range(4):
        first = [mapping[neighbours_second[index_def][0]][i_def] + (0 if four == i_def else 1) for i_def in range(4)]
        second = [mapping[neighbours_second[index_def][1]][i_def] + (0 if four == i_def else 1) for i_def in range(4)]
        update_list[index_def][four] = (get_min(first), get_min(second))
        mapping[index_def][four] = first[get_min(first)] + second[get_min(second)]


def init_step(first_line, mapping, char_to_int_def, main_parts, which_part, flags, neighbours_sixth, checking):
    for i_def in range(first_line):
        mapping[i_def][char_to_int_def[main_parts[i_def][which_part]]] = 0
        flags[i_def] = 1
        if len(neighbours_sixth[i_def]) > 0:
            checking.append(neighbours_sixth[i_def][0])


number, rest_of_lines = read_from_file()
neighbours1, neighbours2, neighbours_main, parts = get_empty_result(number)
analyse_input(rest_of_lines, parts, neighbours2, neighbours1, neighbours_main, number)
result_counter = 0
for i in range(len(parts[0])):
    second_neighbours, update_phase, updated_phase = get_iteration_lists(neighbours1)
    to_check = list()
    init_step(number, second_neighbours, char_to_int, parts, i, updated_phase, neighbours2, to_check)
    last_value = None
    while len(to_check) > 0:
        last_value = to_check[-1]
        to_check = to_check[:-1]
        Structures.create_matrix_to_analyse(number, Structures.not_to_change(rest_of_lines))
        check_mapped(second_neighbours, neighbours1, last_value, update_phase)
        updated_phase[last_value] = 1
        if len(neighbours2[last_value]) > 0 and all(
                [updated_phase[u] for u in neighbours1[neighbours2[last_value][0]]]):
            to_check.append(neighbours2[last_value][0])
    min_value = get_min(second_neighbours[last_value])
    parts[last_value] += int_to_char[min_value]
    first_min = second_neighbours[last_value][min_value]
    first_in_first_out = [(last_value, min_value)]
    while len(first_in_first_out) != 0:
        last_value, k = first_in_first_out[0]
        first_in_first_out = first_in_first_out[1:]
        if len(neighbours1[last_value]) > 0:
            update_results(k, update_phase[last_value][k][0], neighbours_main, last_value, neighbours1[last_value][0],
                           update_phase[last_value][k][1], neighbours1[last_value][1], neighbours1, parts, int_to_char,
                           first_in_first_out)
    result_counter += first_min
print_result(neighbours_main, result_counter)