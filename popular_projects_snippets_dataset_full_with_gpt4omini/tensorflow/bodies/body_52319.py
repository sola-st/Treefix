# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests _get_sparse_tensors with a dynamic sequence length."""
with ops.Graph().as_default():
    inputs = sparse_tensor.SparseTensorValue(
        indices=np.zeros((0, 2)), values=[], dense_shape=(2, 0))
    expected = sparse_tensor.SparseTensorValue(
        indices=np.zeros((0, 3)),
        values=np.array((), dtype=np.int64),
        dense_shape=(2, 0, 1))
    column = sfc.sequence_categorical_column_with_vocabulary_file(
        key='aaa',
        vocabulary_file=self._wire_vocabulary_file_name,
        vocabulary_size=self._wire_vocabulary_size)
    input_placeholder_shape = list(inputs.dense_shape)
    # Make second dimension (sequence length) dynamic.
    input_placeholder_shape[1] = None
    input_placeholder = array_ops.sparse_placeholder(
        dtypes.string, shape=input_placeholder_shape)
    id_weight_pair = _get_sparse_tensors(column, {'aaa': input_placeholder})

    self.assertIsNone(id_weight_pair.weight_tensor)
    with _initialized_session() as sess:
        result = id_weight_pair.id_tensor.eval(
            session=sess, feed_dict={input_placeholder: inputs})
        _assert_sparse_tensor_value(
            self, expected, result)
