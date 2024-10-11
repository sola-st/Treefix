# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Creates a new `WhileContext` from protocol buffer.

    Args:
      context_def: `WhileContextDef` protocol buffer.
      import_scope: Optional `string`. Name scope to add.
    """
assert isinstance(context_def, control_flow_pb2.WhileContextDef)
# Create from context_def.
g = ops.get_default_graph()
self._name = ops.prepend_name_scope(context_def.context_name, import_scope)
if context_def.maximum_iterations_name:
    self._maximum_iterations = g.as_graph_element(
        ops.prepend_name_scope(context_def.maximum_iterations_name,
                               import_scope))
else:
    self._maximum_iterations = None
self._parallel_iterations = context_def.parallel_iterations
self._back_prop = context_def.back_prop
self._swap_memory = context_def.swap_memory
self._pivot_for_pred = g.as_graph_element(
    ops.prepend_name_scope(context_def.pivot_for_pred_name, import_scope))
# We use this node to control constants created by the body lambda.
self._pivot_for_body = g.as_graph_element(
    ops.prepend_name_scope(context_def.pivot_for_body_name, import_scope))
# The boolean tensor for loop termination condition. Used in code
# generation for gradient computation.
self._pivot = g.as_graph_element(
    ops.prepend_name_scope(context_def.pivot_name, import_scope))
# The list of exit tensors for loop variables.
self._loop_exits = [
    g.as_graph_element(ops.prepend_name_scope(exit_name, import_scope))
    for exit_name in context_def.loop_exit_names
]
# The list of enter tensors for loop variables.
self._loop_enters = [
    g.as_graph_element(ops.prepend_name_scope(enter_name, import_scope))
    for enter_name in context_def.loop_enter_names
]
super(WhileContext, self).__init__(
    values_def=context_def.values_def, import_scope=import_scope)

# import_scope causes self.name to be different from the original serialized
# context's name. Rewrite "frame_name" attrs with the new name.
if import_scope:
    for tensor_name in self._values:
        op = g.as_graph_element(tensor_name).op
        if util.IsLoopEnter(op):
            # pylint: disable=protected-access
            op._set_attr("frame_name",
                         attr_value_pb2.AttrValue(s=compat.as_bytes(self.name)))
            # pylint: enable=protected-access
self._graph = ops.get_default_graph()
