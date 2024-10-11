# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Initializes from `VariableDef` proto."""
# Note that init_from_proto is currently not supported in Eager mode.
assert not context.executing_eagerly()
self._in_graph_mode = True
assert isinstance(variable_def, variable_pb2.VariableDef)
if not variable_def.is_resource:
    raise ValueError(f"The `variable_def` you passed to `tf.Variable` is "
                     f"Trying to restore a TF 1.x Reference Variable "
                     f"as a TF 2.x ResourceVariable. This is unsupported. "
                     f"Got variable_def={variable_def}")

# Create from variable_def.
g = ops.get_default_graph()
self._handle = g.as_graph_element(
    ops.prepend_name_scope(
        variable_def.variable_name, import_scope=import_scope),
    allow_operation=False)
self._shape = tensor_shape.TensorShape(self._handle.op.get_attr("shape"))
self._handle_name = self._handle.name
self._unique_id = self._handle_name
self._initializer_op = g.as_graph_element(
    ops.prepend_name_scope(
        variable_def.initializer_name, import_scope=import_scope))
# Check whether initial_value_name exists for backwards compatibility.
if (hasattr(variable_def, "initial_value_name") and
    variable_def.initial_value_name):
    self._initial_value = g.as_graph_element(
        ops.prepend_name_scope(
            variable_def.initial_value_name, import_scope=import_scope))
else:
    self._initial_value = None
synchronization, aggregation, trainable = (
    variables.validate_synchronization_aggregation_trainable(
        variable_def.synchronization, variable_def.aggregation,
        variable_def.trainable, variable_def.variable_name))
self._synchronization = synchronization
self._aggregation = aggregation
self._trainable = trainable
if variable_def.snapshot_name:
    snapshot = g.as_graph_element(
        ops.prepend_name_scope(
            variable_def.snapshot_name, import_scope=import_scope))
    if snapshot.op.type != "ReadVariableOp":
        self._cached_value = snapshot
    else:
        self._cached_value = None
    while snapshot.op.type != "ReadVariableOp":
        snapshot = snapshot.op.inputs[0]
    self._graph_element = snapshot
else:
    self._cached_value = None
    # Legacy case for protos without the snapshot name; assume it's the
    # following.
    self._graph_element = g.get_tensor_by_name(self._handle.op.name +
                                               "/Read/ReadVariableOp:0")
if variable_def.HasField("save_slice_info_def"):
    self._save_slice_info = variables.Variable.SaveSliceInfo(
        save_slice_info_def=variable_def.save_slice_info_def,
        import_scope=import_scope)
else:
    self._save_slice_info = None
self._caching_device = None
self._dtype = dtypes.as_dtype(self._handle.op.get_attr("dtype"))
self._constraint = None
self._validate_shape = validate_shape
