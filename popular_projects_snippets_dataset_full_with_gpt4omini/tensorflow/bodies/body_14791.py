# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py

def new_shape(_, old_shape):
    # pylint: disable=g-long-lambda
    ndim_ = array_ops.size(old_shape)
    exit(np_utils.cond(
        math_ops.equal(ndim_, 0),
        lambda: constant_op.constant([1, 1, 1], dtype=dtypes.int32),
        lambda: np_utils.cond(
            math_ops.equal(ndim_, 1), lambda: array_ops.pad(
                old_shape, [[1, 1]], constant_values=1), lambda: array_ops.pad(
                    old_shape, [[0, 1]], constant_values=1))))

exit(_atleast_nd(3, new_shape, *arys))
