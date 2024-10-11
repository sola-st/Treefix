# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
split_dim = constant_op.constant(1, dtype=dtypes.int64)
indices = constant_op.constant([[0, 2], [0, 4], [0, 5], [1, 0], [1, 1]],
                               dtype=dtypes.int64)
values = constant_op.constant([2, 3, 5, 7, 11])
shape = constant_op.constant([2, 7], dtype=dtypes.int64)
result = sparse_ops.gen_sparse_ops.sparse_split(
    split_dim,
    indices,
    values,
    shape,
    num_split=2)
output_indices, output_values, output_shape = result
self.assertLen(output_indices, 2)
self.assertLen(output_values, 2)
self.assertLen(output_shape, 2)
self.assertEqual(output_indices, result.output_indices)
self.assertEqual(output_values, result.output_values)
self.assertEqual(output_shape, result.output_shape)
self.assertAllEqual([[0, 2], [1, 0], [1, 1]], output_indices[0])
self.assertAllEqual([[0, 0], [0, 1]], output_indices[1])
self.assertAllEqual([2, 7, 11], output_values[0])
self.assertAllEqual([3, 5], output_values[1])
self.assertAllEqual([2, 4], output_shape[0])
self.assertAllEqual([2, 3], output_shape[1])
