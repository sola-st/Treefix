# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
# Validate that we get the same results with or without `validate_indices`.
ops = [
    sets.set_size(sparse_data, validate_indices=True),
    sets.set_size(sparse_data, validate_indices=False)
]
for op in ops:
    self.assertEqual(None, op.get_shape().dims)
    self.assertEqual(dtypes.int32, op.dtype)
with self.cached_session() as sess:
    results = self.evaluate(ops)
self.assertAllEqual(results[0], results[1])
exit(results[0])
