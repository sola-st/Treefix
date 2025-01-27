# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
for t in [
    np.float16, np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype
]:
    self._testSelu(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t))
    # Force executed on CPU in case GPU kernels are available.
    with ops.device("/device:CPU:0"):
        self._testSelu(
            np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t))
