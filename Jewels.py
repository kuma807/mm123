import sys

class Jewels():
    def __init__(self, N, C):
        self.N = N
        self.C = C
        self.grid = [[0 for i in range(N)] for j in range(N)]

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

    def gridy(self):
        index = [[] for _ in range(self.C)]
        for i in range(self.N):
            for j in range(self.N):
                index[self.grid[i][j]].append([i, j])
        found = False
        # print(index)
        #wlen5
        if not found:
            for h in range(self.N):
                for w in range(self.N - 4):
                    if len(index[self.grid[h][w]]) >= 5 and self.grid[h][w] == self.grid[h][w + 1] and self.grid[h][w] == self.grid[h][w + 3] and self.grid[h][w] == self.grid[h][w + 4]:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h, w + 1], [h, w + 2], [h, w + 3], [h, w + 4]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w + 2, pos_index[0], pos_index[1])
                                found = True
                                break
                        if found:
                            break
                if found:
                    break
        #hlen5
        if not found:
            for h in range(self.N - 4):
                for w in range(self.N):
                    if len(index[self.grid[h][w]]) >= 5 and self.grid[h][w] == self.grid[h + 1][w] and self.grid[h][w] == self.grid[h + 3][w] and self.grid[h][w] == self.grid[h + 4][w]:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h + 1, w], [h + 2, w], [h + 3, w], [h + 4, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h + 2, w, pos_index[0], pos_index[1])
                                found = True
                                break
                        if found:
                            break
                if found:
                    break
        #wmake5
        if not found:
            for h in range(self.N):
                for w in range(self.N - 4):
                    # print(h, w)
                    if (self.grid[h][w] == self.grid[h][w + 1] and self.grid[h][w] == self.grid[h][w + 3]) and len(index[self.grid[h][w]]) >= 5:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h, w + 1], [h, w + 3], h, w + 4]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w + 4, pos_index[0], pos_index[1])
                                found = True
                                break
                    elif (self.grid[h][w] == self.grid[h][w + 2] and self.grid[h][w] == self.grid[h][w + 3]) and len(index[self.grid[h][w]]) >= 5 and w - 1 >= 0:
                        want_c = self.grid[h][w]
                        used = [[h, w - 1], [h, w], [h, w + 2], [h, w + 3]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w - 1, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break
        #hmake5
        if not found:
            for h in range(self.N - 4):
                for w in range(self.N):
                    # print(h, w)
                    if (self.grid[h][w] == self.grid[h + 1][w] and self.grid[h][w] == self.grid[h + 3][w]) and len(index[self.grid[h][w]]) >= 5:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h + 1, w], [h + 3, w], h + 4, w]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h + 4, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    elif (self.grid[h][w] == self.grid[h + 2][w] and self.grid[h][w] == self.grid[h + 3][w]) and len(index[self.grid[h][w]]) >= 5 and h - 1 >= 0:
                        want_c = self.grid[h][w]
                        used = [[h - 1, w], [h, w], [h + 2, w], [h + 3, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h - 1, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break
        #wlen4
        # if not found:
        #     for h in range(self.N):
        #         for w in range(self.N - 3):
        #             # print(h, w)
        #             if (self.grid[h][w] == self.grid[h][w + 1] and self.grid[h][w] == self.grid[h][w + 3]) and len(index[self.grid[h][w]]) >= 4:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h, w + 1], [h, w + 3]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h, w + 2, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             elif (self.grid[h][w] == self.grid[h][w + 2] and self.grid[h][w] == self.grid[h][w + 3]) and len(index[self.grid[h][w]]) >= 4:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h, w + 2], [h, w + 3]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h, w + 1, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             if found:
        #                 break
        #         if found:
        #             break
        #hlen4
        # if not found:
        #     for h in range(self.N - 3):
        #         for w in range(self.N):
        #             # print(h, w)
        #             if (self.grid[h][w] == self.grid[h + 1][w] and self.grid[h][w] == self.grid[h + 3][w]) and len(index[self.grid[h][w]]) >= 4:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h + 1, w], [h + 3, w]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h + 2, w, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             elif (self.grid[h][w] == self.grid[h + 2][w] and self.grid[h][w] == self.grid[h + 3][w]) and len(index[self.grid[h][w]]) >= 4:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h + 2, w], [h + 3, w]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h + 1, w, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             if found:
        #                 break
        #         if found:
        #             break
        #wmake4
        if not found:
            for h in range(self.N):
                for w in range(self.N - 2):
                    if w - 1 >= 0 and self.grid[h][w + 2] == self.grid[h][w + 1] and len(index[self.grid[h][w + 2]]) >= 5 and self.grid[h][w - 1] != self.grid[h][w + 2]:
                        want_c = self.grid[h][w + 2]
                        used = [[h, w - 1], [h, w + 1], [h, w + 2]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w - 1, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and w + 3 < self.N and self.grid[h][w] == self.grid[h][w + 1] and len(index[self.grid[h][w]]) >= 5 and self.grid[h][w + 3] != self.grid[h][w]:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h, w + 1], [h, w + 3]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h, w + 3, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and self.grid[h][w] == self.grid[h][w + 2] and len(index[self.grid[h][w]]) >= 5:
                        want_c = self.grid[h][w]
                        dw = 0
                        if w - 1 >= 0:
                            dw = -1
                        if w + 3 < self.N:
                            dw = 3
                        used = [[h, w], [h, w + 2], [h, w + dw]]
                        for pos_index in index[want_c]:
                            if pos_index not in used and self.grid[h][w] != self.grid[h][w + dw]:
                                self.swap(h, w + dw, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break
        #hmake4
        if not found:
            for h in range(self.N - 2):
                for w in range(self.N):
                    if h - 1 >= 0 and self.grid[h + 2][w] == self.grid[h + 1][w] and len(index[self.grid[h + 2][w]]) >= 5 and self.grid[h + 1][w] != self.grid[h - 1][w]:
                        want_c = self.grid[h + 2][w]
                        used = [[h - 1, w], [h + 1, w], [h + 2, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h - 1, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and h + 3 < self.N and self.grid[h][w] == self.grid[h + 1][w] and len(index[self.grid[h][w]]) >= 5 and self.grid[h][w] != self.grid[h + 3][w]:
                        want_c = self.grid[h][w]
                        used = [[h, w], [h + 1, w], [h + 3, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used:
                                self.swap(h + 3, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if not found and self.grid[h][w] == self.grid[h + 2][w] and len(index[self.grid[h][w]]) >= 5:
                        want_c = self.grid[h][w]
                        dh = 0
                        if h - 1 >= 0:
                            dh = -1
                        if h + 3 < self.N:
                            dh = 3
                        used = [[h, w], [h + 2, w], [h + dh, w]]
                        for pos_index in index[want_c]:
                            if pos_index not in used and self.grid[h][w] != self.grid[h + dh][w]:
                                self.swap(h + dh, w, pos_index[0], pos_index[1])
                                found = True
                                break
                    if found:
                        break
                if found:
                    break
        #wlen3
        # if not found:
        #     for h in range(self.N):
        #         for w in range(self.N - 2):
        #             # print(h, w)
        #             if self.grid[h][w + 2] == self.grid[h][w + 1] and len(index[self.grid[h][w + 2]]) >= 3:
        #                 want_c = self.grid[h][w + 2]
        #                 used = [[h, w + 2], [h, w + 1]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h, w, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             elif self.grid[h][w] == self.grid[h][w + 1] and len(index[self.grid[h][w]]) >= 3:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h, w + 1]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h, w + 2, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             elif self.grid[h][w] == self.grid[h][w + 2] and len(index[self.grid[h][w]]) >= 3:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h, w + 2]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h, w + 1, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             if found:
        #                 break
        #         if found:
        #             break
        #hlen3
        # if not found:
        #     for h in range(self.N - 2):
        #         for w in range(self.N):
        #             # print(h, w)
        #             if self.grid[h][w] == self.grid[h + 1][w] and len(index[self.grid[h][w]]) >= 3:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h + 1, w]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h + 2, w, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             elif self.grid[h][w] == self.grid[h + 2][w] and len(index[self.grid[h][w]]) >= 3:
        #                 want_c = self.grid[h][w]
        #                 used = [[h, w], [h + 2, w]]
        #                 for pos_index in index[want_c]:
        #                     if pos_index not in used:
        #                         self.swap(h, w + 1, pos_index[0], pos_index[1])
        #                         found = True
        #                         break
        #             if found:
        #                 break
        #         if found:
        #             break
        #len0
        if not found:
            for h in range(self.N // 2):
                for w in range(self.N - 1):
                    now = [h, w]
                    if len(index[self.grid[h][w]]) >= 3:
                        for pos_index in index[self.grid[h][w]]:
                            if pos_index != now:
                                self.swap(h, w + 1, pos_index[0], pos_index[1])
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
  jew.gridy()
  # print('ji')
  jew.get_input()
  runtime = int(input())
