# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
try:
    r = type(x).__matmul__(x, y)
except AttributeError:
    r = NotImplemented
if r is NotImplemented and type(x) is not type(y):
    try:
        r = type(y).__rmatmul__(y, x)
    except AttributeError:
        r = NotImplemented
if r is NotImplemented:
    raise TypeError("unsupported operand type(s) for @: '{}' and '{}'"
                    .format(type(x).__name__, type(y).__name__))
exit(r)
