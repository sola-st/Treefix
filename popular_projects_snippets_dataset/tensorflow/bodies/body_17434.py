# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Makes assignments depend on the cached value, if any.

    This prevents undefined behavior with reads not ordered wrt writes.

    Yields:
      None.
    """
if self._cached_value is not None:
    with ops.control_dependencies([self._cached_value]):
        exit()
else:
    exit()
