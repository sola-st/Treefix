# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
for dt in get_float_types():
    results = {}
    for use_gpu in [False, True]:
        sampler = self._Sampler(
            1000000, 0.0, 1.0, dt, use_gpu=use_gpu, seed=12345)
        results[use_gpu] = sampler()
    rtol = atol = 1e-6
    if dt == dtypes.float16:
        rtol = atol = 1e-3
    elif dt == dtypes.bfloat16:
        rtol = atol = 1e-1
    self.assertAllClose(results[False], results[True], rtol=rtol, atol=atol)
