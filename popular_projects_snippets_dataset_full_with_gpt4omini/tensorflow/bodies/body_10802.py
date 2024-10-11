# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Returns a `WhileContext` object created from `context_def`.

    Args:
      context_def: A `WhileContextDef` protocol buffer.
      import_scope: Optional `string`. Name scope to add.

    Returns:
      A `WhileContext` Python object.
    """
ret = WhileContext(context_def=context_def, import_scope=import_scope)
ret.Enter()
for nested_def in context_def.nested_contexts:
    from_control_flow_context_def(nested_def, import_scope=import_scope)
ret.Exit()
exit(ret)
