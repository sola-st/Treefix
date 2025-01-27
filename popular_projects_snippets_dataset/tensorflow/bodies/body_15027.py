# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
row_splits = constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
rp = RowPartition.from_row_splits(row_splits)
rt = RaggedTensor(values=values, row_partition=rp, internal=True)

self.assertAllEqual(rt,
                    [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
