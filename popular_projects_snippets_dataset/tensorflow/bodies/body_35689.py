# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Use Anderson-Darling test to test distribution appears normal."""
if dtype == dtypes.bfloat16 and not test_util.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(8, 0)):
    self.skipTest("Bfloat16 requires compute capability 8.0")
n = 1000
gen = random.Generator.from_seed(1234)
x = gen.normal(shape=[n], dtype=dtype).numpy()
# The constant 2.492 is the 5% critical value for the Anderson-Darling
# test where the mean and variance are known. This test is probabilistic
# so to avoid flakiness the seed is fixed.
self.assertLess(
    random_test_util.anderson_darling(x.astype(float)), 2.492)
