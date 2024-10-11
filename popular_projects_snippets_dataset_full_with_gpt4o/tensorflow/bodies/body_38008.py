# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
if not test_util.is_gpu_available():
    self.skipTest("Requires GPU")
# Negative integer powers return zero on GPUs for abs(LHS) > 1. Negative
# integer powers for 1 and -1 will return the correct result.
x = np.array([2, 3, 1, -1, -1]).astype(np.int64)
y = np.array([-1, 0, -2, -2, -3]).astype(np.int64)
z = math_ops.pow(x, y)
self.assertAllEqual(self.evaluate(z), [0, 1, 1, 1, -1])
