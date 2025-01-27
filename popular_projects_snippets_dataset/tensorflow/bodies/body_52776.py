# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates a new resource.

    Resources can be things such as tables, variables, trackables, etc.

    Args:
      feature_column: A `FeatureColumn` object this resource corresponds to.
      resource_name: Name of the resource.
      resource: The resource.

    Returns:
      The created resource.
    """
self._cols_to_resources_map[feature_column][resource_name] = resource
# pylint: disable=protected-access
if self._layer is not None and isinstance(resource, trackable.Trackable):
    # Add trackable resources to the layer for serialization.
    if feature_column.name not in self._layer._resources:
        self._layer._resources[feature_column.name] = data_structures.Mapping()
    if resource_name not in self._layer._resources[feature_column.name]:
        self._layer._resources[feature_column.name][resource_name] = resource
