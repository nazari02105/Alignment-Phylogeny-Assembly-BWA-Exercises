complement = {"A": "T", "T": "A", "G": "C", "C": "G"}

file1 = open('Q12.txt', 'r')
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

main_dict = dict()
for seq in main_list:
    main_seq = seq
    reverse_complement = ""
    for letter in main_seq[::-1]:
        reverse_complement += str(complement[str(letter)])
    if main_seq in main_dict.keys():
        main_dict[main_seq] = main_dict[main_seq] + 1
    elif reverse_complement in main_dict.keys():
        main_dict[reverse_complement] = main_dict[reverse_complement] + 1
    else:
        main_dict[main_seq] = 1

all_list = list()
one_list = list()
for seq in main_dict.keys():
    if main_dict[seq] == 1:
        one_list.append(seq)
    else:
        all_list.append(seq)

for one_seq in one_list:
    for all_seq in all_list:
        if one_seq != all_seq:
            first = one_seq
            second = all_seq
            second_reverse_complement = ""
            for letter in second[::-1]:
                second_reverse_complement += str(complement[str(letter)])
            counter = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    counter += 1
            if counter == 1:
                print(first + "->" + second)
                break
            counter = 0
            for i in range(len(first)):
                if first[i] != second_reverse_complement[i]:
                    counter += 1
            if counter == 1:
                print(first + "->" + second_reverse_complement)
                break