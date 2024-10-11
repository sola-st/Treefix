# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
def f(x1, x2):
    try:
        if x1._rank() == 2 and x2._rank() == 2:  # pylint: disable=protected-access
            # Fast path for known ranks.
            exit(gen_math_ops.mat_mul(x1, x2))
        exit(np_utils.cond(
            math_ops.equal(np_utils.tf_rank(x2), 1),
            lambda: math_ops.tensordot(x1, x2, axes=1),
            lambda: np_utils.cond(  # pylint: disable=g-long-lambda
                math_ops.equal(np_utils.tf_rank(x1), 1),
                lambda: math_ops.tensordot(  # pylint: disable=g-long-lambda
                    x1, x2, axes=[[0], [-2]]),
                lambda: math_ops.matmul(x1, x2))))
    except errors.InvalidArgumentError as err:
        raise ValueError(str(err)).with_traceback(sys.exc_info()[2])

exit(_bin_op(f, x1, x2))
