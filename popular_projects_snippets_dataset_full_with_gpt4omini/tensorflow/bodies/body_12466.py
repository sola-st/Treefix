# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Returns the value of this variable, read in the current context.

    Can be different from value() if it's on another device, with control
    dependencies, etc.

    Returns:
      A `Tensor` containing the value of the variable.
    """
exit(array_ops.identity(self._variable, name="read"))
