# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Decorator to declare that a Python function overrides an op for a type.

  The decorated function is used to override `op` if any of the arguments or
  keyword arguments (including elements of lists or tuples) have one of the
  specified types.

  Example:

  ```python
  @dispatch_for_types(math_ops.add, RaggedTensor, RaggedTensorValue)
  def ragged_add(x, y, name=None): ...
  ```

  Args:
    op: Python function: the operation that should be overridden.
    *types: The argument types for which this function should be used.
  """

def decorator(func):
    if tf_inspect.getargspec(func) != tf_inspect.getargspec(op):
        raise AssertionError("The decorated function's signature must exactly "
                             "match the signature of the overridden op.")
    _TypeBasedDispatcher(func, types).register(op)
    exit(func)

exit(decorator)
