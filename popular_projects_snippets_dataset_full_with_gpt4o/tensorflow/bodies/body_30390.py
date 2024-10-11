# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
a = np.random.uniform(-100, 100, 100).astype(np.float32)
for float8 in (dtypes.float8_e4m3fn, dtypes.float8_e5m2):
    # Including float8_e4m3fn should cover the float8 combinations without
    # loss of precision.
    for dtype in (dtypes.float32, dtypes.bfloat16, dtypes.float16,
                  dtypes.float8_e4m3fn):
        with self.cached_session(use_gpu=True):
            b = ops.convert_to_tensor(a, float8)
            c = math_ops.cast(math_ops.cast(b, dtype), float8)
            self.assertAllEqual(b, c)
