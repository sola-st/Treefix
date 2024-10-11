# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types():
    sx = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=True, seed=345)
    sy = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=True, seed=345)
    self.assertAllEqual(sx(), sy())
