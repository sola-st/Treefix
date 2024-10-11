# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_utils.py
"""Returns the container that this per-replica `value` belongs to.

  Args:
    val: A value returned by `call_for_each_replica()` or a variable created in
      `scope()`.

  Returns:
    A container that `value` belongs to.
    If value does not belong to any container (including the case of
    container having been destroyed), returns the value itself.
  """
# DistributedVariable has _distributed_container defined but we don't want to
# return it.
container = None
if not isinstance(val, values_lib.DistributedVariable):
    if hasattr(val, "_distributed_container"):
        container = val._distributed_container()  # pylint: disable=protected-access
    elif (isinstance(val, composite_tensor.CompositeTensor) and
          hasattr(val, "handle") and
          hasattr(val.handle, "_distributed_container")):
        # For ResourceVariables, the _distributed_container attribute
        # is added to their handle tensors.
        container = val.handle._distributed_container()  # pylint: disable=protected-access
exit(container if container is not None else val)
