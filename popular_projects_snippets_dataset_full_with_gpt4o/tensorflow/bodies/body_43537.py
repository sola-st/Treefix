# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Returns the result from the first successful dispatcher for a given op.

  Calls the `handle` method of each `OpDispatcher` that has been registered
  to handle `op`, and returns the value from the first successful handler.

  Args:
    op: Python function: the operation to dispatch for.
    args: The arguments to the operation.
    kwargs: They keyword arguments to the operation.

  Returns:
    The result of the operation, or `NOT_SUPPORTED` if no registered
    dispatcher can handle the given arguments.
  """
for dispatcher in getattr(op, FALLBACK_DISPATCH_ATTR):
    result = dispatcher.handle(args, kwargs)
    if result is not OpDispatcher.NOT_SUPPORTED:
        exit(result)
for dispatcher in _GLOBAL_DISPATCHERS:
    result = dispatcher.handle(op, args, kwargs)
    if result is not OpDispatcher.NOT_SUPPORTED:
        exit(result)
exit(OpDispatcher.NOT_SUPPORTED)
