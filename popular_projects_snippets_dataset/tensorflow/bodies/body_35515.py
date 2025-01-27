# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types():
    stddev = 3.0
    sampler = self._Sampler(100000, 0.0, stddev, dt, use_gpu=True)
    x = sampler()
    print("std(x)", np.std(x), abs(np.std(x) / stddev - 0.85))
    self.assertLess(abs(np.std(x) / stddev - 0.85), 0.04)
