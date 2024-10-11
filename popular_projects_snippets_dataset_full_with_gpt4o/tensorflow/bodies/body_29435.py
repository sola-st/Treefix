# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[4], [3], [1], [7]], dtype=dtypes.int32)
for dtype in (dtypes.int32, dtypes.float32, dtypes.bfloat16):
    updates = constant_op.constant([9, 10, 11, 12], dtype=dtype)
    ref = resource_variable_ops.ResourceVariable([0, 0, 0, 0, 0, 0, 0, 0],
                                                 dtype=dtype)
    expected = np.array([0, 11, 0, 10, 9, 0, 0, 12])
    scatter = state_ops.scatter_nd_update(ref, indices, updates)

    with test_util.device(use_gpu=True):
        self.evaluate(ref.initializer)
        self.evaluate(scatter)
        self.assertAllClose(ref, expected)
