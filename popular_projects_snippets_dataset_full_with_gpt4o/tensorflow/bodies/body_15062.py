# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = [b'a', b'b', b'c', b'd', b'e', b'f', b'g']
row_splits = [0, 2, 5, 6, 6, 7]
rt = ragged_tensor_value.RaggedTensorValue(
    np.array(values), np.array(row_splits, dtype=np.int64))
expected_str = '<tf.RaggedTensorValue {}>'.format([[b'a', b'b'],
                                                   [b'c', b'd', b'e'],
                                                   [b'f'], [], [b'g']])
expected_repr = ("tf.RaggedTensorValue(values=array({}, dtype='|S1'), "
                 'row_splits=array({}))'.format(values, row_splits))
self.assertEqual(' '.join(str(rt).split()), expected_str)
self.assertEqual(' '.join(repr(rt).split()), expected_repr)
