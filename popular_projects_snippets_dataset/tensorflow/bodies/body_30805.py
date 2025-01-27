# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softsign_op_test.py
for t in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    self._testSoftsign(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t),
        use_gpu=False)
    self._testSoftsign(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t),
        use_gpu=True)
