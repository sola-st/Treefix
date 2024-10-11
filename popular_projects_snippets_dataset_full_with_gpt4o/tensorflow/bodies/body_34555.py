# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
size = 10
ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=size)
_, ta = control_flow_ops.while_loop(
    lambda i, _: i < size,
    lambda i, ta: (i + 1, ta.write(i, [[0.]])), [0, ta],
    parallel_iterations=1)
self.assertIsNotNone(ta.element_shape.dims)
