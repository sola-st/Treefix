# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
for dtype in (dtypes.int32, dtypes.float32):
    indices = constant_op.constant([[4], [3], [1], [7]])
    updates = constant_op.constant([9, 10, 11, 12], dtype=dtype)
    t = array_ops.ones([8], dtype=dtype)
    assigned = array_ops.tensor_scatter_update(t, indices, updates)
    added = array_ops.tensor_scatter_add(t, indices, updates)
    subbed = array_ops.tensor_scatter_sub(t, indices, updates)

    self.assertAllEqual(assigned,
                        constant_op.constant([1, 11, 1, 10, 9, 1, 1, 12]))
    self.assertAllEqual(added,
                        constant_op.constant([1, 12, 1, 11, 10, 1, 1, 13]))
    self.assertAllEqual(subbed,
                        constant_op.constant([1, -10, 1, -9, -8, 1, 1, -11]))
