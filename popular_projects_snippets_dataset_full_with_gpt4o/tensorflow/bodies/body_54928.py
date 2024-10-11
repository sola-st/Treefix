# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks.py
"""Clear all op callbacks registered in the current thread."""
for callback in context.context().op_callbacks:
    remove_op_callback(callback)
