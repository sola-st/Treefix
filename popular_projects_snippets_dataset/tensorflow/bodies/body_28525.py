# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
i = math_ops.cast(i, dtypes.int32)
exit((
    tensor_array_ops.TensorArray(
        dtype=dtypes.int32, element_shape=(), size=i)
    .unstack(math_ops.range(i))))
