# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
"""Test for `fold_in`."""
orig_seed = constant_op.constant([1, 2], dtype='int32')
seed = stateless.fold_in(orig_seed, constant_op.constant(3, dtype=dtype))
new_seeds = []
new_seeds.append(seed)
seed = stateless.fold_in(seed, constant_op.constant(4, dtype=dtype))
new_seeds.append(seed)
for s in new_seeds:
    self.assertEqual(s.shape, [2])
    self.assertDTypeEqual(s.dtype, dtype)
self.assertNoEqualPair([math_ops.cast(orig_seed, dtype)] + new_seeds)
