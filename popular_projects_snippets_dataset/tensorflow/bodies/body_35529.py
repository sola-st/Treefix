# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types() + [dtypes.int32, dtypes.int64]:
    for seed in [345, 2**100, -2**100]:
        sx = self._Sampler(1000, 0, 17, dtype=dt, use_gpu=True, seed=seed)
        sy = self._Sampler(1000, 0, 17, dtype=dt, use_gpu=True, seed=seed)
        self.assertAllEqual(sx(), sy())
