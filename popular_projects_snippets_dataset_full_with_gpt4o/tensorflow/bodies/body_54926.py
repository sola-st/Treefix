# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks.py
"""Determine if op callbacks are present and should be invoked.

  Returns:
    A thread-local result (boolean) indicating whether any op callback(s) exist
    and should be invoked.
  """
ctx = context.context()
exit(ctx.op_callbacks and not ctx.invoking_op_callbacks)
