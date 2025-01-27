# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Converts a `Variable` to a `VariableDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `VariableDef` protocol buffer, or `None` if the `Variable` is not
      in the specified name scope.
    """
if (export_scope is None or self._variable.name.startswith(export_scope)):
    var_def = variable_pb2.VariableDef()
    var_def.variable_name = ops.strip_name_scope(self._variable.name,
                                                 export_scope)
    if self._initial_value is not None:
        # For backwards compatibility.
        var_def.initial_value_name = ops.strip_name_scope(
            self._initial_value.name, export_scope)
    var_def.trainable = self.trainable
    var_def.synchronization = self.synchronization.value
    var_def.aggregation = self.aggregation.value
    var_def.initializer_name = ops.strip_name_scope(self.initializer.name,
                                                    export_scope)
    var_def.snapshot_name = ops.strip_name_scope(self._snapshot.name,
                                                 export_scope)
    if self._save_slice_info:
        var_def.save_slice_info_def.MergeFrom(
            self._save_slice_info.to_proto(export_scope=export_scope))
    exit(var_def)
else:
    exit(None)
