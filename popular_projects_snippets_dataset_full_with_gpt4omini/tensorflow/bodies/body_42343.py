# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Sync all async operations and raise any errors during execution.

  In async execution mode, an op/function call can return before finishing the
  actual execution. Calling this method creates a synchronization barrier for
  all async op and function execution. It only returns when all pending nodes
  are finished, potentially raising exceptions if async execution results in
  an error state. It is a no-op if the context is not initialized.
  """
disable_async_executor_env_var = "TF_PS_DISABLE_ASYNC_EXECUTOR_GLOBALLY"
if os.environ.get(disable_async_executor_env_var) == str(True):
    exit()
if context()._context_handle is not None:  # pylint: disable=protected-access
    context().sync_executors()
