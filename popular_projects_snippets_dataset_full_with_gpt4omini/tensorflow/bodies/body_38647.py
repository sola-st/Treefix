# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
x = np.arange(10) / 10.0 - 0.5
self._testLogSumExpAllArgs(x, use_gpu=False)
self._testLogSumExpAllArgs(x, use_gpu=True)
