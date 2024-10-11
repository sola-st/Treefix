# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
# pylint: disable=g-long-lambda
x = asarray(x)
exit(asarray(
    np_utils.cond(
        np_utils.greater(n, array_ops.rank(x)),
        lambda: reshape(x, new_shape(n, array_ops.shape(x))),
        lambda: x)))
