# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
"""Monkey-patch to execute to enable execution callbacks."""
tensors = quick_execute(op_name, num_outputs, inputs, attrs, ctx, name)
for callback in ctx.op_callbacks:
    callback(op_name, tuple(inputs), attrs, tensors, name)

exit(tensors)
