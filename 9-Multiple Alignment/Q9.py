import numpy as np
import copy

length1 = 0
length2 = 0
length3 = 0
length4 = 0
score_matrix = None
optimal_moves = None
all_situations = ["0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]


def get_score(c1, c2, c3, c4):
    counter = 0
    if c1 != c2:
        counter -= 1
    if c1 != c3:
        counter -= 1
    if c1 != c4:
        counter -= 1
    if c2 != c3:
        counter -= 1
    if c2 != c4:
        counter -= 1
    if c3 != c4:
        counter -= 1
    return counter


def binary_to_decimal_convertor(number):
    to_return = 0
    counter = len(number) - 1
    position = 0
    while counter >= 0:
        this_time = int(number[counter])
        to_return += this_time * (2 ** position)
        position += 1
        counter -= 1
    return to_return


def get_situation(number, first_def, second_def, third_def, forth_def, s1_def, s2_def, s3_def, s4_def, the_list):
    global score_matrix
    number = binary_to_decimal_convertor(number)
    for index in the_list:
        if index == 1:
            first_def -= 1
        if index == 2:
            second_def -= 1
        if index == 3:
            third_def -= 1
        if index == 4:
            forth_def -= 1
    value = score_matrix[first_def, second_def, third_def, forth_def] + get_score('-' if 1 not in the_list else s1_def[first_def], '-' if 2 not in the_list else s2_def[second_def], '-' if 3 not in the_list else s3_def[third_def], '-' if 4 not in the_list else s4_def[forth_def])
    return value, number


def multiple_alignment(s1_def, s2_def, s3_def, s4_def):
    global length1, length2, length3, length4, score_matrix, optimal_moves, all_situations
    for first in range(length1):
        for second in range(length2):
            for third in range(length3):
                for forth in range(length4):
                    if not first == second == third == forth == 0:
                        # let's start brute force algorithm
                        the_values = []
                        the_optimal_moves = copy.deepcopy(the_values)

                        the_binary_codes = []
                        if forth != 0:
                            the_binary_codes.append("0001")
                        if third != 0:
                            the_binary_codes.append("0010")
                        if third != 0 and forth != 0:
                            the_binary_codes.append("0011")
                        if second != 0:
                            the_binary_codes.append("0100")
                        if second != 0 and forth != 0:
                            the_binary_codes.append("0101")
                        if second != 0 and third != 0:
                            the_binary_codes.append("0110")
                        if second != 0 and third != 0 and forth != 0:
                            the_binary_codes.append("0111")
                        if first != 0:
                            the_binary_codes.append("1000")
                        if first != 0 and forth != 0:
                            the_binary_codes.append("1001")
                        if first != 0 and third != 0:
                            the_binary_codes.append("1010")
                        if first != 0 and third != 0 and forth != 0:
                            the_binary_codes.append("1011")
                        if first != 0 and second != 0:
                            the_binary_codes.append("1100")
                        if first != 0 and second != 0 and forth != 0:
                            the_binary_codes.append("1101")
                        if first != 0 and second != 0 and third != 0:
                            the_binary_codes.append("1110")
                        if first != 0 and second != 0 and third != 0 and forth != 0:
                            the_binary_codes.append("1111")
                        for index in range(len(the_binary_codes)):
                            the_binary_code = the_binary_codes[index]
                            iii_list = []
                            for iii in range(len(the_binary_code)):
                                if the_binary_code[iii] == '1':
                                    iii_list.append(iii + 1)
                            value, optimal_move = get_situation(the_binary_codes[index], first, second, third, forth, s1_def, s2_def, s3_def, s4_def, iii_list)
                            the_values.append(value)
                            the_optimal_moves.append(optimal_move)

                        index_of_max = np.argmax(the_values)
                        score_matrix[first, second, third, forth] = the_values[index_of_max]
                        optimal_moves[first, second, third, forth] = the_optimal_moves[index_of_max]

    seq1 = ''
    seq2 = ''
    seq3 = ''
    seq4 = ''
    first = length1 - 1
    second = length2 - 1
    third = length3 - 1
    forth = length4 - 1
    while True:
        m = int(optimal_moves[first, second, third, forth])
        m_binary = "{0:#b}".format(m)[2:]
        minus_len = 4 - len(m_binary)
        m_binary2 = ""
        for iii in range(minus_len):
            m_binary2 += "0"
        m_binary2 += m_binary
        if m == 0:
            break
        for iii in range(len(m_binary2)):
            if iii == 0 and m_binary2[iii] == '0':
                seq4 += '-'
            if iii == 0 and m_binary2[iii] == '1':
                seq4 += s4_def[forth - 1]
            if iii == 1 and m_binary2[iii] == '0':
                seq3 += '-'
            if iii == 1 and m_binary2[iii] == '1':
                seq3 += s3_def[third - 1]
            if iii == 2 and m_binary2[iii] == '0':
                seq2 += '-'
            if iii == 2 and m_binary2[iii] == '1':
                seq2 += s2_def[second - 1]
            if iii == 3 and m_binary2[iii] == '0':
                seq1 += '-'
            if iii == 3 and m_binary2[iii] == '1':
                seq1 += s1_def[first - 1]
        for iii in range(len(m_binary2)):
            if iii == 0 and m_binary2[iii] == '1':
                first -= 1
            if iii == 1 and m_binary2[iii] == '1':
                second -= 1
            if iii == 2 and m_binary2[iii] == '1':
                third -= 1
            if iii == 3 and m_binary2[iii] == '1':
                forth -= 1

    return score_matrix[length1 - 1, length2 - 1, length3 - 1, length4 - 1], seq1, seq2, seq3, seq4


with open(f'Q10.txt', 'r') as fin:
    main_list = list()
    while True:
        line = fin.readline()
        if not line:
            break
        content = line.strip()
        if not content.startswith(">"):
            main_list.append(content)

    length1 = len(main_list[0]) + 1
    length2 = len(main_list[1]) + 1
    length3 = len(main_list[2]) + 1
    length4 = len(main_list[3]) + 1
    score_matrix = np.zeros((length1, length2, length3, length4))
    optimal_moves = np.zeros((length1, length2, length3, length4))
    ED, s1, s2, s3, s4 = multiple_alignment(main_list[0], main_list[1], main_list[2], main_list[3])
    print(int(ED))
    print(s1)
    print(s2)
    print(s3)
    print(s4)