# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Context manager for changing executor for current thread.

  Args:
    e: A Executor to execute eager ops under this scope. Setting it to None will
      switch back to use the default executor for the context.

  Yields:
    Context manager for setting the executor for current thread.
  """
ctx = context()
executor_old = ctx.executor
try:
    ctx.executor = e
    exit()
finally:
    ctx.executor = executor_old
