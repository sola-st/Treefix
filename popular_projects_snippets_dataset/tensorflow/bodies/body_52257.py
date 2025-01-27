# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column.py
if not isinstance(self.categorical_column, _SequenceCategoricalColumn):
    raise ValueError(
        'In embedding_column: {}. '
        'categorical_column must be of type _SequenceCategoricalColumn '
        'to use sequence_input_layer. '
        'Suggested fix: Use one of sequence_categorical_column_with_*. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
dense_tensor = self._get_dense_tensor_internal(  # pylint: disable=protected-access
    inputs=inputs,
    weight_collections=weight_collections,
    trainable=trainable)
sparse_tensors = self.categorical_column._get_sparse_tensors(inputs)  # pylint: disable=protected-access
sequence_length = fc_utils.sequence_length_from_sparse_tensor(
    sparse_tensors.id_tensor)
exit(_SequenceDenseColumn.TensorSequenceLengthPair(
    dense_tensor=dense_tensor, sequence_length=sequence_length))
