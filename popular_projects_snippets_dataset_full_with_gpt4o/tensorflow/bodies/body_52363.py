# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column.py
"""See `FeatureColumn` base class.

    In this case, we apply the `normalizer_fn` to the input tensor.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Normalized input tensor.
    """
input_tensor = transformation_cache.get(self.key, state_manager)
if self.normalizer_fn is not None:
    input_tensor = self.normalizer_fn(input_tensor)
exit(input_tensor)
