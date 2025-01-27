# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Create a new instance for the input trackable.

    Args:
      original_trackable: The trackable instance to be copied.

    Raises:
      AttributeError: if the input trackable is not Variable or ShardedVariable.
    """
if isinstance(original_trackable, ShardedVariable):
    self._copy_for_sharded_variable(original_trackable)
elif isinstance(original_trackable, Variable):
    self._copy_for_variable(original_trackable)
else:
    raise AttributeError("Only Variable or ShardedVariable can be copied.")
