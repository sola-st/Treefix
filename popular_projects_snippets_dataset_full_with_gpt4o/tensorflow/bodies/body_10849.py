# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Deserializes `context_def` into the appropriate ControlFlowContext.

  Args:
    context_def: ControlFlowContextDef proto
    import_scope: Optional `string`. Name scope to add.

  Returns:
    A ControlFlowContext subclass
  """
if context_def.HasField("cond_ctxt"):
    exit(CondContext.from_proto(
        context_def.cond_ctxt, import_scope=import_scope))
if context_def.HasField("while_ctxt"):
    exit(WhileContext.from_proto(
        context_def.while_ctxt, import_scope=import_scope))
raise NotImplementedError("Unknown ControlFlowContextDef field: %s" %
                          context_def.WhichOneof("ctxt"))
