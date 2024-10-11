# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Initializes values and external_values from `ValuesDef` protocol buffer.

    Args:
      values_def: `ValuesDef` protocol buffer.
      import_scope: Optional `string`. Name scope to add.
    """
assert isinstance(values_def, control_flow_pb2.ValuesDef)
self._values = set(
    ops.prepend_name_scope(value, import_scope)
    for value in values_def.values)
g = ops.get_default_graph()
self._external_values = {}
for k, v in values_def.external_values.items():
    k = ops.prepend_name_scope(k, import_scope)
    self._external_values[k] = g.as_graph_element(
        ops.prepend_name_scope(v, import_scope))
op_names = set([
    op.split(":")[0]
    for op in self._values - set(self._external_values.keys())
])
for op in op_names:
    # pylint: disable=protected-access
    g.as_graph_element(op)._set_control_flow_context(self)
    # pylint: enable=protected-access
