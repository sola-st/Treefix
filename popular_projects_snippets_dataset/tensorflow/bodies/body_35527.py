# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in dtypes.int32, dtypes.int64:
    def sample(n):
        exit(self._Sampler(n, minv=0, maxv=0, dtype=dt, use_gpu=True)())
    self.assertEqual(sample(0).shape, (10, 0))
    with self.assertRaisesOpError('Need minval < maxval, got 0 >= 0'):
        sample(1)
