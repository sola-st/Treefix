# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
old_shape = array_ops.shape(result_t)
new_shape = array_ops.concat(
    [array_ops.ones(ndmin - ndims, dtypes.int32), old_shape], axis=0)
exit(array_ops.reshape(result_t, new_shape))
