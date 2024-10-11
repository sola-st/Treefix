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
      The updated variable. If `read_value` is false, instead returns None in
      Eager mode and the assign op in graph mode.
    """
raise NotImplementedError
