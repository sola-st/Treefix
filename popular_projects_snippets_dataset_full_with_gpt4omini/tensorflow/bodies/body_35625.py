# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
for dt in _SUPPORTED_DTYPES:
    results = {}
    for use_gpu in [False, True]:
        sampler = self._Sampler(1000, 1.0, dt, use_gpu=use_gpu, seed=12345)
        results[use_gpu] = sampler()
    if dt == dtypes.float16:
        self.assertAllClose(results[False], results[True], rtol=1e-3, atol=1e-3)
    else:
        self.assertAllClose(results[False], results[True], rtol=1e-6, atol=1e-6)
