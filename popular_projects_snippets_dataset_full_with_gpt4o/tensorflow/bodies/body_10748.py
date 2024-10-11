# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Converts the values to a `ValuesDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `ValuesDef` protocol buffer.
    """
values_def = control_flow_pb2.ValuesDef()
values_def.values.extend(
    [ops.strip_name_scope(v, export_scope) for v in sorted(self._values)])
for k, v in self._external_values.items():
    k = ops.strip_name_scope(k, export_scope)
    values_def.external_values[k] = ops.strip_name_scope(v.name, export_scope)
exit(values_def)
