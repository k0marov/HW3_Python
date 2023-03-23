a = list(map(int, input().split()))
for i in range(len(a)-1):
    a[i], a[-1] = a[-1], a[i]
print(*a)
