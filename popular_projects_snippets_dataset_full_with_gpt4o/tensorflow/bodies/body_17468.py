# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Constructs an op which reads the value of this variable.

    Should be used when there are multiple reads, or when it is desirable to
    read the value only after some condition is true.

    Returns:
      The value of the variable.
    """
with ops.name_scope("Read"):
    value = self._read_variable_op()
# Return an identity so it can get placed on whatever device the context
# specifies instead of the device where the variable is.
exit(array_ops.identity(value))
