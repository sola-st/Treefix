# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Converts a `CondContext` to a `CondContextDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `CondContextDef` protocol buffer.
    """
if (export_scope is None or self.name.startswith(export_scope)):
    context_def = control_flow_pb2.CondContextDef()
    context_def.context_name = ops.strip_name_scope(self.name, export_scope)
    context_def.pred_name = ops.strip_name_scope(self._pred.name,
                                                 export_scope)
    context_def.pivot_name = ops.strip_name_scope(self._pivot.name,
                                                  export_scope)
    context_def.branch = self._branch
    context_def.values_def.MergeFrom(
        super(CondContext, self)._to_values_def(export_scope))
    for nested in self._nested_contexts:
        nested_def = context_def.nested_contexts.add()
        nested.to_control_flow_context_def(nested_def)

    exit(context_def)
else:
    exit(None)
