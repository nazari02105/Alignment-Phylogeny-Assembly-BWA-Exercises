import copy

all_chars = input().split()
number = int(input())
temp_list = list()
all_kinds = copy.deepcopy(all_chars)
for i in range(number - 1):
    temp_list = copy.deepcopy(all_kinds)
    all_kinds = copy.deepcopy([])
    for j in temp_list:
        for k in all_chars:
            this_time = str(j) + str(k)
            all_kinds.append(this_time)
all_kinds = sorted(all_kinds)
for i in all_kinds:
    print(i)