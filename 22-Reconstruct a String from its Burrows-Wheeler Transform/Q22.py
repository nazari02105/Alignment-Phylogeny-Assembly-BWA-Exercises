import copy

file1 = open('Q5.txt', 'r')
main_list = list()
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
file1.close()
BWT = main_list[0]
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
for i in main_result:
    if i[-1] == '$':
        print(i)
        break