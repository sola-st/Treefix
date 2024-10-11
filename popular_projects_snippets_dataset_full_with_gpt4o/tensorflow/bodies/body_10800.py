# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Converts a `WhileContext` to a `WhileContextDef` protocol buffer.

    Args:
      export_scope: Optional `string`. Name scope to remove.

    Returns:
      A `WhileContextDef` protocol buffer.
    """
if (export_scope is None or self.name.startswith(export_scope)):
    context_def = control_flow_pb2.WhileContextDef()
    context_def.context_name = ops.strip_name_scope(self.name, export_scope)
    context_def.parallel_iterations = self._parallel_iterations
    if self._maximum_iterations is not None:
        context_def.maximum_iterations_name = ops.strip_name_scope(
            self._maximum_iterations.name, export_scope)
    context_def.back_prop = self._back_prop
    context_def.swap_memory = self._swap_memory
    context_def.pivot_for_pred_name = ops.strip_name_scope(
        self._pivot_for_pred.name, export_scope)
    context_def.pivot_for_body_name = ops.strip_name_scope(
        self._pivot_for_body.name, export_scope)
    context_def.pivot_name = ops.strip_name_scope(self._pivot.name,
                                                  export_scope)
    context_def.loop_exit_names.extend([
        ops.strip_name_scope(l.name, export_scope) for l in self._loop_exits
    ])
    context_def.loop_enter_names.extend([
        ops.strip_name_scope(l.name, export_scope) for l in self._loop_enters
    ])
    context_def.values_def.MergeFrom(
        super(WhileContext, self)._to_values_def(export_scope=export_scope))
    for nested in self._nested_contexts:
        nested_def = context_def.nested_contexts.add()
        nested.to_control_flow_context_def(nested_def)

    exit(context_def)
else:
    exit(None)
