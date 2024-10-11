# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
"""Creates a new variable.

    Args:
      feature_column: A `FeatureColumn` object this variable corresponds to.
      name: variable name.
      shape: variable shape.
      dtype: The type of the variable. Defaults to `self.dtype` or `float32`.
      trainable: Whether this variable is trainable or not.
      use_resource: If true, we use resource variables. Otherwise we use
        RefVariable.
      initializer: initializer instance (callable).

    Returns:
      The created variable.
    """
if name in self._cols_to_vars_map[feature_column]:
    raise ValueError('Variable already exists.')

# We explicitly track these variables since `name` is not guaranteed to be
# unique and disable manual tracking that the add_weight call does.
with trackable.no_manual_dependency_tracking_scope(self._layer):
    var = self._layer.add_weight(
        name=name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        trainable=self._trainable and trainable,
        use_resource=use_resource,
        # TODO(rohanj): Get rid of this hack once we have a mechanism for
        # specifying a default partitioner for an entire layer. In that case,
        # the default getter for Layers should work.
        getter=variable_scope.get_variable)
if isinstance(var, variables.PartitionedVariable):
    for v in var:
        part_name = name + '/' + str(v._get_save_slice_info().var_offset[0])  # pylint: disable=protected-access
        self._layer._track_trackable(v, feature_column.name + '/' + part_name)  # pylint: disable=protected-access
else:
    if isinstance(var, trackable.Trackable):
        self._layer._track_trackable(var, feature_column.name + '/' + name)  # pylint: disable=protected-access

self._cols_to_vars_map[feature_column][name] = var
exit(var)
