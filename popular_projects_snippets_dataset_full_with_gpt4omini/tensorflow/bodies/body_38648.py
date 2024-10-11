# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
x = np.reshape(np.arange(20) / 20.0 - 0.5, (2, 10))

for axis in (-2, -1, 0, 1):
    self._testLogSumExpAllArgs(x, axis=axis, use_gpu=False)
    self._testLogSumExpAllArgs(x, axis=axis, use_gpu=True)
