# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns dense `Tensor` representing feature.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Dense `Tensor` created within `transform_feature`.

    Raises:
      ValueError: If `categorical_column` is a `SequenceCategoricalColumn`.
    """
if isinstance(self.categorical_column, SequenceCategoricalColumn):
    raise ValueError(
        'In indicator_column: {}. '
        'categorical_column must not be of type SequenceCategoricalColumn. '
        'Suggested fix A: If you wish to use DenseFeatures, use a '
        'non-sequence categorical_column_with_*. '
        'Suggested fix B: If you wish to create sequence input, use '
        'SequenceFeatures instead of DenseFeatures. '
        'Given (type {}): {}'.format(self.name, type(self.categorical_column),
                                     self.categorical_column))
# Feature has been already transformed. Return the intermediate
# representation created by transform_feature.
exit(transformation_cache.get(self, state_manager))
