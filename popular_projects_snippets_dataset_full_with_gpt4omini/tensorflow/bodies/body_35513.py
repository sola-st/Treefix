# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
# Skip the test if there is no GPU.
if not test.is_gpu_available():
    exit()

for dt in get_float_types():
    results = {}
    for use_gpu in [False, True]:
        # We need a particular larger number of samples to test multiple rounds
        # on GPU
        sampler = self._Sampler(
            1000000, 0.0, 1.0, dt, use_gpu=use_gpu, seed=12345)
        results[use_gpu] = sampler()
    atol = rtol = 1e-6
    if dt == dtypes.float16:
        atol = rtol = 1e-3
    if dt == dtypes.bfloat16:
        atol = rtol = 1e-1
    self.assertAllClose(results[False], results[True], rtol=rtol, atol=atol)
