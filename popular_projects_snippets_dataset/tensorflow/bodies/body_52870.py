# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
if not isinstance(
    self.categorical_column,
    (SequenceCategoricalColumn, fc_old._SequenceCategoricalColumn)):  # pylint: disable=protected-access
    raise ValueError(
        'In embedding_column: {}. '
        'categorical_column must be of type SequenceCategoricalColumn '
        'to use SequenceFeatures. '
        'Suggested fix: Use one of sequence_categorical_column_with_*. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
sparse_tensors = self.categorical_column._get_sparse_tensors(inputs)  # pylint: disable=protected-access
dense_tensor = self._old_get_dense_tensor_internal(
    sparse_tensors,
    weight_collections=weight_collections,
    trainable=trainable)
sequence_length = fc_utils.sequence_length_from_sparse_tensor(
    sparse_tensors.id_tensor)
exit(SequenceDenseColumn.TensorSequenceLengthPair(
    dense_tensor=dense_tensor, sequence_length=sequence_length))
