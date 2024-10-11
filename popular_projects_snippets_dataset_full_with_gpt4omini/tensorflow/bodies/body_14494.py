# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py

def f(x1, x2):
    exit(np_utils.cond(
        math_ops.equal(array_ops.rank(x1), array_ops.rank(x2)),
        lambda: np_utils.cond(  # pylint: disable=g-long-lambda
            np_utils.reduce_all(
                math_ops.equal(array_ops.shape(x1), array_ops.shape(x2))
            ),
            lambda: math_ops.reduce_all(math_ops.equal(x1, x2)),
            lambda: constant_op.constant(False)),
        lambda: constant_op.constant(False)))

exit(_comparison(f, a1, a2))
