# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
if dtype == dtypes.bfloat16 and not test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    self.skipTest("Bfloat16 requires compute capability 8.0")
minval = 2
maxval = 33
size = 1000
gen = random.Generator.from_seed(1234)
x = gen.uniform(
    shape=[size], dtype=dtype, minval=minval, maxval=maxval).numpy()
self.assertTrue(np.all(x >= minval))
self.assertTrue(np.all(x < maxval))
