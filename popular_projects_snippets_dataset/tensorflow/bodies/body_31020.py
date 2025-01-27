# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
if not test.is_gpu_available():
    self.skipTest("No GPU available")
for t in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    self._testLeakyRelu(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t),
        alpha=0.1)
