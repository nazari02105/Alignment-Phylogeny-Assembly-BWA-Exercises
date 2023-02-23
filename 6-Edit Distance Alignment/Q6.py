# actually I used
# https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/sequence_alignment.py
# very much
class SequenceAlignment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solution = []

    def find_solution(self, OPT, m, n):
        if m == 0 and n == 0:
            return
        insert = OPT[m][n - 1] + 1 if n != 0 else float("inf")
        align = OPT[m - 1][n - 1] + 1 if self.x[m - 1] != self.y[n - 1] else OPT[m - 1][n - 1] + 0 if m != 0 and n != 0 else float("inf")
        delete = OPT[m - 1][n] + 1 if m != 0 else float("inf")
        best_choice = min(insert, align, delete)
        if best_choice == insert:
            self.solution.append("insert_" + str(self.y[n - 1]))
            return self.find_solution(OPT, m, n - 1)
        elif best_choice == align:
            self.solution.append("align_" + str(self.y[n - 1]))
            return self.find_solution(OPT, m - 1, n - 1)
        elif best_choice == delete:
            self.solution.append("remove_" + str(self.x[m - 1]))
            return self.find_solution(OPT, m - 1, n)

    def alignment(self):
        OPT = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]
        for i_def in range(1, len(self.x) + 1):
            OPT[i_def][0] = i_def
        for j in range(1, len(self.y) + 1):
            OPT[0][j] = j
        for i in range(1, len(self.x) + 1):
            for j in range(1, len(self.y) + 1):
                OPT[i][j] = min(OPT[i - 1][j - 1] + 1 if self.x[i - 1] != self.y[j - 1] else OPT[i - 1][j - 1] + 0, OPT[i - 1][j] + 1, OPT[i][j - 1] + 1,)
        self.find_solution(OPT, len(self.x), len(self.y))
        return OPT[len(self.x)][len(self.y)], self.solution[::-1]


if __name__ == '__main__':
    file1 = open('Q2.txt', 'r')
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
    x = main_list[0]
    y = main_list[1]

    sqalign = SequenceAlignment(x, y)
    min_edit, steps = sqalign.alignment()

    print(min_edit)

    result = ""
    counter = 0
    for i in range(len(steps)):
        content = steps[i]
        if content.startswith("align") or content.startswith("remove"):
            result += str(x[counter])
            counter += 1
        else:
            result += "-"
    print(result)

    result = ""
    counter = 0
    for i in range(len(steps)):
        content = steps[i]
        if content.startswith("align") or content.startswith("insert"):
            result += str(y[counter])
            counter += 1
        else:
            result += "-"
    print(result)