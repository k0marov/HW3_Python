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
    def eval_slice(start, end):
        length = end-start
        if length == 1:
            return exp[0]
        elif length == 3:
            return apply_op(*exp[start:end])
        left, right = 0, 0
        if exp[start+2] in OPERATORS:
            left = eval_slice(start, start+3)
            right = eval_slice(start+3, end-1)
        else:
            left = eval_slice(start, start)
            right = eval_slice(start+1, end-1)
        return apply_op(left, right, exp[end-1])
    return eval_slice(0, len(exp))


exp = list(input().split())

print(evaluate(exp))
