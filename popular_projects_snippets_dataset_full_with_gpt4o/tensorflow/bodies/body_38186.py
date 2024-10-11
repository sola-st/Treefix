# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
for dtype in (dtypes_lib.int32, dtypes_lib.int64, dtypes_lib.float16,
              dtypes_lib.float32, dtypes_lib.float64):
    with self.subTest(dtype=dtype):
        x = array_ops.placeholder(dtype)
        y = math_ops.conj(x)
        self.assertEqual(x, y)
