# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
for dt in dtypes.float16, dtypes.float32, dtypes.float64:
    sx = self._Sampler(1000, 1.0, dt, use_gpu=True, seed=345)
    sy = self._Sampler(1000, 1.0, dt, use_gpu=True, seed=345)
    self.assertAllEqual(sx(), sy())
