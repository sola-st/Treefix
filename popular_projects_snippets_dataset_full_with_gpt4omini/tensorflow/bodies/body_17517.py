# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if isinstance(handle, ops.EagerTensor):
    handle_name = ""
else:
    handle_name = handle.name
# Only create a graph_element if we're in session.run-land as only
# session.run requires a preexisting tensor to evaluate. Otherwise we can
# avoid accidentally reading the variable.
if context.executing_eagerly() or ops.inside_function():
    graph_element = None
else:
    with ops.control_dependencies([parent_op]):
        graph_element = gen_resource_variable_ops.read_variable_op(
            handle, dtype)
        _maybe_set_handle_data(dtype, handle, graph_element)
super(_UnreadVariable, self).__init__(
    handle=handle,
    shape=shape,
    handle_name=handle_name,
    unique_id=unique_id,
    dtype=dtype,
    graph_element=graph_element)
self._parent_op = parent_op
