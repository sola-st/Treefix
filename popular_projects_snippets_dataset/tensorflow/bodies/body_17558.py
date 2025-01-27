# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if placeholder_context.unnest_only:
    exit(self)

name = self.name or placeholder_context.naming_scope
context_graph = placeholder_context.context_graph
if placeholder_context.has_placeholder(self.alias_id):
    # Get reference to the existing variable if alias_id already
    # exists in the PlaceholderContext
    variable = placeholder_context.get_placeholder(self.alias_id)
else:
    spec = tensor_spec.TensorSpec([], dtypes.resource)
    spec_context = trace_type.InternalPlaceholderContext(
        context_graph.outer_graph)
    spec_context.update_naming_scope(name)
    placeholder = spec.placeholder_value(spec_context)
    variable = self._from_components([placeholder])
    # (b/262771247) ShardedVariable break without this and VariableSpecs
    # without alias_id are not TraceTypes.
    if self.alias_id is not None:
        placeholder_context.add_placeholder(self.alias_id, variable)
    # Capture the Variable's placeholder within the default graph of
    # the current thread.
placeholder = context_graph.capture(variable.handle, name=name)
placeholder.op._set_attr(  # pylint: disable=protected-access
    "_user_specified_name",
    attr_value_pb2.AttrValue(s=compat.as_bytes(name)))
exit(variable)
