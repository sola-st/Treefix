# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
for dtype in (dtypes.int32, dtypes.float32):
    indices = constant_op.constant([[4], [3], [1], [7]])
    updates = constant_op.constant([0, 2, -1, 2], dtype=dtype)
    t = array_ops.ones([8], dtype=dtype)
    assigned = array_ops.tensor_scatter_update(t, indices, updates)
    min_result = array_ops.tensor_scatter_min(t, indices, updates)
    max_result = array_ops.tensor_scatter_max(t, indices, updates)

    self.assertAllEqual(assigned,
                        constant_op.constant([1, -1, 1, 2, 0, 1, 1, 2]))
    self.assertAllEqual(min_result,
                        constant_op.constant([1, -1, 1, 1, 0, 1, 1, 1]))
    self.assertAllEqual(max_result,
                        constant_op.constant([1, 1, 1, 2, 1, 1, 1, 2]))
