# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
for dt in dtypes.float16, dtypes.float32, dtypes.float64:
    sampler = self._Sampler(1000, 2.0, 1.0, dt)
    x = sampler()
    y = sampler()
    # Number of different samples.
    count = (x == y).sum()
    count_limit = 20 if dt == dtypes.float16 else 10
    self.assertLess(count, count_limit)
