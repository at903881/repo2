def view(flats, i, dir):
    res = True
    for idx in range(len(flats)):
        if idx == i: continue
        if dir == "down" and flats[idx][0] == flats[i][0] and flats[idx][1] < flats[i][1] and flats[idx][2] >= flats[i][
            2]:
            res = False
            return res
        if dir == "up" and flats[idx][0] == flats[i][0] and flats[idx][1] > flats[i][1] and flats[idx][2] >= flats[i][
            2]:
            res = False
            return res
        if dir == "right" and flats[idx][0] > flats[i][0] and flats[idx][1] == flats[i][1] and flats[idx][2] >= \
                flats[i][2]:
            res = False
            return res
        if dir == "left" and flats[idx][0] < flats[i][0] and flats[idx][1] == flats[i][1] and flats[idx][2] >= flats[i][
            2]:
            res = False
            return res
    return res


a = list(map(int, input().split()))
dl = [a[0], a[1]]
tl = [a[2], a[3]]
tr = [a[4], a[5]]
dr = [a[6], a[7]]

n, charge = map(int, input().split())
extra = charge * 2

ans = 0

flats = []
for _ in range(n):
    flats.append(list(map(int, input().split())))

for i in range(n):
    #      f x
    if dl[0] <= flats[i][0] <= dr[0]:
        if flats[i][1] > tl[1]:
            if view(flats, i, "down"):
                ans += extra
            elif view(flats, i, "up"):
                ans += extra

    elif dl[1] <= flats[i][1] <= tl[1]:
        if flats[i][0] > tr[0]:
            if view(flats, i, "left"):
                ans += extra
            elif view(flats, i, "right"):
                ans += extra
    else:
        ans+=charge
    print(ans, flats[i])

print(ans)

# 1 1 1 3 1 3 1 1
# 4 1
# 0 1 2
# 0 3 3
# 2 0 2
# 3 2 1
