# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types():
    sampler = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=True)
    x = sampler()
    y = sampler()
    # Number of different samples.
    count = (x == y).sum()
    if count >= 10:
        print("x = ", x)
        print("y = ", y)
        print("count = ", count)
    self.assertTrue(count < 10)
