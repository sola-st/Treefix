# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softplus_op_test.py
for t in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    self._testSoftplus(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t),
        use_gpu=False)
    self._testSoftplus(
        np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]).astype(t),
        use_gpu=True)
    if t == dtypes.bfloat16.as_numpy_dtype:
        # bfloat16 dtype doesn't have finfo.
        # Calculate epsilon using machine_epsilon = base ^ (-(precision - 1))
        log_eps = np.log(2 ** (-(8 - 1)))
    else:
        log_eps = np.log(np.finfo(t).eps)
    one = t(1)
    ten = t(10)
    self._testSoftplus(
        [
            log_eps, log_eps - one, log_eps + one, log_eps - ten,
            log_eps + ten, -log_eps, -log_eps - one, -log_eps + one,
            -log_eps - ten, -log_eps + ten
        ],
        use_gpu=False)
    self._testSoftplus(
        [
            log_eps, log_eps - one, log_eps + one, log_eps - ten,
            log_eps + ten - log_eps, -log_eps - one, -log_eps + one,
            -log_eps - ten, -log_eps + ten
        ],
        use_gpu=True)
