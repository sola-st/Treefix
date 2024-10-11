# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests that non_deterministic_ints returns different results every time.

    This test is flaky, but with very low probability of failing.
    """
shape = [2, 3]
dtype = dtypes.int64
a = random.non_deterministic_ints(shape=shape, dtype=dtype)
self.assertAllEqual(shape, a.shape)
self.assertEqual(dtype, a.dtype)
b = random.non_deterministic_ints(shape, dtype=dtype)
self.assertAllDifferent([a, b])
