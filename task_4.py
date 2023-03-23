n = int(input())
PORRIDGES = ["Манная", "Гречневая",
             "Пшённая", "Овсяная",
             "Рисовая",]

for day in range(n):
    i = day % len(PORRIDGES)
    print(PORRIDGES[i])
