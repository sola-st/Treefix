# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates an _StateManagerImpl object.

    Args:
      layer: The input layer this state manager is associated with.
      trainable: Whether by default, variables created are trainable or not.
    """
self._trainable = trainable
self._layer = layer
if self._layer is not None and not hasattr(self._layer, '_resources'):
    self._layer._resources = data_structures.Mapping()  # pylint: disable=protected-access
self._cols_to_vars_map = collections.defaultdict(lambda: {})
self._cols_to_resources_map = collections.defaultdict(lambda: {})
