# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cumulative_logsumexp_test.py
for dtype in self.valid_dtypes:
    for reverse in (True, False):
        for exclusive in (True, False):
            self._testLogSumExp(
                x, dtype=dtype, use_gpu=use_gpu,
                reverse=reverse, exclusive=exclusive,
                axis=axis)
