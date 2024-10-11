# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
for t in [
    np.float16, np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype
]:
    self._testAll(
        np.random.rand(4, 3, 2, 3, 4).astype(t),
        np.random.rand(4).astype(t))
