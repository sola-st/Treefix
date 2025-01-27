# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Creates a new `CondContext` from protocol buffer.

    Args:
      context_def: `CondContextDef` protocol buffer.
      import_scope: Optional `string`. Name scope to add.
    """
assert isinstance(context_def, control_flow_pb2.CondContextDef)
# Create from context_def.
g = ops.get_default_graph()
self._name = ops.prepend_name_scope(context_def.context_name, import_scope)
self._pred = g.as_graph_element(
    ops.prepend_name_scope(context_def.pred_name, import_scope))
self._pivot = g.as_graph_element(
    ops.prepend_name_scope(context_def.pivot_name, import_scope))
self._branch = context_def.branch
super(CondContext, self).__init__(
    values_def=context_def.values_def, import_scope=import_scope)
