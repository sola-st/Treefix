# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_test.py
for dtype in [np.float16, np.float32, np.float64,
              dtypes_lib.bfloat16.as_numpy_dtype]:
    with self.subTest(dtype=dtype):
        self._testDtype(dtype)
