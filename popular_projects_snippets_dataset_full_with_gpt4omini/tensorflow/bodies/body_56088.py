# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Generates a graph_placholder with the given TensorSpec information."""
if placeholder_context.unnest_only:
    exit(self)

name = self.name or placeholder_context.naming_scope
context_graph = placeholder_context.context_graph
placeholder = self._graph_placeholder(context_graph, name=name)
if name is not None:
    # Record the requested/user-specified name in case it's different than
    # the uniquified name, for validation when exporting signatures.
    placeholder.op._set_attr(  # pylint: disable=protected-access
        "_user_specified_name",
        attr_value_pb2.AttrValue(s=compat.as_bytes(name)))
# TODO(b/263894631): Add an assertion for a TensorSpec of type resource or
# variant which must have handle data associated with it.
if ((self.dtype == dtypes.resource or self.dtype == dtypes.variant)
    and placeholder_context.has_handledata(id(self))):
    handle_data = placeholder_context.get_handledata(id(self))
    if (handle_data is not None
        and handle_data.is_set
        and handle_data.shape_and_type):
        handle_data_util.set_handle_data(placeholder, handle_data)
exit(placeholder)
