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

# def evaluate(left, right=[0], op=PLUS):
#     if len(left) != 0:
#         l_val = evaluate()
#
#


def evaluate(exp):
    if len(exp) == 1:
        return int(exp[0])
    elif len(exp) == 3:
        return apply_op(*exp)
    # left = apply_op(*exp[:3])
    # right = apply_op(*exp[3:-1])
    # return apply_op(left, right, exp[-1])

    left, right, op = exp[:3]
    if op in OPERATORS:
        left = apply_op(left, right, op)
        right = evaluate(exp[3:-1])
        return apply_op(left, right, exp[-1])
    else:
        right = evaluate(exp[1:-1])
        return apply_op(left, right, exp[-1])
    #
    # left = None
    # right = None
    # for i in range(len(exp)):
    #     token = exp[i]
    #     if token in OPERATORS:
    #         left = apply_op(left, right, token)
    #         right = evaluate(exp[i+1:-1])
    #         return apply_op(left, right, exp[i-1])
    #     elif left is None:
    #         left = token
    #     elif right is None:
    #         right = token
    #     else:
    #         right = evaluate([right]+exp[i:-1])
    #         return apply_op(left, right, exp[i-1])
    #
    # return 0


exp = list(input().split())

print(evaluate(exp))
