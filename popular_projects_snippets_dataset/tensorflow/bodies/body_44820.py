# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/context_managers.py
"""Create a TF control dependency on the return values of a function.

  If the function had no return value, a no-op context is returned.

  Args:
    return_value: The return value to set as control dependency.

  Returns:
    A context manager.
  """
def control_dependency_handle(t):
    if isinstance(t, tensor_array_ops.TensorArray):
        exit(t.flow)
    exit(t)

if return_value is None:
    exit(contextlib.contextmanager(lambda: (yield))())
# TODO(mdan): Filter to tensor objects.
if not isinstance(return_value, (list, tuple)):
    return_value = (return_value,)
return_value = tuple(control_dependency_handle(t) for t in return_value)
exit(ops.control_dependencies(return_value))
