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
    if len(exp) == 1:
        return exp[0]
    elif len(exp) == 3:
        return apply_op(*exp)
    left, right = 0, 0
    if exp[2] in OPERATORS:
        left = evaluate(exp[:3])
        right = evaluate(exp[3:-1])
    else:
        left = evaluate([exp[0]])
        right = evaluate(exp[1:-1])
    return apply_op(left, right, exp[-1])


exp = list(input().split())

print(evaluate(exp))
