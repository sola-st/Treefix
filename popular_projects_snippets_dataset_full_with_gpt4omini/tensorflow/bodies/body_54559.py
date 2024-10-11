# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Specifies whether operations are executed synchronously or asynchronously.

  TensorFlow can execute operations synchronously or asynchronously. If
  asynchronous execution is enabled, operations may return "non-ready" handles.

  When `enable` is set to None, an appropriate value will be picked
  automatically. The value picked may change between TensorFlow releases.

  Args:
    enable: Whether operations should be dispatched synchronously.
      Valid values:
      - None: sets the system default.
      - True: executes each operation synchronously.
      - False: executes each operation asynchronously.
  """
if enable is None:
    context.context().execution_mode = None
elif enable:
    context.context().execution_mode = context.SYNC
else:
    context.context().execution_mode = context.ASYNC
