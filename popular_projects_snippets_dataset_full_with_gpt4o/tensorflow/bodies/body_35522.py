# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types() + [dtypes.int32, dtypes.int64]:
    sampler = self._Sampler(1000, minv=-2, maxv=8, dtype=dt, use_gpu=True)
    x = sampler()
    self.assertTrue(-2 <= np.min(x))
    self.assertTrue(np.max(x) < 8)
