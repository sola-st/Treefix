# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns dense `Tensor` representing feature.

    Args:
      transformation_cache: A `FeatureTransformationCache` object to access
        features.
      state_manager: A `StateManager` to create / access resources such as
        lookup tables.

    Returns:
      Transformed feature `Tensor`.

    Raises:
      ValueError: if input rank is not known at graph building time.
    """
id_weight_pair = self.categorical_column.get_sparse_tensors(
    transformation_cache, state_manager)
exit(self._transform_id_weight_pair(id_weight_pair,
                                      self.variable_shape[-1]))
