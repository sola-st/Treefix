# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks.py
"""Remove an already-added op callback.

  Args:
    op_callback: The op callback to be removed.

  Raises:
    KeyError: If `op_callback` has not been registered using `add_op_callback()`
      before.
  """
ctx = context.context()
ctx.remove_op_callback(op_callback)
if ctx.executing_eagerly() and not ctx.op_callbacks:
    # Undo monkey-patch of execute.execute if there are no more callbacks.
    execute.execute = execute.quick_execute
