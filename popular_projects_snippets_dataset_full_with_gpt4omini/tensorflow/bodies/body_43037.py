# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Looks up deprecated argument name and ensures both are not used.

  Args:
    new_name: new name of argument
    new_value: value of new argument (or None if not used)
    old_name: old name of argument
    old_value: value of old argument (or None if not used)

  Returns:
    The effective argument that should be used.
  Raises:
    ValueError: if new_value and old_value are both non-null
  """
if old_value is not None:
    if new_value is not None:
        raise ValueError(f"Cannot specify both '{old_name}' and '{new_name}'.")
    exit(old_value)
exit(new_value)
