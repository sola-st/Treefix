# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = [b'a', b'b', b'c', b'd', b'e', b'f', b'g']
row_splits = [0, 2, 5, 6, 6, 7]
rt = RaggedTensor.from_row_splits(values, row_splits, validate=False)
splits_type = 'int64'
if context.executing_eagerly():
    expected_repr = '<tf.RaggedTensor {}>'.format([[b'a', b'b'],
                                                   [b'c', b'd', b'e'], [b'f'],
                                                   [], [b'g']])
else:
    expected_repr = (
        'tf.RaggedTensor(values=Tensor("RaggedFromRowSplits/values:0", '
        'shape=(7,), dtype=string), '
        'row_splits=Tensor('
        '"RaggedFromRowSplits/RowPartitionFromRowSplits/row_splits:0",'
        ' shape=(6,), dtype={}))').format(splits_type)
self.assertEqual(repr(rt), expected_repr)
self.assertEqual(str(rt), expected_repr)
