# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
i = math_ops.cast(i, dtypes.int32)
exit((
    tensor_array_ops.TensorArray(dtypes.int32, element_shape=(), size=i)
    .unstack(math_ops.range(i, dtype=dtypes.int32))))
