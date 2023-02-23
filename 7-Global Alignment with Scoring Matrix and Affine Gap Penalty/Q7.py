mapping = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12,
           'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
a = 11
b = 1
score_matrix = []
file1 = open('Q3_matrix.txt', 'r')
while True:
    line = file1.readline()
    if not line:
        break
    content = line.strip()
    content = content.split()
    if len(content) == 21:
        content = content[1:]
        to_add = []
        for item in content:
            to_add.append(int(item))
        score_matrix.append(to_add)
file1.close()
is_insertion_or_deletion = list()


class SequenceAlignment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solution = []

    def find_solution(self, OPT, m, n):
        global is_insertion_or_deletion
        if m == 0 and n == 0:
            return
        # insert
        if n == 0:
            insert = float("inf")
        elif is_insertion_or_deletion[m][n - 1]:
            insert = OPT[m][n - 1] + b
        else:
            insert = OPT[m][n - 1] + a
        # align
        if m == 0 or n == 0:
            align = float("inf")
        else:
            align = OPT[m - 1][n - 1] + (-1 * score_matrix[mapping[self.x[m - 1]]][mapping[self.y[n - 1]]])
        # delete
        if m == 0:
            delete = float("inf")
        elif is_insertion_or_deletion[m - 1][n]:
            delete = OPT[m - 1][n] + b
        else:
            delete = OPT[m - 1][n] + a

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
        global is_insertion_or_deletion
        OPT = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]
        is_insertion_or_deletion = [[False for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]
        for i_def in range(1, len(self.x) + 1):
            OPT[i_def][0] = a + (i_def - 1) * b
            is_insertion_or_deletion[i_def][0] = True
        for j in range(1, len(self.y) + 1):
            OPT[0][j] = a + (j - 1) * b
            is_insertion_or_deletion[0][j] = True
        for i in range(1, len(self.x) + 1):
            for j in range(1, len(self.y) + 1):
                the_insert = OPT[i][j - 1] + b if is_insertion_or_deletion[i][j - 1] else OPT[i][j - 1] + a
                the_delete = OPT[i - 1][j] + b if is_insertion_or_deletion[i - 1][j] else OPT[i - 1][j] + a
                the_align = OPT[i - 1][j - 1] + (-1 * score_matrix[mapping[self.x[i - 1]]][mapping[self.y[j - 1]]])
                OPT[i][j] = min(the_align, the_delete, the_insert)
                if OPT[i][j] == the_align:
                    pass
                elif OPT[i][j] == the_insert or OPT[i][j] == the_delete:
                    is_insertion_or_deletion[i][j] = True
        self.find_solution(OPT, len(self.x), len(self.y))
        return OPT[len(self.x)][len(self.y)], self.solution[::-1]


if __name__ == '__main__':
    file1 = open('Q3.txt', 'r')
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

    print(-1 * min_edit + 2)

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