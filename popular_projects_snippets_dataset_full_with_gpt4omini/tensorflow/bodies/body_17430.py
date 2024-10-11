# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Records that `variable` was accessed for the tape and FuncGraph."""
if hasattr(ops.get_default_graph(), "watch_variable"):
    ops.get_default_graph().watch_variable(variable)
if variable.trainable:
    tape.variable_accessed(variable)
