# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
flat_values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
nested_row_splits = [[0, 2, 3, 3, 5], [0, 2, 2, 5, 6, 7]]
nested_row_partition = [
    RowPartition.from_row_splits(constant_op.constant(x, dtypes.int64))
    for x in nested_row_splits
]

rt = RaggedTensor._from_nested_row_partitions(
    flat_values, nested_row_partition, validate=False)
self.assertEqual(rt.dtype, dtypes.string)
self.assertEqual(rt.shape.as_list(), [4, None, None])
self.assertEqual(rt.ragged_rank, 2)
self.assertAllEqual(
    rt, [[[b'a', b'b'], []], [[b'c', b'd', b'e']], [], [[b'f'], [b'g']]])
