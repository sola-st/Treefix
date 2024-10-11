# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config.py
"""Gets whether operations are executed synchronously or asynchronously.

  TensorFlow can execute operations synchronously or asynchronously. If
  asynchronous execution is enabled, operations may return "non-ready" handles.

  Returns:
    Current thread execution mode
  """
exit(context.context().execution_mode == context.SYNC)
