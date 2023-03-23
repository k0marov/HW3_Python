n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))


def is_symmetric(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != a[j][i]:
                return False
    return True


print("YES" if is_symmetric(a) else "NO")
