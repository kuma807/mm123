import sys

class Jewels():
    def __init__(self, N, C):
        self.cnt = 0
        self.N = N
        self.C = C
        self.grid = [[0 for i in range(N)] for j in range(N)]
        self.want_grid = [[-1 for i in range(N)] for j in range(N)]
        self.stater_index = []
        self.holder_index = []
        temp = [[1, 1, 0, 0, 1, 0, 0, 1, 1], [2, 2, 1, 1, 0, 1, 1, 2, 2], [3, 3, 2, 2, 0, 2, 2, 3, 3], [-1, -1, 3, 3, 1, 3, 3, -1, -1], [-1, -1, -1, -1, 2, -1, -1, -1, -1], [-1, -1, -1, -1, 3, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, 7, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
        if N == 8:
            self.want_grid = [[1, 1, 0, 0, 1, 0, 1, 1], [2, 2, 1, 1, 0, 1, 2, 2], [3, 3, 2, 2, 0, 2, 3, 3], [4, 4, 3, 3, 1, 3, 0, -1], [6, 6, 4, 5, 2, -1, -1, -1], [-1, -1, 5, 7, 3, -1, -1, -1], [-1, -1, 6, -1, 5, -1, -1, -1], [-1, -1, 7, -1, 7, -1, -1, -1]]
            self.stater_index = [0, 4]
            self.holder_index = [3, 6]
        elif N == 9:
            self.want_grid = [[1, 1, 0, 0, 1, 0, 0, 1, 1], [2, 2, 1, 1, 0, 1, 1, 2, 2], [3, 3, 2, 2, 0, 2, 2, 3, 3], [4, 4, 3, 3, 1, 3, 3, 0, -1], [6, 6, 4, 5, 2, 4, -1, -1, -1], [8, 8, 5, 7, 3, 5, -1, -1, -1], [-1, -1, 6, -1, 5, -1, -1, -1, -1], [-1, -1, 7, -1, 7, -1, -1, -1, -1], [-1, -1, 8, -1, -1, -1, -1, -1, -1]]
            self.stater_index = [0, 4]
            self.holder_index = [3, 7]
            # print(self.want_grid)
        else:
            for i in range(len(temp)):
                for j in range(len(temp[i])):
                    self.want_grid[i][j] = temp[i][j]
            hight = [N for _ in range(N)]
            for w in range(N):
                for h in range(N):
                    if self.want_grid[h][w] == -1:
                      hight[w] = h
                      break
            cnt = 4
            for i in range((N - 9) // 2):
                for j in range(9):
                    self.want_grid[hight[j]][j] = cnt % C
                    hight[j] += 1
                cnt += 1
            while True:
                if hight[2] == N:
                    break
                for i in range(0, 3):
                    self.want_grid[hight[i]][i] = cnt % C
                    hight[i] += 1
                cnt += 1
                if hight[2] == N:
                    break
                for i in range(2, 5):
                    self.want_grid[hight[i]][i] = cnt % C
                    hight[i] += 1
                self.want_grid[hight[5]][5] = (cnt + C - 1) % C
                hight[5] += 1
                cnt += 1
            self.want_grid[0][9] = 0
            self.stater_index = [0, 4]
            self.holder_index = [0, 9]
            # print(self.want_grid)

    def swap(self, h1, w1, h2, w2):
        self.grid[h1][w1], self.grid[h2][w2] = self.grid[h2][w2], self.grid[h1][w1]
        print(str(h1)+" "+str(w1)+" "+str(h2)+" "+str(w2))
        sys.stdout.flush()

    def update(self):
        place_del = [[False for i in range(self.N)] for j in range(self.N)]
        for i in range(self.N):
            cnt = 0
            before = self.grid[i][0]
            for j in range(self.N):
                if self.grid[i][j] == before and self.grid[i][j] != -1:
                    cnt += 1
                else:
                    if cnt >= 3:
                        for k in range(cnt):
                            place_del[i][j - k - 1] = True
                    cnt = 1
                    before = self.grid[i][j]
            if cnt >= 3:
                for k in range(cnt):
                    place_del[i][j - k - 1] = True
        for i in range(self.N):
            cnt = 0
            before = self.grid[0][i]
            for j in range(self.N):
                if self.grid[j][i] == before and self.grid[i][j] != -1:
                    cnt += 1
                else:
                    if cnt >= 3:
                        for k in range(cnt):
                            place_del[j - k - 1][i] = True
                    cnt = 1
                    before = self.grid[j][i]
            if cnt >= 3:
                for k in range(cnt):
                    place_del[j - k - 1][i] = True
        new_grid = [[-1 for i in range(self.N)] for j in range(self.N)]
        for w in range(self.N):
            index = 0
            for h in range(self.N):
                if place_del[h][w]:
                    continue
                new_grid[index][w] = self.grid[h][w]
                index += 1
        self.grid = new_grid

    def get_input(self):
        for i in range(self.N):
            for j in range(self.N):
                self.grid[i][j] = int(input()) - 1

    def make_want(self):
        index = [[] for _ in range(self.C)]
        for i in range(self.N):
            for j in range(self.N):
                if self.want_grid[i][j] != -1 and self.grid[i][j] == (self.want_grid[i][j] % self.C):
                    continue
                index[self.grid[i][j]].append([i, j])
        found = False
        done = True
        for h in range(self.N):
            for w in range(self.N):
                if (self.want_grid[h][w] != -1 and self.grid[h][w] == (self.want_grid[h][w] % self.C)) or self.want_grid[h][w] == -1:
                    continue
                done = False
                want_c = self.want_grid[h][w] % self.C
                for pos_index in index[want_c]:
                    pos_h, pos_w = pos_index
                    if (self.want_grid[pos_h][pos_w] != -1 and self.grid[pos_h][pos_w] != (self.want_grid[pos_h][pos_w] % self.C)) or self.want_grid[pos_h][pos_w] == -1:
                        self.swap(pos_h, pos_w, h, w)
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if not found and not done:
            self.gridy()
        if not found and done:
            self.swap(self.stater_index[0], self.stater_index[1], self.holder_index[0], self.holder_index[1])

    def gridy(self):
        index = [[] for _ in range(self.C)]
        for i in range(self.N):
            for j in range(self.N):
                if self.want_grid[i][j] != -1 and self.grid[i][j] == self.want_grid[i][j] % self.C:
                    continue
                index[self.grid[i][j]].append([i, j])
        found = False
        #wlen3
        if not found:
            for h in range(self.N):
                for w in range(self.N - 2):
                    interfer = False
                    for i in range(3):
                        if self.want_grid[h][w + i] != -1 and self.grid[h][w + i] == self.want_grid[h][w + i] % self.C:
                            interfer = True
                    if interfer:
                        continue
                    if self.grid[h][w + 2] == self.grid[h][w + 1] and len(index[self.grid[h][w + 2]]) >= 3:
                        want_c = self.grid[h][w + 2]
                        used = [[h, w], [h, w + 1], [h, w + 2]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and self.grid[h][w] == self.grid[h][w + 1] and len(index[self.grid[h][w]]) >= 3:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h, w + 1], [h, w + 2]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w + 2, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and self.grid[h][w] == self.grid[h][w + 2] and len(index[self.grid[h][w]]) >= 3:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h, w + 1], [h, w + 2]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w + 1, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break
        #hlen3
        if not found:
            for h in range(self.N - 2):
                for w in range(self.N):
                    # print(h, w)
                    interfer = False
                    for i in range(3):
                        if self.want_grid[h + i][w] != -1 and self.grid[h + i][w] == self.want_grid[h + i][w] % self.C:
                            interfer = True
                    if interfer:
                        continue
                    if self.grid[h][w] == self.grid[h + 1][w] and len(index[self.grid[h][w]]) >= 3:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h + 1, w], [h + 2, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h + 2, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and self.grid[h][w] == self.grid[h + 2][w] and len(index[self.grid[h][w]]) >= 3:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h + 1, w], [h + 2, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h + 1, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break
        #wmake3
        if not found:
            for h in range(self.N):
                for w in range(self.N - 1):
                    interfer = True
                    third_pos = [-1, 2]
                    for i in third_pos:
                        if w + i >= 0 and w + i < self.N and ((self.want_grid[h][w + i] != -1 and self.grid[h][w + i] != self.want_grid[h][w + i] % self.C) or self.want_grid[h][w + i] == -1):
                            interfer = False
                    for i in range(2):
                        if self.want_grid[h][w + i] != -1 and self.grid[h][w + i] == self.want_grid[h][w + i] % self.C:
                            interfer = True
                    if interfer:
                        continue
                    used = [[h, w], [h, w + 1]]
                    if len(index[self.grid[h][w]]) >= 3 and self.grid[h][w] != self.grid[h][w + 1]:
                        for pos_index in index[self.grid[h][w]]:
                            if pos_index not in used:
                                self.swap(h, w + 1, pos_index[0], pos_index[1])
                                found = True
                                # print(h, w + 1, pos_index[0], pos_index[1], 'hi')
                                break
                    if not found and len(index[self.grid[h][w + 1]]) >= 3 and self.grid[h][w] != self.grid[h][w + 1]:
                        for pos_index in index[self.grid[h][w + 1]]:
                            if pos_index not in used:
                                # self.cnt += 1
                                # if self.cnt >= 200:
                                #     print('hi')
                                self.swap(h, w, pos_index[0], pos_index[1])
                                found = True
                                # print(h, w + 1, pos_index[0], pos_index[1], 'hi')
                                break
                    if found:
                        break
                if found:
                    break
        #hmake3
        if not found:
            for h in range(self.N - 1):
                for w in range(self.N):
                    interfer = False
                    for i in range(2):
                        if self.want_grid[h + i][w] != -1 and self.grid[h + i][w] == self.want_grid[h + i][w] % self.C:
                            interfer = True
                    if interfer:
                        continue
                    used = [[h, w], [h + 1, w]]
                    if len(index[self.grid[h][w]]) >= 3:
                        for pos_index in index[self.grid[h][w]]:
                            if pos_index not in used:
                                self.swap(h + 1, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break

N = int(input())
C = int(input())
jew = Jewels(N, C)
jew.get_input()

for i in range(1000):
    r1 = 0
    c1 = i%N
    r2 = 1+(i%(N-1))
    c2 = c1
    # jew.swap(r1, c1, r2, c2)
    # jew.update()
    jew.make_want()
    # print('ji')
    jew.get_input()
    runtime = int(input())
