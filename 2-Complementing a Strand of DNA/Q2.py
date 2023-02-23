main_string = input()
reverse_string = ""
counter = len(main_string) - 1
while counter > -1:
    reverse_string += str(main_string[counter])
    counter -= 1
true_string = ""
for i in reverse_string:
    if i == 'A':
        true_string += "T"
    elif i == 'T':
        true_string += "A"
    elif i == 'C':
        true_string += "G"
    else:
        true_string += "C"
print(true_string)