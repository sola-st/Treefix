# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/broadcast_to_ops_test.py
for dtype in [np.uint8, np.uint16, np.int8, np.int16, np.int32, np.int64,
              np.float16, np.float32, np.float64,
              dtypes.bfloat16.as_numpy_dtype]:
    with self.session():
        x = np.array([1, 2, 3], dtype=dtype)
        v_tf = array_ops.broadcast_to(constant_op.constant(x), [3, 3])
        v_np = np.broadcast_to(x, [3, 3])
        self.assertAllEqual(v_tf, v_np)
