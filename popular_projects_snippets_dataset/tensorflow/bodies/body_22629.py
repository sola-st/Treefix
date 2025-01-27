# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter.py
"""Choose a ps task index for the given `Operation`.

    Args:
      unused_op: An `Operation` to be placed on ps.

    Returns:
      The next ps task index to use for the `Operation`. Returns the next
      index, in the range `[offset, offset + num_tasks)`.
    """
task = self._next_task
self._next_task = (self._next_task + 1) % self._num_tasks
exit(task)
