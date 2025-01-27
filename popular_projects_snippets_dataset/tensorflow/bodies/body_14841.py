# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py

def run_test(a, b):
    for fn in self.array_transforms:
        arg1 = fn(a)
        arg2 = fn(b)
        self.match(
            math_fun(arg1, arg2),
            np_fun(arg1, arg2),
            msg='{}({}, {})'.format(name, arg1, arg2))
    # Tests type promotion
    for type_a in self.types:
        for type_b in self.types:
            if not check_promotion and type_a != type_b:
                continue
            arg1 = np_array_ops.array(a, dtype=type_a)
            arg2 = np_array_ops.array(b, dtype=type_b)
            self.match(
                math_fun(arg1, arg2),
                np_fun(arg1, arg2),
                msg='{}({}, {})'.format(name, arg1, arg2),
                check_dtype=check_promotion_result_type)

if operands is None:
    operands = [(5, 2), (5, [2, 3]), (5, [[2, 3], [6, 7]]), ([1, 2, 3], 7),
                ([1, 2, 3], [5, 6, 7])]
for operand1, operand2 in operands:
    run_test(operand1, operand2)
if extra_operands is not None:
    for operand1, operand2 in extra_operands:
        run_test(operand1, operand2)
