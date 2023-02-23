import copy

file1 = open('Q6.txt', 'r')
main_list = list()
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
file1.close()
BWT = main_list[0]
patterns = main_list[1].strip().split()
main_length = len(BWT)
last_col = list()
for i in BWT:
    last_col.append(i)
first_col = copy.deepcopy(last_col)
first_col.sort()
main_result = list()
for i in range(len(first_col)):
    main_result.append(str(last_col[i]) + str(first_col[i]))
while len(main_result[0]) < main_length:
    main_result.sort()
    for i in range(len(main_result)):
        main_result[i] = str(last_col[i]) + main_result[i]
main_result.sort()
start_point = {"$": -1, "A": -1, "C": -1, "G": -1, "T": -1}
counter = 0
for i in main_result:
    first_char = i[0]
    if start_point[str(first_char)] == -1:
        start_point[str(first_char)] = counter
    counter += 1
end_point = {"$": 0, "A": start_point["C"]-1, "C": start_point["G"]-1, "G": start_point["T"]-1, "T": len(BWT)-1}
last_col_pre_process = {}
counter = 0
for i in main_result:
    last_char = i[-1]
    if counter == 0:
        last_col_pre_process[counter] = {"$": 0, "A": 0, "C": 0, "G": 0, "T": 0}
    else:
        last_col_pre_process[counter] = copy.deepcopy(last_col_pre_process[counter-1])
    last_col_pre_process[counter][str(last_char)] += 1
    counter += 1
the_result = []
for pattern in patterns:
    start_index = 0
    end_index = len(BWT) - 1
    rev_pattern = pattern[::-1]
    flag = True
    for i, character in enumerate(rev_pattern):
        if i == 0:
            start_index = start_point[str(character)]
            end_index = end_point[str(character)]
        else:
            in_the_range = last_col_pre_process[end_index][str(character)] - last_col_pre_process[start_index-1][str(character)]
            before_range = last_col_pre_process[start_index-1][str(character)]
            start_index = start_point[str(character)] + before_range
            end_index = start_index + in_the_range - 1
        if end_index < start_index:
            the_result.append(0)
            flag = False
            break
    if flag:
        the_result.append(end_index - start_index + 1)
res = " ".join([str(item) for item in the_result])
print(res)