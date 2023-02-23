file1 = open('rosalind_ba9a.txt', 'r')
trie_counter = 1
current_number = 0
trie_dict = dict()


def temp_func(number, character):
    global trie_dict
    for key in trie_dict.keys():
        if str(key.split("->")[0]) == str(number) and str(trie_dict[key]) == str(character):
            return int(key.split("->")[1])
    return -1


while True:
    line = file1.readline()
    if not line:
        break
    main_content = line.strip()
    current_number = 0
    for i in main_content:
        returned_value = temp_func(current_number, i)
        if returned_value == -1:
            trie_dict[str(current_number) + "->" + str(trie_counter)] = str(i)
            current_number = trie_counter
            trie_counter += 1
        else:
            current_number = returned_value
file1.close()

for key in trie_dict.keys():
    print(key + ":" + trie_dict[key])