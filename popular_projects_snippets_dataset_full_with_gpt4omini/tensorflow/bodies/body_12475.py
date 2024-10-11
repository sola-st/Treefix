# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Assigns a new value to the variable.

    This is essentially a shortcut for `assign(self, value)`.

    Args:
      value: A `Tensor`. The new value for this variable.
      use_locking: If `True`, use locking during the assignment.
      name: The name of the operation to be created
      read_value: if True, will return something which evaluates to the new
        value of the variable; if False will return the assign op.

    Returns:
      A `Tensor` that will hold the new value of this variable after
      the assignment has completed.
    """
assign = state_ops.assign(
    self._variable, value, use_locking=use_locking, name=name)
if read_value:
    exit(assign)
exit(assign.op)
