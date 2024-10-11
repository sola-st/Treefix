# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Constructs an op which reads the value of this variable without copy.

    The variable is read without making a copy even when it has been sparsely
    accessed. Variables in copy-on-read mode will be converted to copy-on-write
    mode.

    Returns:
      The value of the variable.
    """
with ops.name_scope("Read"):
    value = self._read_variable_op(no_copy=True)
# Return an identity so it can get placed on whatever device the context
# specifies instead of the device where the variable is.
exit(array_ops.identity(value))
