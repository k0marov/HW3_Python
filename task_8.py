PLUS = '+'
MINUS = '-'
MULT = '*'
OPERATORS = [PLUS, MINUS, MULT]


def apply_op(left, right, op):
    l_op = int(left)
    r_op = int(right)
    if op == PLUS:
        return l_op + r_op
    elif op == MINUS:
        return l_op - r_op
    elif op == MULT:
        return l_op * r_op
    # raise Exception ...


def evaluate(exp):
    cache = []
    for token in exp:
        if token in OPERATORS:
            right = cache.pop()
            left = cache.pop()
            cache.append(apply_op(left, right, token))
        else:
            cache.append(token)
    return cache[0]


exp = list(input().split())

print(evaluate(exp))
