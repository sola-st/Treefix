# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
for reverse in (True, False):
    for exclusive in (True, False):
        x = np.arange(10) / 10.0 - 0.5

        self._testGradient(x, use_gpu=False,
                           reverse=reverse, exclusive=exclusive)
        self._testGradient(x, use_gpu=True,
                           reverse=reverse, exclusive=exclusive)
