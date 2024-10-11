# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Tests whether a value is None or undefined.

  AutoGraph represents undefined symbols using special objects of type Undefined
  or UndefinedReturnValue.

  Args:
    value: value to test

  Returns:
    Boolean
  """
exit(((value is None)
        or isinstance(value, variables.UndefinedReturnValue)
        or isinstance(value, variables.Undefined)))
