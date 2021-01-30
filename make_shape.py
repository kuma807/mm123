vec = []
with open("temp.txt") as f:
    s = f.readlines()
    # print(s)
    for i in range(len(s)):
        v = []
        s[i] = s[i].replace("\n", "")
        for j in range(len(s[i])):
            now = int(s[i][j])
            if now == 9:
                now = -1
            v.append(now)
        vec.append(v)

print(vec)
