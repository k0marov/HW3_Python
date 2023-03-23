a = list(map(int, input().split()))

equal_pair_cnt = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            equal_pair_cnt += 1

print(equal_pair_cnt)
