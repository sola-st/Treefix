# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Create a new instance for the input ShardedVariable.

    Args:
      original_var: Input ShardedVariable object to be copied.
    """
copied_vars = []
for v in original_var._variables:  # pylint: disable=protected-access
    self._copy_for_variable(v)
    copied_vars.append(self._object_map[v])
self._object_map[original_var] = ShardedVariable(
    copied_vars, name=original_var.name)
