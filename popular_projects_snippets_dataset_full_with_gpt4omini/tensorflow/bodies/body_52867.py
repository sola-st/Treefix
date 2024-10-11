# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns tensor after doing the embedding lookup.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Embedding lookup tensor.

    Raises:
      ValueError: `categorical_column` is SequenceCategoricalColumn.
    """
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
# Get sparse IDs and weights.
sparse_tensors = self.categorical_column.get_sparse_tensors(
    transformation_cache, state_manager)
exit(self._get_dense_tensor_internal(sparse_tensors, state_manager))
