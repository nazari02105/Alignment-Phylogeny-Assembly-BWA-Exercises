file1 = open('rosalind_gc.txt', 'r')
count = 0

max_name = ""
max_number = -1
now_total = 1
now_gc = 0
now_name = ""

while True:
    count += 1
    line = file1.readline()
    if not line:
        break
    main_content = line.strip()
    if main_content.startswith(">"):
        percentage = now_gc / now_total
        now_gc = 0
        now_total = 0
        if percentage > max_number:
            max_number = percentage
            max_name = now_name
        now_name = main_content[1:]
    else:
        for i in main_content:
            if i is 'G' or i is 'C':
                now_gc += 1
            now_total += 1

percentage = now_gc / now_total
if percentage > max_number:
    max_number = percentage
    max_name = now_name

print(max_name)
print("{:.6f}".format(max_number * 100));

file1.close()