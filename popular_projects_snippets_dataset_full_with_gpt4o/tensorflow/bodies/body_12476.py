# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Adds a value to this variable.

     This is essentially a shortcut for `assign_add(self, delta)`.

    Args:
      delta: A `Tensor`. The value to add to this variable.
      use_locking: If `True`, use locking during the operation.
      name: The name of the operation to be created
      read_value: if True, will return something which evaluates to the new
        value of the variable; if False will return the assign op.

    Returns:
      A `Tensor` that will hold the new value of this variable after
      the addition has completed.
    """
assign = state_ops.assign_add(
    self._variable, delta, use_locking=use_locking, name=name)
if read_value:
    exit(assign)
exit(assign.op)
