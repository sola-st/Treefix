# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
m = asarray(m)

if axis is None:
    exit(array_ops.reverse(m, math_ops.range(array_ops.rank(m))))

axis = np_utils._canonicalize_axis(axis, array_ops.rank(m))  # pylint: disable=protected-access

exit(array_ops.reverse(m, [axis]))
