# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/clip_ops_test.py
values = constant_op.constant(values)
indices = constant_op.constant(indices)
shape = constant_op.constant(shape)
# IndexedSlices mode
indexed_slices = indexed_slices_lib.IndexedSlices(values, indices, shape)
clipped = clip_ops.clip_by_norm(indexed_slices, max_norm, axes)
# clipped should be IndexedSlices
self.assertIsInstance(clipped, indexed_slices_lib.IndexedSlices)
clipped = ops.convert_to_tensor(clipped)

# Tensor mode
dense_tensor = ops.convert_to_tensor(indexed_slices)
dense_clipped = clip_ops.clip_by_norm(dense_tensor, max_norm, axes)
result, expected = self.evaluate([clipped, dense_clipped])
self.assertAllClose(result, expected)
