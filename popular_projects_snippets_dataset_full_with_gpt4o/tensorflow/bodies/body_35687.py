# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
if dtype == dtypes.bfloat16 and not test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    self.skipTest("Bfloat16 requires compute capability 8.0")
gen = random.Generator.from_seed(1234)
x = gen.normal(shape=[10000], dtype=dtype).numpy()
self.assertTrue(np.all(np.isfinite(x)))
