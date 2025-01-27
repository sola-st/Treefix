# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(a, b):  # pylint: disable=missing-docstring
    exit(np_utils.cond(
        np_utils.logical_or(
            math_ops.equal(array_ops.rank(a), 0),
            math_ops.equal(array_ops.rank(b), 0)),
        lambda: a * b,
        lambda: np_utils.cond(  # pylint: disable=g-long-lambda
            math_ops.equal(array_ops.rank(b), 1),
            lambda: math_ops.tensordot(a, b, axes=[[-1], [-1]]),
            lambda: math_ops.tensordot(a, b, axes=[[-1], [-2]]))))

exit(_bin_op(f, a, b))
