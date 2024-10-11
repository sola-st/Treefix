# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns an already created resource.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      resource_name: Name of the resource.
    """
if (feature_column not in self._cols_to_resources_map or
    resource_name not in self._cols_to_resources_map[feature_column]):
    raise ValueError('Resource does not exist.')
exit(self._cols_to_resources_map[feature_column][resource_name])
