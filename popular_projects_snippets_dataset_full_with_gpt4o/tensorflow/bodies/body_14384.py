# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(a, b):
    exit(np_utils.cond(
        np_utils.logical_or(
            math_ops.equal(array_ops.rank(a), 0),
            math_ops.equal(array_ops.rank(b), 0)), lambda: a * b,
        lambda: math_ops.tensordot(a, b, axes=[[-1], [-1]])))

exit(_bin_op(f, a, b))
