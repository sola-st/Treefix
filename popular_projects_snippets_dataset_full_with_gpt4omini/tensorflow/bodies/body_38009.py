# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
"""Regression test for GitHub issue #58369."""
if not test_util.is_gpu_available():
    self.skipTest("Requires GPU")

dtypes = [
    dtypes_lib.bfloat16.as_numpy_dtype,
    np.float16,
    np.float32,
    np.float64,
]

for dtype in dtypes:
    x = np.array([4, 0, -1, 4, 0, -1], dtype=dtype)
    y = np.array([np.inf, np.inf, np.inf, -np.inf, -np.inf, -np.inf],
                 dtype=dtype)
    expected = np.array([4, 0, np.inf, -np.inf, 0, -1], dtype=dtype)

    self.assertAllClose(self.evaluate(math_ops.mod(x, y)), expected)
