# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Converts a `ResourceVariable` to a `VariableDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Raises:
      RuntimeError: If run in EAGER mode.

    Returns:
      A `VariableDef` protocol buffer, or `None` if the `Variable` is not
      in the specified name scope.
    """
if context.executing_eagerly():
    raise RuntimeError("This operation is not supported "
                       "when eager execution is enabled.")
if export_scope is None or self.handle.name.startswith(export_scope):
    var_def = variable_pb2.VariableDef()
    var_def.variable_name = ops.strip_name_scope(self.handle.name,
                                                 export_scope)
    if self._initial_value is not None:
        # This is inside an if-statement for backwards compatibility, since
        # self._initial_value might be None for variables constructed from old
        # protos.
        var_def.initial_value_name = ops.strip_name_scope(
            self._initial_value.name, export_scope)
    var_def.initializer_name = ops.strip_name_scope(self.initializer.name,
                                                    export_scope)
    if self._cached_value is not None:
        var_def.snapshot_name = ops.strip_name_scope(self._cached_value.name,
                                                     export_scope)
    else:
        # Store the graph_element here
        var_def.snapshot_name = ops.strip_name_scope(self._graph_element.name,
                                                     export_scope)
    var_def.is_resource = True
    var_def.trainable = self.trainable
    var_def.synchronization = self.synchronization.value
    var_def.aggregation = self.aggregation.value
    if self._save_slice_info:
        var_def.save_slice_info_def.MergeFrom(
            self._save_slice_info.to_proto(export_scope=export_scope))
    exit(var_def)
else:
    exit(None)
