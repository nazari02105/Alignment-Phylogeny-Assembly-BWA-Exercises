def get_lens(the_list):
    to_return = 0
    for seq in the_list:
        to_return += len(seq)
    return to_return


def new_main_list(the_list):
    to_return = list()
    for _ in the_list:
        max_index = -1
        max_len = -1
        for i_def, seq in enumerate(the_list):
            if len(seq) > max_len and seq not in to_return:
                max_len = len(seq)
                max_index = i_def
        to_return.append(the_list[max_index])
    return to_return


def result(n50, n75):
    temp = 0
    for i in main_list:
        temp += len(i)
        if n50 == total_len and temp > total_len * 0.5:
            n50 = len(i)
        if temp > total_len * 0.75:
            n75 = len(i)
            break
    return n50, n75


file1 = open('Q4.txt', 'r')
main_list = list()
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
file1.close()
main_list = [*set(main_list)]
main_list = new_main_list(main_list)
total_len = get_lens(main_list)
N50, N75 = result(total_len, total_len)
print(N50, N75)