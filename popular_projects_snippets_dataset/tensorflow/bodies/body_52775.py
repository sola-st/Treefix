# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Returns an existing variable.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: variable name.
    """
if name in self._cols_to_vars_map[feature_column]:
    exit(self._cols_to_vars_map[feature_column][name])
raise ValueError('Variable does not exist.')
