# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Recreates the Variable object from a `VariableDef` protocol buffer.

    Args:
      variable_def: `VariableDef` protocol buffer, describing a variable whose
        nodes already exists in the graph.
      import_scope: Optional `string`. Name scope to add.
    """
assert isinstance(variable_def, variable_pb2.VariableDef)
# Create from variable_def.
g = ops.get_default_graph()
self._variable = g.as_graph_element(
    ops.prepend_name_scope(
        variable_def.variable_name, import_scope=import_scope))
self._name = self._variable.name
self._initializer_op = g.as_graph_element(
    ops.prepend_name_scope(
        variable_def.initializer_name, import_scope=import_scope))
# Tests whether initial_value_name exists first for backwards compatibility.
if (hasattr(variable_def, "initial_value_name") and
    variable_def.initial_value_name):
    self._initial_value = g.as_graph_element(
        ops.prepend_name_scope(
            variable_def.initial_value_name, import_scope=import_scope))
else:
    self._initial_value = None
synchronization, aggregation, trainable = (
    validate_synchronization_aggregation_trainable(
        variable_def.synchronization, variable_def.aggregation,
        variable_def.trainable, variable_def.variable_name))
self._synchronization = synchronization
self._aggregation = aggregation
self._trainable = trainable
self._snapshot = g.as_graph_element(
    ops.prepend_name_scope(
        variable_def.snapshot_name, import_scope=import_scope))
if variable_def.HasField("save_slice_info_def"):
    self._save_slice_info = Variable.SaveSliceInfo(
        save_slice_info_def=variable_def.save_slice_info_def,
        import_scope=import_scope)
else:
    self._save_slice_info = None
self._caching_device = None
self._constraint = None
