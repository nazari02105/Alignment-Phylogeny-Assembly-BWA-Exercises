file1 = open('Q1.txt', 'r')
main_list = list()
to_add = ""
while True:
    line = file1.readline()
    if not line:
        break
    content = line.strip()
    if not content.startswith(">"):
        to_add += content
    else:
        main_list.append(to_add)
        to_add = ""
file1.close()
main_list.append(to_add)
main_list = main_list[1:]

def get_percentage(first_seq, second_seq):
    length = len(first_seq)
    not_equal = 0
    for num in range(length):
        if first_seq[num] != second_seq[num]:
            not_equal += 1
    return not_equal / length


second_list = list()
for i in main_list:
    temp_list = list()
    for j in main_list:
        percentage = get_percentage(i, j)
        temp_list.append(percentage)
    second_list.append(temp_list)

for inner_list in second_list:
    to_print = ""
    for i in inner_list:
        temp = f'{i:.5f}'
        to_print += temp + " "
    to_print = to_print.strip()
    print(to_print)