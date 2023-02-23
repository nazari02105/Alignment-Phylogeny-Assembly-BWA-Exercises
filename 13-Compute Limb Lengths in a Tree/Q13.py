file1 = open('Q2.txt', 'r')
main_list = []
while True:
    line = file1.readline()
    if not line:
        break
    content = line.strip()
    main_list.append(content)
n = int(main_list[0])
j = int(main_list[1])
main_list = main_list[2:]
distance = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for i2 in range(n):
        distance[i][i2] = int(main_list[i].split()[i2])
result = float('inf')
i = j - 1 if j > 0 else j + 1
for k in range(n):
    if i != k and k != j:
        now = (distance[i][j] + distance[j][k] - distance[i][k]) // 2
        if now < result:
            result = now
print(result)