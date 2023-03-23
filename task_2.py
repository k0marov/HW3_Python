n = int(input())

seq = [0]
while len(seq) < n:
    seq += [1-e for e in seq]

print(*seq[:n], sep='')
