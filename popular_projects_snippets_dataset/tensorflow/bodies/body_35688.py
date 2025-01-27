# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Use Pearson's Chi-squared test to test for uniformity."""
if dtype == dtypes.bfloat16 and not test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    self.skipTest("Bfloat16 requires compute capability 8.0")
n = 1000
seed = 123
gen = random.Generator.from_seed(seed)
maxval = 1
if dtype.is_integer:
    maxval = 100
x = gen.uniform(shape=[n], maxval=maxval, dtype=dtype).numpy()
if maxval > 1:
    # Normalize y to range [0, 1).
    x = x.astype(float) / maxval
# Tests that the values are distributed amongst 10 bins with equal
# probability. 16.92 is the Chi^2 value for 9 degrees of freedom with
# p=0.05. This test is probabilistic and would be flaky if the random
# seed were not fixed.
val = random_test_util.chi_squared(x, 10)
self.assertLess(val, 16.92)
