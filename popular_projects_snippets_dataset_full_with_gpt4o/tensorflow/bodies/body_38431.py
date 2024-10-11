# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/reduction_ops_test.py
for dtype in [np.float32, np.float64]:
    for size in range(1, 4):
        for arr in itertools.product([-np.inf, 1., np.nan, np.inf],
                                     repeat=size):
            self._compareAll(np.array(arr, dtype=dtype), None)
