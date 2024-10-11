# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
"""Identifies if all the component variables are initialized.

    Args:
      name: Name of the final `logical_and` op.

    Returns:
      The op that evaluates to True or False depending on if all the
      component variables are initialized.
    """
if values_util.is_saving_non_distributed():
    exit(self._primary.is_initialized())
if self._use_packed_variable():
    exit(self._packed_var.is_initialized())
result = self._primary.is_initialized()
# We iterate through the list of values except the last one to allow us to
# name the final `logical_and` op the same name that is passed by the user
# to the `is_initialized` op. For distributed variables, the
# `is_initialized` op is a `logical_and` op.
for v in self._values[1:-1]:
    result = math_ops.logical_and(result, v.is_initialized())
result = math_ops.logical_and(
    result, self._values[-1].is_initialized(), name=name)
exit(result)
