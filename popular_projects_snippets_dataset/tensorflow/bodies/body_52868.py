# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
if isinstance(
    self.categorical_column,
    (SequenceCategoricalColumn, fc_old._SequenceCategoricalColumn)):  # pylint: disable=protected-access
    raise ValueError(
        'In embedding_column: {}. '
        'categorical_column must not be of type _SequenceCategoricalColumn. '
        'Suggested fix A: If you wish to use DenseFeatures, use a '
        'non-sequence categorical_column_with_*. '
        'Suggested fix B: If you wish to create sequence input, use '
        'SequenceFeatures instead of DenseFeatures. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
sparse_tensors = self.categorical_column._get_sparse_tensors(  # pylint: disable=protected-access
    inputs, weight_collections, trainable)
exit(self._old_get_dense_tensor_internal(sparse_tensors,
                                           weight_collections, trainable))
