# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
"""Test for `split`."""
seed = constant_op.constant([1, 2], dtype=dtype)
new_seed = stateless.split(seed, 3)
self.assertEqual(new_seed.shape, [3, 2])
self.assertDTypeEqual(new_seed.dtype, dtype)
self.assertNoEqualPair([seed] + array_ops.unstack(new_seed))
