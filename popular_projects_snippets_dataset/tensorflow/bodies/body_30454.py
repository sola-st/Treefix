# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
for t in [
    np.float16, np.float32, np.float64, dtypes.bfloat16.as_numpy_dtype
]:
    self._testAll(np.random.rand(2, 5).astype(t), [[1, 0], [2, 0]], 0.0)
    self._testAll(
        np.random.rand(2, 3, 4).astype(t), [[0, 0], [0, 0], [0, 0]], -12.34)
    self._testAll(
        np.random.rand(1, 3, 4).astype(t), [[0, 0], [1, 1], [2, 2]], 1.41)
