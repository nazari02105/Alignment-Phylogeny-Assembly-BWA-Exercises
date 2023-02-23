main_dict = {"A": 4, "R": 6, "D": 2, "N": 2, "C": 2, "E": 2, "Q": 2, "G": 4, "H": 2, "I": 3, "L": 6, "K": 2, "M": 1,
             "F": 2, "P": 4, "S": 6, "T": 4, "W": 1, "Y": 2, "V": 4}

file1 = open('Q11.txt', 'r')
content = ""
while True:
    line = file1.readline()
    if not line:
        break
    content += line.strip()
file1.close()

counter = 1
for i in content:
    counter *= main_dict[i]
    counter %= 1000000
counter *= 3
counter %= 1000000
print(counter)