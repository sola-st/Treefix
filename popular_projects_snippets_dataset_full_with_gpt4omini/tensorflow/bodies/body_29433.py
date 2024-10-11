# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[4], [3], [1], [7]], dtype=dtypes.int32)
for dtype in (dtypes.int32, dtypes.int64, dtypes.float32, dtypes.float64,
              dtypes.complex64, dtypes.complex128,
              dtypes.bfloat16.as_numpy_dtype):
    updates = constant_op.constant([9, 10, 11, 12], dtype=dtype)
    ref = variables.Variable([0, 0, 0, 0, 0, 0, 0, 0], dtype=dtype)
    expected = np.array([0, 11, 0, 10, 9, 0, 0, 12])
    scatter = state_ops.scatter_nd_update(ref, indices, updates)
    init = variables.global_variables_initializer()

    with test_util.use_gpu():
        self.evaluate(init)
        result = self.evaluate(scatter)
        self.assertAllClose(result, expected)
