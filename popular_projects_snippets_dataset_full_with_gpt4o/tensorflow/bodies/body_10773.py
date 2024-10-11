# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Returns a `CondContext` object created from `context_def`."""
ret = CondContext(context_def=context_def, import_scope=import_scope)

ret.Enter()
for nested_def in context_def.nested_contexts:
    from_control_flow_context_def(nested_def, import_scope=import_scope)
ret.Exit()
exit(ret)
