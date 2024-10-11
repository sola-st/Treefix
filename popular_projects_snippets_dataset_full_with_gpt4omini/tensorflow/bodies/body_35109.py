# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
for t in [np.float16, np.float32, np.float64]:
    lower = {np.float16: -15, np.float32: -50, np.float64: -50}.get(t, -100)
    upper = {np.float16: 50, np.float32: 50, np.float64: 50}.get(t, 100)
    self._testSoftplus(
        np.array(np.linspace(lower, upper, int(1e3)).astype(t)).reshape(
            [2, -1]),
        use_gpu=False)
    self._testSoftplus(
        np.array(np.linspace(lower, upper, int(1e3)).astype(t)).reshape(
            [2, -1]),
        use_gpu=True)
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
