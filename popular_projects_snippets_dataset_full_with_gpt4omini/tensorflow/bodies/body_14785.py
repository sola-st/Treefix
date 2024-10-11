# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
old_shape = asarray(old_shape, dtype=np.int32)
new_shape = array_ops.pad(
    old_shape, [[math_ops.maximum(n - array_ops.size(old_shape), 0), 0]],
    constant_values=1)
exit(asarray(new_shape))
