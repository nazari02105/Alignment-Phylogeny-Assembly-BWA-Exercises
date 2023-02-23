mapping = {'A': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 12, 'Q': 13, 'R': 14, 'S': 15, 'T': 16, 'V': 17, 'W': 18, 'Y': 19}
score_matrix = []
file1 = open('Q4_matrix.txt', 'r')
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
to_break_list = list()
i_end = 0
j_end = 0
i_start = 0
j_start = 0


class SequenceAlignment(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solution = []

    def find_solution(self, OPT, m, n):
        global to_break_list, i_start, j_start
        if (m == 0 and n == 0) or to_break_list[m][n]:
            i_start = m
            j_start = n
            return
        insert = OPT[m][n - 1] + 5 if n != 0 else float("inf")
        align = OPT[m - 1][n - 1] + (-1 * score_matrix[mapping[self.x[m - 1]]][mapping[self.y[n - 1]]]) if m != 0 and n != 0 else float("inf")
        delete = OPT[m - 1][n] + 5 if m != 0 else float("inf")
        best_choice = min(insert, align, delete, 0)
        if best_choice == 0:
            i_start = m
            j_start = n
            return
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
        global i_end, j_end
        global to_break_list
        OPT = [[0 for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]
        to_break_list = [[False for _ in range(len(self.y) + 1)] for _ in range(len(self.x) + 1)]
        for i_def in range(1, len(self.x) + 1):
            to_break_list[i_def][0] = True
        for j in range(1, len(self.y) + 1):
            to_break_list[0][j] = True
        for i in range(1, len(self.x) + 1):
            for j in range(1, len(self.y) + 1):
                insert = OPT[i][j - 1] + 5
                delete = OPT[i - 1][j] + 5
                align = OPT[i - 1][j - 1] + (-1 * score_matrix[mapping[self.x[i-1]]][mapping[self.y[j-1]]])
                OPT[i][j] = min(align, delete, insert, 0)
                if OPT[i][j] == 0:
                    to_break_list[i][j] = True

        i_end = 0
        j_end = 0
        min_score = float("inf")
        for i_def in range(1, len(self.x) + 1):
            for j_def in range(1, len(self.y) + 1):
                if OPT[i_def][j_def] < min_score:
                    min_score = OPT[i_def][j_def]
                    i_end = i_def
                    j_end = j_def
        self.find_solution(OPT, i_end, j_end)
        return min_score


if __name__ == '__main__':
    file1 = open('Q4.txt', 'r')
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
    min_edit = sqalign.alignment()

    print(min_edit * -1)
    print(x[i_start: i_end + 1])
    print(y[j_start: j_end + 1])

    # result = ""
    # counter = 0
    # for i in range(len(steps)):
    #     content = steps[i]
    #     if content.startswith("align") or content.startswith("remove"):
    #         result += str(x[counter])
    #         counter += 1
    #     else:
    #         result += "-"
    # print(result)
    #
    # result = ""
    # counter = 0
    # for i in range(len(steps)):
    #     content = steps[i]
    #     if content.startswith("align") or content.startswith("insert"):
    #         result += str(y[counter])
    #         counter += 1
    #     else:
    #         result += "-"
    # print(result)