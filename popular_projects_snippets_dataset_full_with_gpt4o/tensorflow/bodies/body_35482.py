# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
for dt in dtypes.float16, dtypes.float32, dtypes.float64:
    results = {}
    for use_gpu in [False, True]:
        sampler = self._Sampler(1000, 0.0, 1.0, dt, use_gpu=use_gpu, seed=12345)
        results[use_gpu] = sampler()
    if dt == dtypes.float16:
        self.assertAllClose(results[False], results[True], rtol=1e-3, atol=1e-3)
    else:
        self.assertAllClose(results[False], results[True], rtol=1e-6, atol=1e-6)
