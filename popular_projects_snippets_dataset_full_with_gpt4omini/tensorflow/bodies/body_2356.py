# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Use Anderson-Darling test to test distribution appears normal."""
self.check_dtype(dtype)
with ops.device(xla_device_name()):
    n = 1000
    gen = random.Generator.from_seed(seed=1234, alg=alg)
    x = gen.normal(shape=[n], dtype=dtype).numpy()
    # The constant 2.492 is the 5% critical value for the Anderson-Darling
    # test where the mean and variance are known. This test is probabilistic
    # so to avoid flakiness the seed is fixed.
    self.assertLess(
        random_test_util.anderson_darling(x.astype(float)), 2.492)
