# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types() + [dtypes.int32, dtypes.int64]:
    maxv = 1.0 if dt.is_floating else 17
    results = {}
    for use_gpu in False, True:
        sampler = self._Sampler(
            1000000, minv=0, maxv=maxv, dtype=dt, use_gpu=use_gpu, seed=12345)
        results[use_gpu] = sampler()
    self.assertAllEqual(results[False], results[True])
