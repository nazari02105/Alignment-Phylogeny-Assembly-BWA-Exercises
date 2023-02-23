file1 = open('Q1.txt', 'r')
main_list = list()
while True:
    line = file1.readline()
    if not line:
        break
    main_list.append(line.strip())
file1.close()
main_list = [*set(main_list)]
convert_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
reverse_complement_list = list()
for seq in main_list:
    rev_com = ""
    reversed_seq = seq[::-1]
    for character in reversed_seq:
        rev_com += str(convert_dict[character])
    reverse_complement_list.append(rev_com)
main_list += reverse_complement_list
main_list = [*set(main_list)]
for seq in main_list:
    print("(" + str(seq[:len(seq)-1]) + ", " + str(seq[1:]) + ")")