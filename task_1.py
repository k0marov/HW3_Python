def can_eat(knight, target):
    k_x, k_y = knight
    t_x, t_y = target

    eats_1 = abs(k_x-t_x) == 2 and abs(k_y-t_y) == 1
    eats_2 = abs(k_x-t_x) == 1 and abs(k_y-t_y) == 2

    return eats_1 or eats_2


knight = map(int, input().split())
target = map(int, input().split())

print(can_eat(knight, target))
