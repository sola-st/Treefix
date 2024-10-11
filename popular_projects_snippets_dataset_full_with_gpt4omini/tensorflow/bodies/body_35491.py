# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
for dt in dtypes.float16, dtypes.float32, dtypes.float64:
    sx = self._Sampler(1000, counts=10., probs=0.4, dtype=dt, seed=345)
    sy = self._Sampler(1000, counts=10., probs=0.4, dtype=dt, seed=345)
    self.assertAllEqual(self.evaluate(sx()), self.evaluate(sy()))
