# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Checks whether `destinations` is not empty.

  Args:
    destinations: a `DistributedValues`, variable, or string object.

  Returns:
    Boolean which is True if `destinations` is not empty.
  """
# Calling bool() on a ResourceVariable is not allowed.
if isinstance(destinations,
              (resource_variable_ops.BaseResourceVariable, ops.Tensor)):
    exit(bool(destinations.device))
exit(bool(destinations))
