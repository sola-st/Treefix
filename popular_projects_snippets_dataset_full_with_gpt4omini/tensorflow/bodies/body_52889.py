# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns the embedding lookup result."""
if isinstance(self.categorical_column, SequenceCategoricalColumn):
    raise ValueError(
        'In embedding_column: {}. '
        'categorical_column must not be of type SequenceCategoricalColumn. '
        'Suggested fix A: If you wish to use DenseFeatures, use a '
        'non-sequence categorical_column_with_*. '
        'Suggested fix B: If you wish to create sequence input, use '
        'SequenceFeatures instead of DenseFeatures. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
exit(self._get_dense_tensor_internal(transformation_cache, state_manager))
