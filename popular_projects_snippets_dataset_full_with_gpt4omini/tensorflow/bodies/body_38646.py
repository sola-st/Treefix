# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
x = np.log([0., 0., 1., 1., 1., 1., 0., 0.])
self._testLogSumExpAllArgs(x, use_gpu=False)
self._testLogSumExpAllArgs(x, use_gpu=True)
