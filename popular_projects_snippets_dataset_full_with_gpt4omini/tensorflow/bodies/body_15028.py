# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
row_splits = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
rp = RowPartition.from_row_splits(row_splits)

with self.assertRaisesRegex(ValueError,
                            'RaggedTensor constructor is private'):
    RaggedTensor(values=values, row_partition=rp)

with self.assertRaisesRegex(
    TypeError, r'type\(values\) must be one of: Tensor, RaggedTensor'):
    RaggedTensor(values=range(7), row_partition=rp, internal=True)

with self.assertRaisesRegex(
    TypeError, 'Argument `row_partition` must be a RowPartition'):
    RaggedTensor(
        values=values, row_partition=[0, 2, 2, 5, 6, 7], internal=True)
