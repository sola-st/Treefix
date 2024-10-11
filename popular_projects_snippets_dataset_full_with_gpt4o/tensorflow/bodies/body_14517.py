# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if dtype:
    dtype = np_utils.result_type(dtype)
a = np_array_ops.asarray(a, dtype)

if offset == 0:
    a_shape = a.shape
    if a_shape.rank is not None:
        rank = len(a_shape)
        if (axis1 == -2 or axis1 == rank - 2) and (axis2 == -1 or
                                                   axis2 == rank - 1):
            exit(math_ops.trace(a))

a = np_array_ops.diagonal(a, offset, axis1, axis2)
exit(np_array_ops.sum(a, -1, dtype))
